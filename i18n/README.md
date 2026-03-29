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
| `section_titles.yaml` | Localized section headings for common `required_sections` entries |

## Supported Languages

| Code | Language | Factory | Status |
|------|----------|---------|--------|
| `en` | English | — | Ground truth |
| `zh-CN` | Simplified Chinese | 深圳 (Shenzhen) | ✅ Complete |
| `zh-TW` | Traditional Chinese | 台湾 (Taiwan) | ✅ Complete |
| `vi` | Vietnamese | Vietnam | 🔲 Stub (pending) |

## Usage by RAG Agent

```python
import yaml
from pathlib import Path

doc_titles = yaml.safe_load(Path("i18n/doc_titles.yaml").read_text())
section_titles = yaml.safe_load(Path("i18n/section_titles.yaml").read_text())

def get_doc_title(doc_id: str, lang: str = "en") -> str:
    entry = doc_titles.get(doc_id, {})
    return entry.get(lang) or entry.get("en", doc_id)

def get_section_title(en_heading: str, lang: str = "en") -> str:
    if lang == "en":
        return en_heading
    entry = section_titles.get(en_heading, {})
    return entry.get(lang) or en_heading
```

### System Prompt Integration

When generating a localized document, the agent should:

1. Load the relevant GLOSSARY.md multilingual canonical forms as terminology constraints
2. Use `doc_titles.yaml` to set the document title in the target language
3. Use `section_titles.yaml` to translate section headings
4. Apply terminology from `GLOSSARY.md` `**Canonical Form (zh-CN/zh-TW):**` lines

Example snippet for a zh-CN document generation prompt:

```
Language: Simplified Chinese (zh-CN)
Document: {get_doc_title(doc_id, "zh-CN")}

Terminology constraints (use these exact forms):
- 良率 (not 收率)
- 测试逃逸 (not 漏测)
- 可追溯性 (not 可追踪性)

Section headings:
## {get_section_title("Purpose and Scope", "zh-CN")}
## {get_section_title("Test Coverage", "zh-CN")}
...
```

## Adding Vietnamese (vi) Support

When ready to add full Vietnamese support:

1. Replace all `vi: "(pending)"` entries in `doc_titles.yaml` and `section_titles.yaml`
2. Add `**Canonical Form (vi):**` lines in `GLOSSARY.md` for all 59 terms
3. Update the table above to mark vi as Complete

## Coverage

- `doc_titles.yaml`: 136 entries (131 lifecycle docs + 5 shared snippets)
- `section_titles.yaml`: 35 common section headings
