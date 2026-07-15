---
name: formatting-metabolites
description: Format, audit, or prepare manuscripts for the MDPI journal Metabolites. Use when the user names Metabolites, requests a Metabolites-ready DOCX or LaTeX draft, wants an existing manuscript migrated into the current official Metabolites template, or needs checks for its structured abstract, keywords, author markers, declarations, figures, tables, numeric ACS-style references, cover letter, and submission readiness.
---

# formatting-metabolites

## Source Order

1. Read `references/official-guidelines.md`.
2. Verify the live Metabolites instructions and the template for the requested article type.
3. Apply the shared `formatting-mdpi` workflow. For an existing DOCX, also read `../formatting-mdpi/references/docx-reformatting.md`.
4. Treat the current official journal template as authoritative when it conflicts with local fallback values.

## Choose The Workflow

- For an audit, inspect the manuscript and return findings without changing the file.
- For an existing DOCX, use the official-template migration and render-based QA workflow.
- For a new structural draft, use `scripts/generate_manuscript.py` and label the result an unofficial structural draft unless it was subsequently migrated into the verified official template.

Do not pass an existing manuscript through the skeleton generator. It cannot preserve figures, tables, equations, citation fields, comments, tracked changes, or package relationships.

Label a read-only result `audit-only—not submission-ready`. Render the source when visual layout is in scope; package and content-only audits may remain non-rendering and must say so.

## Metabolites Checks

Check at least:

- exact article type and matching Article, Protocol, or Data Descriptor template
- approximately 250-word structured abstract when applicable, with `Background/Objectives`, `Methods`, `Results`, and `Conclusions`
- 3–10 semicolon-separated keywords
- complete author–affiliation mapping, all correspondence details, `*` correspondence markers, and `†` equal-contribution markers
- numbered research sections; allow combined Results and Discussion and optional Conclusions when the article type permits
- figures near first citation, captions below, preferred 600 dpi, preserved aspect ratio, alt text, and no synthetic upscaling
- editable Word tables, captions above, repeat header rows, printable-width fit, and at least 8 pt table text
- numeric citations in first-appearance order using square brackets before punctuation
- ACS-style MDPI references with full titles and verified ISO 4 journal abbreviations
- CRediT Author Contributions, Funding, conditional ethics and consent, mandatory Data Availability, optional Acknowledgments, and Conflicts of Interest
- generative-AI disclosure in Methods only when the current policy requires it
- cover letter and any relevant reporting checklist

## Missing Facts

Use visible author-query placeholders for facts the manuscript does not provide. Never invent affiliation details, emails, CRediT roles, funder or grant data, ethics committee names, protocol codes, approval dates, consent status, repository links, conflicts, DOI values, or reference metadata.

Do not mark a file submission-ready while author queries remain unresolved.

## File Generation

Use `scripts/generate_manuscript.py` only for a new `.docx` or `.tex` structural draft. The wrapper preselects:

- style: `mdpi`
- journal: `Metabolites`
- article type: `Article`, unless overridden

The generator consumes `../rules/mdpi/metabolites.json`. It does not download or apply the official template and must not be presented as strict template output.

Protocol and Data Descriptor skeleton generation is intentionally blocked because those article types use separate live templates and are not safely represented by the generic IMRaD generator. Use the exact official template workflow for them.

## Acceptance Gate

Before delivering a modified DOCX:

1. Save and reopen it successfully.
2. Run `../formatting-mdpi/scripts/qa_docx.py` with the Metabolites rule profile and, for format-only work, the original source file.
3. Render every page and inspect the full-resolution output.
4. Confirm no clipping, blank pages, stretched figures, split captions, broken tables, missing objects, unresolved placeholders, or template sample text.
5. Deliver the formatted manuscript with an audit, author-query list, change log, and template provenance record.

## Guardrails

- Keep format-only work format-only. Do not silently rewrite scientific claims, methods, results, sample counts, dates, or references.
- Record every requested or necessary content correction separately for author approval.
- Preserve Zotero/EndNote fields, equations, hyperlinks, comments, tracked changes, and custom XML unless a tested transformation explicitly remaps them.
- Do not hard-code manuscript-specific authors, table widths, figure filenames, or journal-abbreviation mappings into reusable code.
