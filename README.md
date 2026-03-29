# MFG Project Lifecycle — Manufacturing Test Engineering Knowledge Base

A structured repository of manufacturing test document templates for NVIDIA GPU, DC-L6, Automotive, and Embedded products. Designed as a knowledge base for Agentic RAG-based document auto-generation.

## Structure

```
P1 (Pre-NPI) → EVT → DVT → PVT → MP
```

| Phase | Checkpoints | Templates |
|-------|:-----------:|:---------:|
| P1 — Concept/Pre-NPI | 4 | 20 |
| EVT — Engineering Validation | 5 | 25 |
| DVT — Design Validation | 6 | 29 |
| PVT — Production Validation | 6 | 28 |
| MP — Mass Production | 6 | 29 |
| Shared Snippets | — | 5 |
| **Total** | **27** | **136** |

## Key Files

| File | Purpose |
|------|---------|
| `MFG_LIFECYCLE.md` | Phase/checkpoint mindmap — source of truth |
| `GLOSSARY.md` | 60+ canonical term definitions — semantic anchor for RAG |
| `DOC_INDEX.md` | Auto-generated document registry (all templates) |
| `CONTRIBUTING.md` | How to add/edit templates |
| `schemas/` | JSON Schema for frontmatter and index validation |
| `scripts/` | Validation, bootstrap, and indexing tools |

## Quick Start

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies
uv sync

# Generate any missing template stubs
uv run python scripts/bootstrap_templates.py

# Validate everything
uv run python scripts/validate_frontmatter.py
uv run python scripts/check_term_consistency.py
uv run python scripts/validate_structure.py

# Rebuild DOC_INDEX.md
uv run python scripts/generate_doc_index.py
```

## Template Frontmatter

Every `*-template.md` file carries structured YAML frontmatter:

```yaml
doc_id: "EVT-CP2-TRP-001"        # Globally unique ID
title: "Test Requirement Plan"
phase: "EVT"
checkpoint: "CP2"
doc_type: "plan"
product_families: [GPU, DC-L6, Automotive, Embedded]
status: "template-stub"
rag_chunk_strategy: "by-section"  # RAG pipeline chunking hint
controlled_terms: [TRP, DFT, "Test Escape"]  # Must match GLOSSARY.md
```

## CI/CD

Pull requests trigger:
1. **Frontmatter validation** — schema compliance, doc_id uniqueness
2. **Term consistency check** — all `controlled_terms` defined in GLOSSARY.md
3. **Structure validation** — index declarations match actual files

Push to main auto-regenerates `DOC_INDEX.md`.

## Design Decisions

- **Phase dir naming** (`p1-concept/`, `evt-engineering-validation/`...) ensures lexicographic lifecycle order in all tools
- **`_index.yaml`** is the source of truth; template stubs are generated from it (bootstrap is idempotent)
- **`GLOSSARY.md`** defines canonical forms for all controlled terms, preventing LLM semantic drift
- **`rag_chunk_strategy`** per-doc field drives the RAG ingestion pipeline chunking logic
- **`shared/_snippets/`** vs **`shared/_partials/`**: snippets are RAG-indexed independently; partials are structural boilerplate only

## License

See [LICENSE](LICENSE).
