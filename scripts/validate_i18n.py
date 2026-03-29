#!/usr/bin/env python3
"""
validate_i18n.py

Validates i18n/ translation data:
1. YAML files parse without error
2. doc_titles.yaml covers every doc_id declared in _index.yaml files and
   shared/_snippets/*.md frontmatter (no missing, no stale entries)
3. doc_titles.yaml "en" values match the canonical English title in the
   source of truth (_index.yaml or snippet frontmatter) — catches renames
   in _index.yaml that were not reflected in the translation table
4. doc_titles.yaml entries have all required locale keys (zh-CN, zh-TW)
5. section_titles.yaml entries have all required locale keys (zh-CN, zh-TW)

Required locales: zh-CN, zh-TW (vi is a declared stub and not enforced)

Usage:
    cd <repo_root>
    python scripts/validate_i18n.py

Exit codes:
    0 — All checks passed
    1 — One or more errors found
"""

import sys
from pathlib import Path

import frontmatter
import yaml

try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
I18N_DIR = ROOT / "i18n"
DOC_TITLES_PATH = I18N_DIR / "doc_titles.yaml"
SECTION_TITLES_PATH = I18N_DIR / "section_titles.yaml"
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def load_yaml(path: Path) -> tuple[dict | None, str | None]:
    """Load and parse a YAML file. Returns (data, error_message)."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        return data, None
    except yaml.YAMLError as e:
        return None, str(e)


def collect_all_doc_metadata() -> dict[str, str]:
    """Return {doc_id: en_title} for every document in _index.yaml files and snippets.

    The English title is the canonical ground truth; doc_titles.yaml["en"]
    must match it exactly.
    """
    docs: dict[str, str] = {}

    # Lifecycle docs from _index.yaml
    for index_file in sorted(ROOT.rglob("_index.yaml")):
        try:
            data = yaml.safe_load(index_file.read_text(encoding="utf-8"))
            for doc in data.get("documents", []):
                doc_id = doc.get("doc_id")
                title = doc.get("title", "")
                if doc_id:
                    docs[doc_id] = title
        except Exception as e:
            log(f"[yellow]WARN[/yellow] Could not parse {index_file.relative_to(ROOT)}: {e}")

    # Shared snippet docs from frontmatter
    snippets_dir = ROOT / "shared" / "_snippets"
    if snippets_dir.exists():
        for f in sorted(snippets_dir.glob("*.md")):
            try:
                post = frontmatter.load(str(f))
                doc_id = post.metadata.get("doc_id")
                title = post.metadata.get("title", "")
                if doc_id:
                    docs[doc_id] = title
            except Exception as e:
                log(f"[yellow]WARN[/yellow] Could not parse {f.relative_to(ROOT)}: {e}")

    return docs


def main() -> None:
    errors: list[str] = []

    log("\n[bold]i18n Validator[/bold]")

    # ── 1. YAML parse checks ──────────────────────────────────────────────────

    for path in (DOC_TITLES_PATH, SECTION_TITLES_PATH):
        if not path.exists():
            errors.append(f"Missing file: {path.relative_to(ROOT)}")
            continue
        data, err = load_yaml(path)
        if err:
            errors.append(f"{path.relative_to(ROOT)}: YAML parse error — {err}")
        elif not isinstance(data, dict):
            errors.append(f"{path.relative_to(ROOT)}: expected a YAML mapping at top level")

    if any("YAML parse error" in e or "Missing file" in e for e in errors):
        # Can't proceed with content checks if files are broken
        for e in errors:
            log(f"[red]✗[/red] {e}")
        log("\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)

    doc_titles, _ = load_yaml(DOC_TITLES_PATH)
    section_titles, _ = load_yaml(SECTION_TITLES_PATH)

    log(f"doc_titles.yaml:     {len(doc_titles)} entries")
    log(f"section_titles.yaml: {len(section_titles)} entries")

    # Locales that must be present in every entry (vi is a declared stub, not enforced)
    REQUIRED_LOCALES = ["zh-CN", "zh-TW"]

    # ── 2. doc_titles.yaml coverage ──────────────────────────────────────────

    kb_docs = collect_all_doc_metadata()
    log(f"doc_ids in KB:       {len(kb_docs)}")

    missing_ids = [doc_id for doc_id in kb_docs if doc_id not in doc_titles]
    for doc_id in sorted(missing_ids):
        errors.append(f"doc_titles.yaml: missing entry for doc_id '{doc_id}'")

    extra_ids = set(doc_titles.keys()) - set(kb_docs.keys())
    for doc_id in sorted(extra_ids):
        errors.append(f"doc_titles.yaml: stale entry '{doc_id}' (not in any _index.yaml or snippet)")

    # ── 3. doc_titles.yaml: "en" must match _index.yaml / snippet title ───────

    for doc_id, entry in doc_titles.items():
        if not isinstance(entry, dict):
            errors.append(f"doc_titles.yaml[{doc_id}]: expected a mapping, got {type(entry).__name__}")
            continue

        if "en" not in entry:
            errors.append(f"doc_titles.yaml[{doc_id}]: missing required 'en' key")
        elif doc_id in kb_docs:
            expected = kb_docs[doc_id]
            actual = entry["en"]
            if actual != expected:
                errors.append(
                    f"doc_titles.yaml[{doc_id}]: 'en' title mismatch — "
                    f"expected '{expected}' (from _index.yaml), got '{actual}'"
                )

        # ── 4. doc_titles.yaml: required locales must be present ─────────────
        for locale in REQUIRED_LOCALES:
            if locale not in entry:
                errors.append(f"doc_titles.yaml[{doc_id}]: missing required locale '{locale}'")
            elif not entry[locale]:
                errors.append(f"doc_titles.yaml[{doc_id}]: locale '{locale}' is empty")

    # ── 5. section_titles.yaml: required locales must be present ─────────────

    for heading, entry in section_titles.items():
        if not isinstance(entry, dict):
            errors.append(f"section_titles.yaml['{heading}']: expected a mapping, got {type(entry).__name__}")
            continue
        for locale in REQUIRED_LOCALES:
            if locale not in entry:
                errors.append(f"section_titles.yaml['{heading}']: missing required locale '{locale}'")
            elif not entry[locale]:
                errors.append(f"section_titles.yaml['{heading}']: locale '{locale}' is empty")

    # ── Report ────────────────────────────────────────────────────────────────

    log(f"\n{'=' * 60}")

    if errors:
        log(f"\n[bold red]ERRORS ({len(errors)}):[/bold red]\n")
        for e in errors:
            log(f"  [red]✗[/red] {e}")
        log(f"\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)
    else:
        log(f"\n[bold green]✓ All i18n checks passed.[/bold green]", "bold green")
        log(f"  doc_titles.yaml: {len(doc_titles)}/{len(kb_docs)} doc_ids covered, en titles match, zh-CN/zh-TW present")
        log(f"  section_titles.yaml: {len(section_titles)} headings — zh-CN/zh-TW present for all")
        log("\n[bold green]PASSED[/bold green]", "bold green")


if __name__ == "__main__":
    main()
