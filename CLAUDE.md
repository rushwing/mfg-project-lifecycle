# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

```bash
# Install dependencies (requires uv)
uv sync

# Validate all template frontmatter against JSON Schema + check doc_id uniqueness
uv run python scripts/validate_frontmatter.py

# Check every controlled_term in templates exists as a canonical form in GLOSSARY.md
uv run python scripts/check_term_consistency.py

# Verify _index.yaml slugs map to real files; check related_docs cross-references
uv run python scripts/validate_structure.py

# Regenerate DOC_INDEX.md (also runs automatically on push to main via CI)
uv run python scripts/generate_doc_index.py

# Generate missing template stubs from _index.yaml (idempotent — never overwrites)
uv run python scripts/bootstrap_templates.py [--dry-run] [--phase EVT] [--force]

# Bump KB version and rotate CHANGELOG.md
uv run python scripts/bump_version.py patch|minor|major [--dry-run]

# Full local validation (mirrors what CI runs on PRs)
uv run python scripts/validate_frontmatter.py && \
uv run python scripts/check_term_consistency.py && \
uv run python scripts/validate_structure.py && \
uv run python scripts/validate_i18n.py
```

## Architecture

### Content model

This is a **DITA-lite knowledge base**: structured Markdown files with YAML frontmatter, not a software application. The Python scripts are tooling that operates on the KB, not the product itself.

The core data flow is:

```
_index.yaml (source of truth)
    → bootstrap_templates.py → *-template.md stubs
    → validate_structure.py  → CI gate (index ↔ files in sync)

*-template.md frontmatter
    → validate_frontmatter.py → CI gate (schema compliance + doc_id uniqueness)
    → check_term_consistency.py → CI gate (controlled_terms ↔ GLOSSARY.md)
    → generate_doc_index.py → DOC_INDEX.md
```

### Two-level metadata hierarchy

- `{phase}/_manifest.yaml` — phase-level metadata (sequence, duration, milestones)
- `{phase}/{checkpoint}/_index.yaml` — checkpoint-level document registry; this is the **source of truth** for which template files should exist and what their frontmatter should contain

When adding a new template, edit `_index.yaml` first, then run `bootstrap_templates.py`. Never hand-create templates without a corresponding `_index.yaml` entry.

### doc_id primary key

Format: `{PHASE}-CP{N}-{DOC_SHORT}-{SEQ3}` (e.g. `EVT-CP2-TRP-001`)
Shared snippets: `SHARED-{TYPE}-{SHORT}-{SEQ3}` (e.g. `SHARED-SNIP-PFC-001`)

`doc_id` is globally unique across the repo and is used for `related_docs` cross-references and RAG citation. `validate_frontmatter.py` enforces uniqueness.

### controlled_terms and semantic drift prevention

Every `*-template.md` lists `controlled_terms` in its frontmatter — MTE vocabulary terms used in that document. `check_term_consistency.py` enforces that each term matches a `## Term Name` heading in `GLOSSARY.md` (canonical form, not an alias). This is the primary guard against LLM semantic drift when the KB is used for Agentic RAG document generation.

### RAG chunking hints

The `rag_chunk_strategy` frontmatter field tells the downstream RAG ingestion pipeline how to chunk each document:
- `by-section` — split at `##` headings (default for narrative docs)
- `by-table` — split at table boundaries (matrix/tracker docs)
- `monolithic` — do not split (short docs < ~500 words)
- `split-h2` — same as `by-section`; explicit alias

### Shared content

- `shared/_snippets/` — standalone RAG-indexed content blocks with full frontmatter (phase: `Universal`)
- `shared/_partials/` — structural boilerplate fragments (not independently RAG-indexed; no frontmatter validation enforced)

### Version management

KB version lives in `pyproject.toml` `[project].version`. `bump_version.py` updates it and rotates `CHANGELOG.md` (`[Unreleased]` → `[X.Y.Z] — date`). The `.github/workflows/release.yml` workflow fires on `v*` tags and creates a GitHub Release with the matching CHANGELOG section and live KB stats.

### Schema enums to know

When editing `_index.yaml` or frontmatter, the constrained enums are:

| Field | Allowed values |
|-------|---------------|
| `phase` | `P1`, `EVT`, `DVT`, `PVT`, `MP`, `Universal` |
| `checkpoint` | `CP1`–`CP6`, `Universal` |
| `doc_type` | `plan`, `spec`, `report`, `checklist`, `tracker`, `matrix`, `log`, `analysis`, `procedure`, `playbook` |
| `status` | `template-stub`, `draft`, `in-review`, `approved`, `superseded`, `archived` |
| `rag_chunk_strategy` | `by-section`, `by-table`, `monolithic`, `split-h2` |
| `embedding_priority` | `high`, `medium`, `low`, `exclude` |
| `owner_role` | `MTE Lead`, `MTE Staff`, `MTE Manager`, `NPI PM`, `Quality Engineer`, `Factory Ops` |
| `test_stations` | `ICT`, `FCT`, `DIAG`, `BURN-IN`, `ATE`, `SYSTEM`, `OBA`, `SFC`, `Universal` |
| `product_families` | `GPU`, `DC-L6`, `Automotive`, `Embedded`, `Universal` |
| `production_stages` | `SMT`, `FATP`, `PACK`, `All` |
| `priority` | `critical`, `required`, `recommended`, `optional` (lifecycle templates only; not required for Universal/snippets) |

The `production_stages` field is derived from `test_stations` by `bootstrap_templates.py` (`ICT`→`SMT`, `FCT/DIAG/BURN-IN/ATE/SYSTEM`→`FATP`, `OBA`→`PACK`, `SFC/Universal`→`All`).

### i18n

**Design principle:** English Markdown is the single ground truth. Translations live in `i18n/` YAML files only — never in template frontmatter or `_index.yaml`.

| File | Purpose |
|------|---------|
| `i18n/doc_titles.yaml` | Localized document titles for all 140 `doc_id`s (135 lifecycle + 5 snippets) |
| `i18n/section_titles.yaml` | Localized headings for ~8 universal structural sections (Purpose and Scope, Revision History, etc.); document-specific headings are translated dynamically by the RAG agent at generation time |
| `i18n/README.md` | Usage instructions and RAG agent integration example |

**Multilingual canonical forms in GLOSSARY.md:** Each of the 65 terms has three additional lines after `**Canonical Form:** \`X\``:
```
**Canonical Form (zh-CN):** `简体中文`
**Canonical Form (zh-TW):** `繁體中文`
**Canonical Form (vi):** *(pending)*
```

`check_term_consistency.py` parses all `**Canonical Form (...)**` lines (English + multilingual) and registers them as valid canonical terms. This allows templates to reference Chinese terms in `controlled_terms` when generating localized documents.

Supported languages: `zh-CN` (深圳), `zh-TW` (台湾), `vi` (stub — pending).

### Inference architecture reference

`docs/agentic-rag-inference.md` documents the recommended on-premise LLM stack for the document generation agent: SGLang + PD separation + Radix Attention + xGrammar structured output. GLOSSARY.md is designed as a shared system prompt prefix that benefits from Radix Attention KV cache reuse across a generation batch.
