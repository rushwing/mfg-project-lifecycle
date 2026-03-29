# i18n — Internationalization Configuration

This directory contains localization data for the MFG Lifecycle KB.

## Design Principle

**English Markdown is the single ground truth.** All template content, frontmatter, and `_index.yaml` definitions remain in English. This directory provides *translation lookup tables* that a RAG agent or document generation script reads at generation time to produce localized output.

Benefits:
- No content duplication across languages
- Single source for validation (CI only runs against English)
- New language support requires only adding entries here, not touching templates

## Files

| File | Purpose |
|------|---------|
| `doc_titles.yaml` | Localized document titles keyed by `doc_id` |
| `section_titles.yaml` | Localized headings for universal structural sections (see below) |

## Supported Languages

| Code | Language | Factory | doc_titles | section_titles |
|------|----------|---------|-----------|---------------|
| `en` | English | — | Ground truth | Ground truth |
| `zh-CN` | Simplified Chinese | 深圳 | ✅ 136/136 | ✅ Structural (8/456 labels; remainder via RAG) |
| `zh-TW` | Traditional Chinese | 台湾 | ✅ 136/136 | ✅ Structural (8/456 labels; remainder via RAG) |
| `vi` | Vietnamese | Vietnam | 🔲 Stub | 🔲 Stub |

## Two-Tier Section Heading Localization

There are 456 unique section-heading labels across all 136 templates.
`section_titles.yaml` covers only ~8 **universal structural headings** that appear in almost every document (Purpose and Scope, Revision History, Exit Criteria, etc.).

The remaining ~448 headings are **document-specific** (e.g. "Coverage Summary by Station", "Bottleneck Station Identification", "BIST Coverage Requirements"). These cannot be enumerated statically — they are different for every template. They are translated **dynamically by the RAG agent at generation time**:

```
Static path  (this file):
  "Purpose and Scope" → "目的与范围"        ← consistent terminology guaranteed

Dynamic path (RAG agent at runtime):
  "Coverage Summary by Station"
    → LLM translates in-context, anchored to GLOSSARY.md canonical forms
    → SGLang xGrammar ensures output is well-formed Markdown
    → GLOSSARY.md controlled terms prevent drift ("良率" not "收率")
```

The static table exists to lock down headings where consistent terminology matters across documents (e.g. "Revision History" must always be "版本历史", not "修订记录"). For document-specific headings, in-context LLM translation with GLOSSARY constraints is sufficient.

## Usage by RAG Agent

```python
import re
import yaml
from pathlib import Path

doc_titles = yaml.safe_load(Path("i18n/doc_titles.yaml").read_text())
section_titles = yaml.safe_load(Path("i18n/section_titles.yaml").read_text())

def get_doc_title(doc_id: str, lang: str = "en") -> str:
    entry = doc_titles.get(doc_id, {})
    return entry.get(lang) or entry.get("en", doc_id)

def get_section_title(en_heading: str, lang: str = "en") -> str:
    """Localize a section heading using the static lookup table.

    required_sections values are numbered: "1. Purpose and Scope".
    section_titles.yaml is keyed by bare labels: "Purpose and Scope".
    This function strips the leading "N. " prefix for lookup, then
    re-attaches it to the localized result.

    Returns the original en_heading unchanged if:
    - lang == "en", OR
    - the bare label is not in section_titles.yaml (document-specific
      heading — delegate to the RAG agent for in-context translation).
    """
    if lang == "en":
        return en_heading
    prefix_match = re.match(r"^(\d+\.\s+)(.*)", en_heading)
    if prefix_match:
        prefix, bare = prefix_match.group(1), prefix_match.group(2)
    else:
        prefix, bare = "", en_heading
    entry = section_titles.get(bare, {})
    localized = entry.get(lang)
    if not localized:
        # Not in static table — caller should pass to RAG agent for translation
        return en_heading
    return prefix + localized
```

### System Prompt Integration

When generating a localized document, the agent should:

1. Load GLOSSARY.md multilingual canonical forms as terminology constraints (shared prefix — cached by Radix Attention)
2. Use `doc_titles.yaml` to set the document title in the target language
3. For each `required_sections` heading: try `get_section_title()` first; if it returns the English heading unchanged, include it in the LLM prompt for in-context translation
4. Apply GLOSSARY.md `**Canonical Form (zh-CN/zh-TW):**` lines to anchor controlled vocabulary

Example instruction block in the zh-CN generation prompt:

```
Language: Simplified Chinese (zh-CN)
Document: {get_doc_title(doc_id, "zh-CN")}

Terminology constraints — use these exact forms, do not use aliases:
- 良率 (not 收率)
- 测试逃逸 (not 漏测)
- 可追溯性 (not 可追踪性)
[... full GLOSSARY.md zh-CN terms ...]

Translate the following section headings to Simplified Chinese, preserving
the number prefix, and respecting terminology constraints above:
{headings_needing_dynamic_translation}

Then generate the full document body under each translated heading.
```

## Adding Vietnamese (vi) Support

When ready to add full Vietnamese support:

1. Replace all `vi: "(pending)"` entries in `doc_titles.yaml` and `section_titles.yaml`
2. Add `**Canonical Form (vi):**` lines in `GLOSSARY.md` for all 59 terms (currently stubbed as `*(pending)*`)
3. Update the language table above

## Coverage

- `doc_titles.yaml`: 136 entries (131 lifecycle docs + 5 shared snippets)
- `section_titles.yaml`: 8 universal structural headings with zh-CN/zh-TW translations; document-specific headings handled by RAG agent at runtime
