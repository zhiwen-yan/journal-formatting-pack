---
name: formatting-frontiers
description: Frontiers journal formatting and submission-readiness assistant. Use when the user asks to format, check, revise, polish, or prepare manuscripts for Frontiers journals such as Frontiers in Pharmacology, Frontiers in Nutrition, Frontiers in Public Health, Frontiers in Medicine, Frontiers in Endocrinology, Frontiers in Immunology, or other Frontiers titles. Check article type, abstract, keywords, manuscript structure, references, figures, tables, supplementary material, ethics, consent, data availability, author contributions, funding, conflicts of interest, AI-use disclosure, and submission checklist.
---

# formatting-frontiers

## Workflow

1. Confirm the exact Frontiers journal and article type.
2. Read the current official Frontiers author guidelines or the user's provided URL/template. Use `references/official-guidelines.md` only as a first-pass source map.
3. Check whether the selected article type has journal-specific limits for abstract, word count, display items, references, or supplementary material.
4. Format or audit the manuscript without inventing missing author, ethics, funding, registration, DOI, PMID, or repository details.
5. Output a checklist plus the requested manuscript sections.

## Required Inputs

Ask for missing items that affect formatting:

- Target Frontiers journal.
- Article type.
- Manuscript text or file.
- Official author guidelines URL or article-type page, if available.
- Whether the study involves humans, animals, public data, clinical trial data, AI tools, or supplementary material.
- Requested output: checklist, revised manuscript, title page, declarations, cover letter, response letter, or full package.

## Checks

Check these Frontiers-sensitive items:

- Title is concise and avoids unnecessary abbreviations.
- Abstract matches the article type and contains no unsupported citations, figures, or tables unless the current guidelines allow them.
- Keywords meet the current journal/article-type requirement.
- Main text headings match the article type.
- Figures and tables are cited in order.
- Figure legends and table titles are complete and separable from the main text if the template requires it.
- Supplementary material is cited and named consistently.
- References and in-text citations follow the current Frontiers style.
- Data availability, ethics, consent, author contributions, funding, conflicts of interest, acknowledgments, and AI-use disclosure are present when required.

## Output

Use this compact audit table unless the user requests a full rewrite:

| Area | Status | Issue | Fix |
|---|---|---|---|
| Article type | Pass/Revise/Missing |  |  |
| Abstract | Pass/Revise/Missing |  |  |
| Keywords | Pass/Revise/Missing |  |  |
| Structure | Pass/Revise/Missing |  |  |
| References | Pass/Revise/Missing |  |  |
| Figures/Tables | Pass/Revise/Missing |  |  |
| Declarations | Pass/Revise/Missing |  |  |
| Submission package | Pass/Revise/Missing |  |  |

## Guardrails

Do not invent ethics approval numbers, trial registration numbers, funding awards, DOI/PMID values, author affiliations, corresponding author emails, ORCID IDs, or data repository links. Use placeholders and ask the user to verify.
