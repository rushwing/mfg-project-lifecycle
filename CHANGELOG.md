# Changelog

All notable changes to the MFG Lifecycle Knowledge Base are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version Numbering Convention

| Bump | When |
|------|------|
| **MAJOR** | Breaking changes to frontmatter schema (new required fields, renamed enums) that require migrating existing templates |
| **MINOR** | New phases, checkpoints, or template categories added; new GLOSSARY terms; new scripts |
| **PATCH** | Template content improvements, bug fixes in scripts, GLOSSARY definition updates, typo corrections |

---

## [Unreleased]

### Added
- (list changes not yet released)

---

## [0.1.0] — 2026-03-29

### Added
- Initial KB structure: 5 phases (P1, EVT, DVT, PVT, MP), 25 checkpoints, 131 template stubs
- `GLOSSARY.md` with 60+ canonical MTE term definitions for semantic drift prevention
- `schemas/template_frontmatter.schema.json` — frontmatter validation schema
- `schemas/checkpoint_index.schema.json` — checkpoint index validation schema
- `schemas/phase_manifest.schema.json` — phase manifest validation schema
- `scripts/bootstrap_templates.py` — idempotent stub generator from `_index.yaml`
- `scripts/validate_frontmatter.py` — CI frontmatter schema validation
- `scripts/check_term_consistency.py` — controlled_terms vs GLOSSARY check
- `scripts/validate_structure.py` — index–file consistency and cross-reference check
- `scripts/generate_doc_index.py` — auto-generates `DOC_INDEX.md`
- `scripts/bump_version.py` — KB version management utility
- `shared/_snippets/` — 5 standalone RAG-indexable content blocks
- `shared/_partials/` — 3 structural include fragments
- `.github/workflows/` — 4 CI pipelines (validate, check-terms, structure, doc-index)
- `pyproject.toml` + `uv.lock` — uv-managed Python dependencies
- `DOC_INDEX.md` — auto-generated full document registry

### Coverage
- Templates: 131 lifecycle + 5 snippets = 136 total
- GLOSSARY terms: 60+
- Lifecycle phases covered: P1 → EVT → DVT → PVT → MP
- Product families: GPU, DC-L6, Automotive, Embedded

[Unreleased]: https://github.com/OWNER/mfg-project-lifecycle/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/OWNER/mfg-project-lifecycle/releases/tag/v0.1.0
