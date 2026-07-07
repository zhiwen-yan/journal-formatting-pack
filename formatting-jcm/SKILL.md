---
name: formatting-jcm
description: Shortcut formatting skill for MDPI Journal of Clinical Medicine submissions. Use when the user explicitly wants Journal of Clinical Medicine formatting, asks to prepare a manuscript for JCM, or wants a fast MDPI journal-specific entry point instead of the broader formatting-mdpi skill. Check manuscript structure, references, author contributions, funding, institutional review board statement, informed consent statement, data availability statement, conflicts of interest, and JCM-specific submission readiness. Also use this skill when the user wants a generated Word or LaTeX manuscript skeleton targeted to Journal of Clinical Medicine.
---

# formatting-jcm

## Purpose

Use this skill when the target journal is clearly `Journal of Clinical Medicine` or `JCM`. Treat it as a shortcut into the MDPI workflow with the target journal preselected.

Prefer the current JCM instructions page or the user's uploaded template over any bundled notes.

This skill should support minimal prompts plus a direct manuscript upload.

## Workflow

1. Confirm the article type for JCM.
2. Read the current JCM instructions page in `references/official-guidelines.md` or a newer user-provided guideline URL.
3. Apply the `formatting-mdpi` workflow and statement checks, but treat JCM-specific journal instructions as final when they differ from general MDPI patterns.
4. Output a checklist, revised structure, declaration text, or submission package material as requested.

## File Outputs

When the user wants a `.docx` or `.tex` manuscript skeleton, use `scripts/generate_manuscript.py`.

This wrapper preselects:

- style: `mdpi`
- journal: `Journal of Clinical Medicine`

If the user wants Zotero-aware references and no Zotero `.bib` source is configured, stop and prompt for configuration or leave a references placeholder.

## Required Inputs

Ask for or infer:

- Article type.
- Manuscript file or text.
- JCM instructions URL or template, only if already available or needed for stricter template matching.
- Whether humans, animals, public data, AI tools, or supplementary materials are involved.
- Desired output.

## Checks

Check by default:

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
