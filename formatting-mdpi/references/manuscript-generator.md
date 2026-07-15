# MDPI Structural Manuscript Generator

Use `scripts/generate_manuscript.py` only when the user wants a new Word or LaTeX structural draft from JSON.

Do not use it to reformat an existing manuscript. It creates a new package and cannot preserve the original document's figures, tables, equations, citation fields, comments, tracked changes, notes, hyperlinks, or relationships.

## Output Status

Label generated files `unofficial structural draft`. The generator applies local journal rules but does not download, convert, or apply the official publisher template.

For strict Word output, generate the draft only as an intermediate artifact, migrate it into the verified official template, run package QA, and inspect every rendered page.

The LaTeX generator uses a generic `article` class and is not an official MDPI LaTeX package.

## Example Commands

Generate a Metabolites Word structural draft:

```powershell
& "<python>" "scripts/generate_manuscript.py" --input "..\formatting-journal\references\example-manuscript.json" --journal "Metabolites" --article-type "Article" --output-format word --output "output\metabolites-structural-draft.docx"
```

Generate a LaTeX structural draft:

```powershell
& "<python>" "scripts/generate_manuscript.py" --input "..\formatting-journal\references\example-manuscript.json" --journal "Metabolites" --output-format latex --output "output\metabolites-structural-draft.tex"
```

An explicit `--rules` path must exist. The generator stops instead of silently ignoring a missing profile.
When no inferred profile matches, the command emits a warning before using generic structural defaults. A journal profile may also block article types that require a separate official template.

## Local Rule Behavior

Known rule profiles can control:

- default article sections
- structured-abstract placeholder labels
- keyword minimum and separator
- reference-style label
- fallback page and font settings
- section and line numbering
- declaration order

Template-derived styles remain authoritative.

## Zotero

LaTeX output can reference a Zotero-exported `.bib` file.

Word output does not format or insert a Zotero bibliography from `.bib`. It only leaves a reminder and placeholder. Preserve existing Zotero or EndNote Word fields when reformatting an existing DOCX.

Never invent bibliography content when Zotero is absent.
