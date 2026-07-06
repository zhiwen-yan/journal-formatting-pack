# Journal Formatting Skill Pack

Codex skills for preparing academic manuscripts for journal submission.

## Skills

- `journal-formatting`: router and universal entry point.
- `frontiers-formatting`: Frontiers journals.
- `mdpi-formatting`: MDPI journals.
- `wiley-formatting`: Wiley journals.
- `elsevier-formatting`: Elsevier and ScienceDirect journals.
- `springer-nature-formatting`: Springer Nature, BMC, and Nature Portfolio journals.
- `taylor-francis-formatting`: Taylor & Francis and Routledge journals.
- `sage-formatting`: SAGE journals.
- `oup-formatting`: Oxford University Press and Oxford Academic journals.
- `plos-formatting`: PLOS journals.
- `generic-journal-formatting`: fallback SCI/biomedical submission checklist.

## Install

Copy the skill folders into your Codex skills directory:

```powershell
Copy-Item -Path ".\*" -Destination "$HOME\.agents\skills" -Recurse -Force
```

The directory copied into `$HOME\.agents\skills` should contain each skill folder directly, for example:

```text
$HOME\.agents\skills\journal-formatting\SKILL.md
$HOME\.agents\skills\frontiers-formatting\SKILL.md
$HOME\.agents\skills\mdpi-formatting\SKILL.md
```

## Source Policy

Journal requirements change. These skills prefer the current official author guidelines URL, PDF, Word template, LaTeX template, or submission-system checklist provided by the user. Bundled references are source maps and first-pass checklists, not permanent replacements for journal instructions.

## Safety Rules

The skills must not invent DOI, PMID, PMCID, ethics approval numbers, trial registration numbers, funding awards, author details, corresponding author emails, ORCID IDs, data repository links, conflicts of interest, or other factual manuscript metadata.

Missing information should be marked with placeholders and sent back to the author for confirmation.
