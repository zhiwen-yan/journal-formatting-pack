# Manuscript Generator

Use `scripts/generate_manuscript.py` when the user wants a real output file instead of only a checklist.

## Supported Outputs

- Word manuscript skeleton: `.docx`
- LaTeX manuscript skeleton: `.tex`

Both formats include:

- title page
- abstract
- keywords
- main sections
- declarations
- references placeholder

## Input Format

Pass a JSON file with fields like:

- `journal`
- `article_type`
- `title`
- `running_title`
- `reference_style`
- `authors`
- `affiliations`
- `abstract`
- `keywords`
- `sections`
- `declarations`

See `references/example-manuscript.json` for a working example.

## Example Commands

Generate a Word manuscript skeleton:

```powershell
& "<python>" "scripts/generate_manuscript.py" --input "references/example-manuscript.json" --output-format word --output "output\manuscript.docx"
```

Generate a LaTeX manuscript skeleton:

```powershell
& "<python>" "scripts/generate_manuscript.py" --input "references/example-manuscript.json" --output-format latex --output "output\manuscript.tex"
```

## Zotero Handling

The generator does not depend on a live Zotero connector. Instead, it can consume a Zotero-exported `.bib` file.

Supported configuration paths:

1. `--zotero-bib "C:\path\to\library.bib"`
2. `ZOTERO_BIB_PATH=C:\path\to\library.bib`

Behavior:

- If configured, the LaTeX output inserts `\addbibresource{...}` and `\printbibliography`.
- If configured, the Word output adds a note reminding the user to refresh the bibliography through Zotero in Word.
- If not configured, the generator leaves a clear references placeholder.
- If the caller sets `--zotero-mode required` without a valid `.bib` path, the script stops and prints a prompt telling the user how to configure Zotero.

## Guardrails

- Do not fabricate bibliography entries.
- Do not assume Zotero is available just because the user mentions it.
- When Zotero is absent, keep the references section as a placeholder and prompt for configuration.
