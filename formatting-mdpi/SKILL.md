---
name: formatting-mdpi
description: MDPI journal formatting and submission-readiness assistant. Use when the user asks to format, check, revise, polish, or prepare manuscripts for MDPI journals such as Nutrients, Foods, IJERPH, Biomedicines, Healthcare, Journal of Clinical Medicine, Cancers, Molecules, or other MDPI titles. Check MDPI manuscript structure, section numbering, abstract, keywords, references, figures, tables, supplementary material, author contributions, funding, institutional review board statement, informed consent statement, data availability statement, acknowledgments, conflicts of interest, AI-use disclosure, and submission checklist. Also use this skill when the user wants a generated MDPI-style Word manuscript skeleton or LaTeX manuscript skeleton.
---

# MDPI Formatting

## Workflow

1. Confirm the exact MDPI journal, article type, and whether the user has the official MDPI Word or LaTeX template.
2. Read the current journal instructions page or the user's provided template. Use `references/official-guidelines.md` as a source map and initial checklist.
3. Check article-type-specific requirements before applying generic MDPI structure.
4. Preserve scientific content and do not invent missing declaration or citation details.
5. Return a checklist, revised structure, or submission sections as requested.

## File Outputs

When the user wants a deliverable manuscript file instead of only a checklist, use `scripts/generate_manuscript.py`.

Read `references/manuscript-generator.md` before running it.

The MDPI generator produces:

- `.docx` manuscript skeleton
- `.tex` manuscript skeleton

Both outputs include:

- title page
- abstract
- keywords
- body section skeleton
- declaration sections
- references placeholder

## Zotero Rules

If the user wants Zotero-aware references:

- Use a Zotero-exported `.bib` file through `--zotero-bib` or `ZOTERO_BIB_PATH`.
- If Zotero is not configured, do not create fake references.
- If Zotero is missing, let the generator print a setup prompt and keep the references section as a placeholder.

## Required Inputs

Ask for:

- Target MDPI journal.
- Article type.
- Manuscript file or text.
- Official journal instructions URL or template.
- Whether humans, animals, public data, AI tools, software/code, or supplementary materials are involved.
- Desired output format.

## Common MDPI Checks

Check:

- Title, authors, affiliations, and corresponding author block.
- Abstract and keywords.
- Numbered main sections when required by the template.
- Introduction, Materials and Methods, Results, Discussion, and Conclusions for standard original research unless the article type differs.
- Figure captions, table captions, in-text citations, and supplementary material citations.
- Reference numbering and reference list completeness.
- Author Contributions, Funding, Institutional Review Board Statement, Informed Consent Statement, Data Availability Statement, Acknowledgments, Conflicts of Interest, and AI-use disclosure when applicable.

## Output

Use this audit table:

| Area | Status | Issue | Fix |
|---|---|---|---|
| Template use | Pass/Revise/Missing |  |  |
| Abstract/keywords | Pass/Revise/Missing |  |  |
| Section structure | Pass/Revise/Missing |  |  |
| References | Pass/Revise/Missing |  |  |
| Figures/Tables | Pass/Revise/Missing |  |  |
| MDPI statements | Pass/Revise/Missing |  |  |
| Submission package | Pass/Revise/Missing |  |  |

## Guardrails

Do not create ethics approvals, consent statements, funding numbers, conflicts of interest, data links, DOI values, or author details from nothing. Draft only factual placeholders and ask the user to confirm.
