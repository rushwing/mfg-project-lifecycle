# Contributing to MFG Lifecycle KB

## Overview

This KB stores manufacturing test document templates for NVIDIA GPU, DC-L6, Automotive, and Embedded products. Templates feed an Agentic RAG pipeline for automated document generation.

## Quick Start

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies
uv sync

# Generate any missing template stubs
uv run python scripts/bootstrap_templates.py

# Validate your changes
uv run python scripts/validate_frontmatter.py
uv run python scripts/check_term_consistency.py
uv run python scripts/validate_structure.py
```

---

## Adding a New Template

### Step 1 — Update `_index.yaml`

Find the correct checkpoint directory and add an entry to its `_index.yaml`:

```yaml
documents:
  - doc_id: "EVT-CP2-XYZ-006"       # Must be globally unique
    title: "My New Template"
    slug: "my-new-template"          # Must match filename (minus -template.md)
    doc_type: "plan"                 # See schema for allowed values
    owner_role: "MTE Lead"
    priority: "required"
    product_families: ["GPU", "DC-L6"]
    test_stations: ["FCT"]
    rag_chunk_strategy: "by-section"
    embedding_priority: "medium"
    controlled_terms: ["FCT", "False Fail"]
    required_sections:
      - "1. Purpose and Scope"
      - "2. Test Procedure"
      - "3. Revision History"
```

### Step 2 — Generate the stub

```bash
python scripts/bootstrap_templates.py
```

This creates `{checkpoint-dir}/my-new-template-template.md` with frontmatter pre-filled from `_index.yaml`.

### Step 3 — Fill the template

Edit the generated stub. Keep all frontmatter fields. Fill each `## Section` with actual content.

### Step 4 — Validate

```bash
python scripts/validate_frontmatter.py
python scripts/check_term_consistency.py
```

---

## Frontmatter Requirements

Every `*-template.md` file must have valid YAML frontmatter. Required fields:

| Field | Type | Notes |
|-------|------|-------|
| `doc_id` | string | Format: `{PHASE}-CP{N}-{SHORT}-{SEQ3}`. Globally unique. |
| `title` | string | Human-readable English title |
| `slug` | string | Lowercase, hyphenated. Must match filename. |
| `version` | string | SemVer. `0.x.x` = stub/draft, `1.x.x` = ratified. |
| `phase` | enum | `P1` \| `EVT` \| `DVT` \| `PVT` \| `MP` |
| `checkpoint` | enum | `CP1`–`CP6` |
| `checkpoint_name` | string | Human-readable checkpoint name |
| `doc_type` | enum | `plan`, `spec`, `report`, `checklist`, `tracker`, `matrix`, `log`, `analysis`, `procedure`, `playbook` |
| `product_families` | array | One or more of: `GPU`, `DC-L6`, `Automotive`, `Embedded`, `Universal` |
| `test_stations` | array | One or more of: `ICT`, `FCT`, `DIAG`, `BURN-IN`, `ATE`, `SYSTEM`, `OBA`, `SFC`, `Universal` |
| `owner_role` | enum | `MTE Lead`, `MTE Staff`, `MTE Manager`, `NPI PM`, `Quality Engineer`, `Factory Ops` |
| `status` | enum | `template-stub`, `draft`, `in-review`, `approved`, `superseded`, `archived` |
| `created_date` | date | ISO 8601 or `YYYY-MM-DD` placeholder |
| `last_updated` | date | ISO 8601 |
| `rag_chunk_strategy` | enum | `by-section` (default), `by-table`, `monolithic`, `split-h2` |
| `embedding_priority` | enum | `high`, `medium`, `low`, `exclude` |
| `controlled_terms` | array | Terms from this doc that must exist in `GLOSSARY.md` |
| `required_sections` | array | Section headings (used by bootstrap script) |

---

## Controlled Terms Policy

`controlled_terms` in frontmatter must use **canonical forms** as defined in `GLOSSARY.md`.

```yaml
# CORRECT — uses canonical form
controlled_terms:
  - "Test Escape"
  - "False Fail"
  - "GR&R"

# WRONG — uses aliases
controlled_terms:
  - "Escape"         # alias → use "Test Escape"
  - "False Reject"   # alias → use "False Fail"
  - "Gauge R&R"      # alias → use "GR&R"
```

To add a new controlled term:
1. Add a `## Term Name` entry to `GLOSSARY.md` with all required fields
2. Then reference it in template frontmatter

---

## `doc_id` Convention

Format: `{PHASE}-CP{N}-{DOC_SHORT}-{SEQ}`

| Segment | Rules |
|---------|-------|
| `PHASE` | `P1`, `EVT`, `DVT`, `PVT`, `MP` |
| `CP{N}` | `CP1`–`CP6` (scoped to phase) |
| `DOC_SHORT` | 2–5 uppercase letters/numbers abbreviating the document type |
| `SEQ` | 3-digit zero-padded sequence within the checkpoint |

Examples: `EVT-CP2-TRP-001`, `DVT-CP5-CAPA-003`, `P1-CP3-ERS-002`

IDs must be globally unique across the entire repository.

---

## RAG Chunking Strategy

Choose `rag_chunk_strategy` based on document structure:

| Strategy | Use When |
|----------|---------|
| `by-section` | Narrative docs with `##` section headings |
| `by-table` | Matrix/report docs where tables are the primary content |
| `monolithic` | Short docs (< 500 words) that lose meaning when split |
| `split-h2` | Long docs where `##` sections are independently meaningful |

---

## PR Checklist

Before submitting a PR:
- [ ] `validate_frontmatter.py` passes with 0 errors
- [ ] `check_term_consistency.py` passes with 0 errors
- [ ] `validate_structure.py` passes with 0 errors (or explains expected missing stubs)
- [ ] New terms added to `GLOSSARY.md` before use in `controlled_terms`
- [ ] `doc_id` follows naming convention and is unique
- [ ] `required_sections` reflects actual document section structure
