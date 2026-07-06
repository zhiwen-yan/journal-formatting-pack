# Journal Formatting Skill Pack

Codex skills for preparing academic manuscripts for journal submission.

This repository packages a publisher-aware journal formatting workflow for academic writing. The main entry skill routes requests to publisher-specific skills, then checks structure, declarations, references, figures, tables, and submission readiness against current journal instructions.

## Included Skills

- `formatting-journal`: universal entry point and router.
- `formatting-frontiers`: Frontiers journals.
- `formatting-mdpi`: MDPI journals.
- `formatting-wiley`: Wiley journals.
- `formatting-elsevier`: Elsevier and ScienceDirect journals.
- `formatting-springer-nature`: Springer Nature, BMC, and Nature Portfolio journals.
- `formatting-taylor-francis`: Taylor & Francis and Routledge journals.
- `formatting-sage`: SAGE journals.
- `formatting-oup`: Oxford University Press and Oxford Academic journals.
- `formatting-plos`: PLOS journals.
- `formatting-generic`: fallback SCI and biomedical submission checklist.
- `formatting-nutrients`: direct shortcut for MDPI Nutrients.
- `formatting-foods`: direct shortcut for MDPI Foods.
- `formatting-jcm`: direct shortcut for MDPI Journal of Clinical Medicine.

## Repository Layout

```text
journal-formatting-pack/
├── formatting-journal/
├── formatting-frontiers/
├── formatting-mdpi/
├── formatting-wiley/
├── formatting-elsevier/
├── formatting-springer-nature/
├── formatting-taylor-francis/
├── formatting-sage/
├── formatting-oup/
├── formatting-plos/
├── formatting-generic/
├── formatting-nutrients/
├── formatting-foods/
└── formatting-jcm/
```

Each skill contains:

- `SKILL.md`: trigger description and operating instructions.
- `agents/openai.yaml`: UI metadata for Codex skill chips.
- `references/`: official source map and checklists to consult during execution.

## Install

Copy the skill folders into your Codex skills directory:

```powershell
Copy-Item -Path ".\*" -Destination "$HOME\.agents\skills" -Recurse -Force
```

After installation, the paths should look like:

```text
$HOME\.agents\skills\formatting-journal\SKILL.md
$HOME\.agents\skills\formatting-frontiers\SKILL.md
$HOME\.agents\skills\formatting-mdpi\SKILL.md
```

You can verify the install with:

```powershell
Get-ChildItem "$HOME\.agents\skills" -Recurse -Filter "SKILL.md" | Select-Object FullName
```

## How To Use

Call the universal router when you want the skill to choose the publisher path:

```text
Use formatting-journal to prepare this manuscript for Frontiers in Pharmacology as an Original Research article. First list missing information, then produce a submission-readiness checklist.
```

Call a publisher-specific skill when you already know the target family:

```text
Use formatting-mdpi for Nutrients. Check manuscript structure, references, declaration sections, and any missing submission statements.
```

Or jump straight to a frequent journal shortcut:

```text
Use formatting-nutrients to prepare this manuscript for Nutrients.
```

## Expected Inputs

These skills work best when the user provides:

- target journal name
- publisher, if known
- article type
- official author guidelines URL, PDF, Word template, or LaTeX template
- manuscript file or manuscript text
- reference style, if known
- study design details such as human, animal, trial, review, or public-data status

## Supported Outputs

- submission-readiness checklist
- formatting audit table
- revised manuscript structure
- declaration sections
- title page
- cover letter
- response letter
- reference-style cleanup
- `.docx` manuscript skeleton generation
- `.tex` manuscript skeleton generation

## Generator Support

The pack includes executable manuscript generators in:

- `formatting-journal/scripts/generate_manuscript.py`
- `formatting-mdpi/scripts/generate_manuscript.py`
- `formatting-nutrients/scripts/generate_manuscript.py`
- `formatting-foods/scripts/generate_manuscript.py`
- `formatting-jcm/scripts/generate_manuscript.py`

These generators can create:

- Word manuscript skeletons
- LaTeX manuscript skeletons

Each generated file can include:

- title page
- abstract
- keywords
- body structure
- declaration sections
- references placeholder

## Zotero Support

The generators do not require a live Zotero connector. They support Zotero through an exported `.bib` file.

Supported configuration:

- `--zotero-bib "C:\path\to\library.bib"`
- `ZOTERO_BIB_PATH=C:\path\to\library.bib`

Behavior:

- If Zotero is configured, LaTeX output inserts bibliography commands.
- If Zotero is configured, Word output inserts a reminder to refresh the bibliography in Zotero for Word.
- If Zotero is not configured, the generators print a prompt and leave a references placeholder.

## Source Policy

Journal requirements change. These skills prefer the current official author guidelines URL, PDF, Word template, LaTeX template, or submission-system checklist provided by the user. Bundled references are source maps and first-pass checklists, not permanent replacements for journal instructions.

## Safety Rules

The skills must not invent DOI, PMID, PMCID, ethics approval numbers, trial registration numbers, funding awards, author details, corresponding author emails, ORCID IDs, data repository links, conflicts of interest, or other factual manuscript metadata.

Missing information should be marked with placeholders and sent back to the author for confirmation.

## Maintenance Notes

- Official source URLs were checked during initial pack creation, but live journal instructions should always win.
- Some publisher sites use anti-bot protection. If a page blocks automation, supply the current guideline URL or upload the PDF or template directly when using the skill.
