---
name: formatting-mdpi
description: Audit, reformat, or prepare manuscripts for MDPI journals, including migration of an existing DOCX into the current official journal template and generation of an unofficial Word or LaTeX structural draft. Use when the user names MDPI or an MDPI journal, asks for journal-specific formatting, template matching, submission-readiness checks, references, figures, tables, declarations, cover letters, or a manuscript skeleton. Route Metabolites, Nutrients, Foods, and Journal of Clinical Medicine requests to their journal-specific rules when available.
---

# formatting-mdpi

## Start With The Exact Target

1. Confirm or infer the journal and article type before choosing a template.
2. Read `references/official-guidelines.md` and the current journal instructions.
3. Prefer a journal-specific skill and rule profile when one exists.
4. Preserve scientific content and record missing facts as author queries.

Do not require a long intake questionnaire. Ask only for information that changes the article type, template, ethics path, or requested deliverable.

## Choose One Mode

### Audit only

Inspect the manuscript and return findings without writing a replacement file.
Use status `audit-only—not submission-ready`. Run structural/package QA when the input is DOCX. Render the existing file when the user asks for visual-layout compliance or when layout defects are part of the audit; a purely structural/content audit does not require a new rendered artifact.

### Reformat an existing DOCX

Read `references/docx-reformatting.md` completely. Use the official template for the exact journal and article type. Preserve text and semantic objects, run package QA, and render every page before delivery.

Do not route an existing DOCX through the JSON skeleton generator. The generator does not preserve figures, editable tables, equations, citation fields, comments, tracked changes, hyperlinks, footnotes, or package relationships.

### Generate a new structural draft

Read `references/manuscript-generator.md`, then use `scripts/generate_manuscript.py`. Label the output an unofficial structural draft unless it is subsequently migrated into and verified against the official template.

## Template Policy

- Resolve the current template from the live journal instructions after selecting the article type.
- Record the final URL, retrieval time, article type, and SHA-256.
- Convert `.dot` or `.dotx` to `.docx` in a working directory before using `python-docx`.
- Verify expected MDPI styles, page settings, header/footer, and line numbering after conversion.
- Let template styles win over local fallback values.
- If the official template is unavailable, ask for an upload or proceed only in structure-only mode. Never claim strict MDPI matching from generic defaults.

## Existing-DOCX Guardrails

- Never overwrite the source file.
- Inventory text, sections, styles, images, tables, equations, hyperlinks, fields, notes, comments, tracked changes, and relationships before editing.
- Preserve Zotero and EndNote fields; do not flatten them.
- Keep equations editable and tables as Word tables.
- Maintain aspect ratio and use original high-resolution figure files when available; do not upscale low-resolution images.
- Keep format-only work format-only. List any content correction separately for author approval.

## Default MDPI Checks

Check the live journal rule for:

- title, author names, affiliation mapping, correspondence, ORCID, and equal-contribution notation
- abstract type, labels, word target, and keyword range
- article-type section order and numbering
- figure/table placement, captions, citations, resolution, permissions, and supplementary numbering
- citation–reference integrity, first-appearance order, numeric ranges, verified DOI/URL metadata, and journal abbreviations
- Author Contributions, Funding, ethics, consent, Data Availability, Acknowledgments, Conflicts of Interest, and policy-specific AI disclosure
- reporting guideline, trial or review registration, cover letter, graphical abstract, highlights, and supplementary files

Do not treat declarations as a flat mandatory list. Trigger ethics, consent, trial, animal, and AI statements from the study design and current journal policy.

## Missing Facts

Never invent DOI, PMID, PMCID, author details, affiliation addresses, correspondence emails, ORCID, CRediT roles, grant numbers, ethics committee names, approval codes or dates, consent status, registrations, repository links, conflicts, or reference metadata.

Use explicit author-query placeholders and block a “submission-ready” status until they are resolved.

## Acceptance Gate

For every modified DOCX:

1. Save and reopen the package successfully.
2. Run `scripts/qa_docx.py`; include `--source` for format-only migrations and `--rules` for a known journal profile.
3. Compare source/output text and semantic-object counts.
4. Render DOCX to PDF or page images and inspect every page at full resolution.
5. Fix blank pages, clipping, font substitution, broken tables, stretched figures, split captions, orphan headings, numbering problems, and header/footer issues.
6. Confirm that template sample text and unresolved placeholders are absent or documented.

## Deliverables

For a template migration, return:

- `formatted.docx`
- `formatting-audit.md`
- `author-queries.md`
- `change-log.md`
- `template-provenance.json`

Use this status language:

- `audit-only—not submission-ready`: read-only findings; no template migration was completed
- `template-matched and verified`: official template applied, package checks passed, and all pages inspected
- `template-matched with author queries`: layout verified but factual placeholders remain
- `structure-only draft`: official template was not applied or verified

## Output Table

| Area | Status | Evidence | Required action |
|---|---|---|---|
| Template provenance | Pass/Revise/Missing |  |  |
| Front matter | Pass/Revise/Missing |  |  |
| Abstract/keywords | Pass/Revise/Missing |  |  |
| Sections | Pass/Revise/Missing |  |  |
| Figures/tables/equations | Pass/Revise/Missing |  |  |
| Citations/references | Pass/Revise/Missing |  |  |
| Back matter | Pass/Revise/Missing |  |  |
| Package/render QA | Pass/Revise/Missing |  |  |
| Submission files | Pass/Revise/Missing |  |  |
