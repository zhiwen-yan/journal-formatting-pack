# MDPI Manuscript Generator

Use `scripts/generate_manuscript.py` when the user wants a Word or LaTeX manuscript skeleton for an MDPI journal.

## Output Types

- `.docx` manuscript skeleton
- `.tex` manuscript skeleton

The generator applies MDPI-friendly defaults for:

- article metadata
- numbered IMRaD-style structure
- declaration blocks
- references placeholder

## Example Commands

Generate a Word manuscript skeleton:

```powershell
& "<python>" "scripts/generate_manuscript.py" --input "..\formatting-journal\references\example-manuscript.json" --output-format word --output "output\mdpi-manuscript.docx"
```

Generate a LaTeX manuscript skeleton:

```powershell
& "<python>" "scripts/generate_manuscript.py" --input "..\formatting-journal\references\example-manuscript.json" --output-format latex --output "output\mdpi-manuscript.tex"
```

## Zotero

MDPI output follows the shared Zotero rules from `../formatting-journal/references/manuscript-generator.md`.

If Zotero is not configured, the generator should not invent bibliography content. It must prompt the user and leave a placeholder.
