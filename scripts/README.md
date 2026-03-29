# Scripts

Validation and tooling scripts for the MFG Lifecycle KB.

## Setup

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies from pyproject.toml
uv sync
```

## Scripts

| Script | Purpose | CI Trigger |
|--------|---------|-----------|
| `bootstrap_templates.py` | Generate template stubs from `_index.yaml` files | Manual |
| `validate_frontmatter.py` | Validate frontmatter against JSON Schema | PR |
| `check_term_consistency.py` | Check `controlled_terms` against `GLOSSARY.md` | PR |
| `validate_structure.py` | Check index–file consistency and cross-references | PR |
| `generate_doc_index.py` | Generate `DOC_INDEX.md` | Push to main |
| `bump_version.py` | Bump KB version in `pyproject.toml` + update `CHANGELOG.md` | Manual |

## Common Workflows

### Add a new template
1. Add document entry to the relevant `_index.yaml`
2. Run `uv run python scripts/bootstrap_templates.py` to generate the stub
3. Fill in the stub content
4. Run `uv run python scripts/validate_frontmatter.py` to verify

### Add a new controlled term
1. Add term definition to `GLOSSARY.md` following the standard format
2. Add term to `controlled_terms` in relevant template frontmatter
3. Run `uv run python scripts/check_term_consistency.py` to verify

### Regenerate DOC_INDEX.md
```bash
uv run python scripts/generate_doc_index.py
```

### Full validation
```bash
uv run python scripts/validate_frontmatter.py && \
uv run python scripts/check_term_consistency.py && \
uv run python scripts/validate_structure.py
```

### Release a new KB version
```bash
# Bump version (patch / minor / major)
uv run python scripts/bump_version.py minor

# Review and fill CHANGELOG.md [Unreleased] section, then:
git add pyproject.toml CHANGELOG.md
git commit -m "chore: release vX.Y.Z"
git tag vX.Y.Z
git push && git push --tags
```
