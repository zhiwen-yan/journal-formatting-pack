# Journal Formatting Skill Pack

Codex skills for preparing academic manuscripts for journal submission.

This repository packages a publisher-aware journal formatting workflow for academic writing. The main entry skill routes requests to publisher-specific skills, then checks structure, declarations, references, figures, tables, and submission readiness against current journal instructions.

## Included Skills

- `journal-formatting`: universal entry point and router.
- `frontiers-formatting`: Frontiers journals.
- `mdpi-formatting`: MDPI journals.
- `wiley-formatting`: Wiley journals.
- `elsevier-formatting`: Elsevier and ScienceDirect journals.
- `springer-nature-formatting`: Springer Nature, BMC, and Nature Portfolio journals.
- `taylor-francis-formatting`: Taylor & Francis and Routledge journals.
- `sage-formatting`: SAGE journals.
- `oup-formatting`: Oxford University Press and Oxford Academic journals.
- `plos-formatting`: PLOS journals.
- `generic-journal-formatting`: fallback SCI and biomedical submission checklist.

## Repository Layout

```text
journal-formatting-pack/
├── journal-formatting/
├── frontiers-formatting/
├── mdpi-formatting/
├── wiley-formatting/
├── elsevier-formatting/
├── springer-nature-formatting/
├── taylor-francis-formatting/
├── sage-formatting/
├── oup-formatting/
├── plos-formatting/
└── generic-journal-formatting/
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
$HOME\.agents\skills\journal-formatting\SKILL.md
$HOME\.agents\skills\frontiers-formatting\SKILL.md
$HOME\.agents\skills\mdpi-formatting\SKILL.md
```

You can verify the install with:

```powershell
Get-ChildItem "$HOME\.agents\skills" -Recurse -Filter "SKILL.md" | Select-Object FullName
```

## How To Use

Call the universal router when you want the skill to choose the publisher path:

```text
Use journal-formatting to prepare this manuscript for Frontiers in Pharmacology as an Original Research article. First list missing information, then produce a submission-readiness checklist.
```

Call a publisher-specific skill when you already know the target family:

```text
Use mdpi-formatting for Nutrients. Check manuscript structure, references, declaration sections, and any missing submission statements.
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

## Source Policy

Journal requirements change. These skills prefer the current official author guidelines URL, PDF, Word template, LaTeX template, or submission-system checklist provided by the user. Bundled references are source maps and first-pass checklists, not permanent replacements for journal instructions.

## Safety Rules

The skills must not invent DOI, PMID, PMCID, ethics approval numbers, trial registration numbers, funding awards, author details, corresponding author emails, ORCID IDs, data repository links, conflicts of interest, or other factual manuscript metadata.

Missing information should be marked with placeholders and sent back to the author for confirmation.

## Maintenance Notes

- Official source URLs were checked during initial pack creation, but live journal instructions should always win.
- Some publisher sites use anti-bot protection. If a page blocks automation, supply the current guideline URL or upload the PDF or template directly when using the skill.
