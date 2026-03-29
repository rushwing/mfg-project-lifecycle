# Agentic RAG Inference Architecture

Reference design for on-premise LLM inference serving the MFG Lifecycle KB document generation agent.

---

## Overview

The RAG agent generates manufacturing documents (TRP, FA reports, yield dashboards, etc.) in multiple languages from a single English KB. The inference stack must handle:

- **High-throughput batch generation**: PVT ramp may require 50–100 documents per build cycle
- **Structured output**: Every document must conform to required_sections and frontmatter schema
- **Multilingual terminology constraints**: GLOSSARY.md canonical forms in zh-CN/zh-TW must appear verbatim
- **Long shared context**: GLOSSARY.md (~900 lines after i18n additions) is included in every prompt as a terminology anchor

Recommended stack: **SGLang + PD Separation + Radix Attention + xGrammar structured output**

---

## Component Roles

### SGLang

SGLang is the inference runtime. Key advantages for this use case:

- **RadixAttention**: Automatic KV cache reuse across requests sharing a common prefix. The GLOSSARY.md system prompt (~6 KB of tokens) is shared across all document generation calls — RadixAttention caches this prefix once, dramatically reducing TTFT for subsequent requests.
- **Continuous batching**: Multiple document stubs can be generated in parallel without blocking on individual completions.
- **Structured output via xGrammar**: Grammar-constrained decoding ensures the model cannot generate malformed YAML frontmatter or skip required sections.
- **OpenAI-compatible API**: Drop-in for Python clients using the `openai` SDK.

### Prefill-Decode (PD) Separation

For document generation, the prompt (GLOSSARY + retrieval context + template stub) is 4–8× longer than the generated output. PD separation assigns prefill to dedicated high-throughput GPUs and decode to latency-optimized GPUs.

Recommended split for a 2-GPU node:
- **Prefill worker**: 1× H100 (or A100 80GB) — processes the long KB context
- **Decode worker**: 1× A100 40GB or L40S — generates output tokens

For CPU-only or budget deployments: disable PD separation and use a single worker with `--mem-fraction-static 0.85`.

### Radix Attention and GLOSSARY.md

The GLOSSARY.md file is designed as a shared system prompt prefix:

```
[System]
You are a manufacturing document generation assistant.
Terminology constraints (use canonical forms exactly):

<GLOSSARY.md contents — all 59 terms with zh-CN/zh-TW canonical forms>
```

Because all requests in a generation batch share this prefix, RadixAttention reuses the KV cache computed on the first request. For a batch of 20 documents, only 1 prefill computation occurs for the shared 6 KB GLOSSARY prefix — the remaining 19 requests read from cache.

Cache hit rate degrades if the system prompt is modified between requests. Keep GLOSSARY.md as a stable, prepended block; do not interleave retrieval chunks into it.

### xGrammar Structured Output

Each document template has a `required_sections` list. The agent must generate all sections in order without hallucinating extra headings or omitting required ones.

Grammar constraint approach:
1. Build a JSON Schema or BNF grammar from `required_sections` at generation time
2. Pass to SGLang via `--constrained-decoding-backend xgrammar`
3. The decoder is prevented from emitting tokens that would violate the section sequence

For YAML frontmatter, use a grammar that enforces the schema from `schemas/template_frontmatter.schema.json`. This eliminates the need for post-generation validation in the hot path.

**When to use grammar vs regex constraints:**

| Scenario | Use |
|----------|-----|
| Required sections in order | Grammar (BNF/JSON Schema) |
| `doc_id` format `{PHASE}-CP{N}-{SHORT}-{SEQ3}` | Regex |
| Status enum values | Grammar (enum constraint) |
| Free-text body within a section | None — let the model generate freely |

---

## i18n Generation Flow

```
User request: "Generate DVT-CP5-YTR-003 in zh-CN"
        │
        ▼
1. Load system prompt
   ├── GLOSSARY.md (with zh-CN canonical forms)     ← shared, cached by RadixAttention
   └── i18n/doc_titles.yaml entry for DVT-CP5-YTR-003

2. RAG retrieval
   ├── Retrieve relevant shared/_snippets/ chunks (yield analysis boilerplate)
   └── Retrieve related docs (DVT-CP4-UPH-001, DVT-CP5-FAR-001) for cross-references

3. Build prompt
   ├── [SYSTEM] GLOSSARY.md prefix (6 KB, cached)
   ├── [USER] Document title: "良率趋势报告" (from doc_titles.yaml)
   ├── [USER] Required sections: from DVT-CP5-YTR-003 frontmatter
   ├── [USER] Terminology: use "良率" not "收率", "测试逃逸" not "漏测", etc.
   └── [USER] Retrieved context chunks

4. SGLang inference
   ├── Grammar: enforce required_sections in order
   ├── Radix cache hit on GLOSSARY prefix
   └── Generate document body in zh-CN

5. Post-process
   ├── Inject frontmatter (doc_id, title from doc_titles.yaml, lang: zh-CN)
   ├── Validate required_sections present (grammar should guarantee this)
   └── Output: Markdown or DOCX via pandoc
```

---

## GPU Configuration

### Minimum (single-GPU, development)

- 1× A100 40GB or RTX 4090 24GB
- Model: Qwen2.5-14B-Instruct or LLaMA-3.1-8B-Instruct (multilingual)
- Context: 32K tokens (sufficient for GLOSSARY + 3–4 retrieved chunks + output)
- Throughput: ~5–10 documents/minute

### Recommended (production, PVT ramp)

- 2× H100 80GB (PD separated)
- Model: Qwen2.5-72B-Instruct (superior zh-CN/zh-TW quality)
- Context: 128K tokens
- Throughput: ~30–50 documents/minute

### Model Selection

For zh-CN/zh-TW manufacturing terminology, prefer models with strong Chinese pretraining:

| Model | zh quality | Context | Notes |
|-------|-----------|---------|-------|
| Qwen2.5-72B-Instruct | Excellent | 128K | Best overall; large VRAM requirement |
| Qwen2.5-32B-Instruct | Very good | 128K | Good balance |
| Qwen2.5-14B-Instruct | Good | 128K | Single A100 40GB feasible |
| LLaMA-3.1-70B-Instruct | Good | 128K | Better English; weaker zh terminology |
| DeepSeek-V2.5 | Excellent | 128K | Strong zh; MoE architecture |

---

## SGLang Deployment

### Install

```bash
pip install sglang[all]
# or with uv:
uv add sglang
```

### Launch server (single GPU)

```bash
python -m sglang.launch_server \
  --model-path Qwen/Qwen2.5-14B-Instruct \
  --port 30000 \
  --context-length 32768 \
  --constrained-decoding-backend xgrammar \
  --mem-fraction-static 0.85
```

### Launch server (PD separated, 2 GPUs)

```bash
# Prefill worker (GPU 0)
CUDA_VISIBLE_DEVICES=0 python -m sglang.launch_server \
  --model-path Qwen/Qwen2.5-72B-Instruct \
  --port 30000 \
  --disaggregation-mode prefill \
  --context-length 131072

# Decode worker (GPU 1)
CUDA_VISIBLE_DEVICES=1 python -m sglang.launch_server \
  --model-path Qwen/Qwen2.5-72B-Instruct \
  --port 30001 \
  --disaggregation-mode decode \
  --prefill-server-url http://localhost:30000
```

### Client example

```python
from openai import OpenAI
import yaml
from pathlib import Path

client = OpenAI(base_url="http://localhost:30000/v1", api_key="none")

glossary = Path("GLOSSARY.md").read_text()
doc_titles = yaml.safe_load(Path("i18n/doc_titles.yaml").read_text())
section_titles = yaml.safe_load(Path("i18n/section_titles.yaml").read_text())

def generate_document(doc_id: str, lang: str = "zh-CN", context_chunks: list[str] = None):
    title = doc_titles[doc_id].get(lang, doc_titles[doc_id]["en"])

    system_prompt = f"""You are a manufacturing document generation assistant for {
        '深圳工厂' if lang == 'zh-CN' else '台灣工廠' if lang == 'zh-TW' else 'the factory'
    }.
Always use the canonical terminology defined below. Do not use aliases.

{glossary}
"""

    user_prompt = f"Generate document: {title} ({doc_id})\nLanguage: {lang}\n"
    if context_chunks:
        user_prompt += "\nRelevant context:\n" + "\n---\n".join(context_chunks)

    response = client.chat.completions.create(
        model="Qwen2.5-14B-Instruct",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,  # low temperature for structured documents
        max_tokens=4096,
    )
    return response.choices[0].message.content
```

---

## Radix Attention Cache Warming

To maximize cache hit rate at the start of a generation batch, send a single "warm-up" request containing only the GLOSSARY system prompt before dispatching the full batch:

```python
# Warm the cache with the shared prefix
client.chat.completions.create(
    model="Qwen2.5-14B-Instruct",
    messages=[{"role": "system", "content": glossary_system_prompt}],
    max_tokens=1,  # minimal generation — we only need the prefill cached
)

# Now dispatch all document generation requests in parallel
import asyncio
tasks = [generate_document(doc_id, lang) for doc_id, lang in batch]
results = await asyncio.gather(*tasks)
```

---

## Output Formats

The LLM generates Markdown. For factory floor use, convert to DOCX or PDF:

```bash
# Markdown → DOCX (Word)
pandoc output.md -o output.docx --reference-doc=templates/factory-doc-template.docx

# Markdown → PDF
pandoc output.md -o output.pdf --pdf-engine=xelatex \
  -V CJKmainfont="Noto Sans CJK SC"  # for zh-CN
```

For zh-TW PDF: use `Noto Sans CJK TC` or `AR PL UMing TW`.

---

## Relationship to KB Structure

```
KB (English ground truth)
├── GLOSSARY.md              → system prompt prefix (terminology constraints)
│   └── Canonical Form (zh-CN/zh-TW) lines → enforce terminology in target lang
├── *-template.md            → required_sections → grammar constraints
├── _index.yaml              → doc_id, title, controlled_terms → retrieval metadata
├── shared/_snippets/*.md    → boilerplate chunks → RAG retrieval candidates
└── i18n/
    ├── doc_titles.yaml      → localized document titles
    └── section_titles.yaml  → localized section headings
```

The inference layer reads from the KB but never writes back to it. The KB remains the single source of truth; the LLM output is the ephemeral artifact.
