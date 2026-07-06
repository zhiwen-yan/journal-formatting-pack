---
name: formatting-nutrients
description: Shortcut formatting skill for MDPI Nutrients submissions. Use when the user explicitly wants Nutrients formatting, asks to prepare a manuscript for Nutrients, or wants a fast MDPI journal-specific entry point instead of the broader formatting-mdpi skill. Check manuscript structure, references, author contributions, funding, institutional review board statement, informed consent statement, data availability statement, conflicts of interest, and Nutrients-specific submission readiness.
---

# Nutrients Formatting

## Purpose

Use this skill when the target journal is clearly `Nutrients`. Treat it as a shortcut into the MDPI workflow with the target journal preselected.

Prefer the current Nutrients instructions page or the user's uploaded template over any bundled notes.

## Workflow

1. Confirm the article type for Nutrients.
2. Read the current Nutrients instructions page in `references/official-guidelines.md` or a newer user-provided guideline URL.
3. Apply the `formatting-mdpi` workflow and statement checks, but treat Nutrients-specific journal instructions as final when they differ from general MDPI patterns.
4. Output a checklist, revised structure, declaration text, or submission package material as requested.

## Required Inputs

Ask for:

- Article type.
- Manuscript file or text.
- Nutrients instructions URL or template, if available.
- Whether humans, animals, public data, AI tools, or supplementary materials are involved.
- Desired output.

## Checks

Check:

- Abstract and keywords.
- Main section structure for the selected article type.
- Reference numbering and formatting.
- Figure and table citations and captions.
- Author Contributions.
- Funding.
- Institutional Review Board Statement.
- Informed Consent Statement.
- Data Availability Statement.
- Conflicts of Interest.

## Guardrails

Do not invent missing declaration facts, study approvals, funding numbers, or reference metadata. Mark uncertain items as needing author confirmation.
