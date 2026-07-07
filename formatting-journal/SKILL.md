---
name: formatting-journal
description: Universal academic journal formatting and submission-readiness router. Use when the user asks to format, check, revise, polish, package, or prepare a manuscript for journal submission, including SCI, SSCI, PubMed-indexed, medical, nursing, public health, nutrition, pharmacology, life science, clinical research, systematic review, meta-analysis, case report, review, protocol, or original research manuscripts. Route publisher-specific tasks to formatting-frontiers, formatting-mdpi, formatting-wiley, formatting-elsevier, formatting-springer-nature, formatting-taylor-francis, formatting-sage, formatting-oup, formatting-plos, or formatting-generic. Also use this skill when the user wants a generated Word manuscript skeleton or LaTeX manuscript skeleton.
---

# formatting-journal

## Purpose

Use this skill as the entry point for journal submission preparation. Identify the target journal, publisher, article type, and available official guidance, then route to the most specific formatting skill.

Prefer the user's current author guidelines URL, PDF, Word template, LaTeX template, or submission-system checklist over any bundled reference because journal requirements change.

This skill should support minimal prompts. If the user uploads a manuscript file and only says something like `Please use formatting-journal to check and organize this manuscript.`, infer as much as possible from the file and ask only for the minimum missing information that changes routing or output.

## Required Inputs

Before changing a manuscript, collect or infer:

1. Target journal name.
2. Publisher, if known.
3. Article type.
4. Official author guidelines URL, PDF, or template, if already available.
5. Manuscript file or text. Direct uploads are preferred when available.
6. Reference style, if known.
7. Research type: human participants, animal study, public database, clinical trial, software/code, qualitative research, systematic review, meta-analysis, or case report.
8. Required output: checklist, revised manuscript, Word-ready structure, references, title page, declarations, cover letter, response letter, or full submission package.

Ask concise follow-up questions only for missing information that changes the formatting decision. If the target journal is unknown, use `formatting-generic` and clearly mark journal-specific items as "confirm with target journal".

## Minimal Prompt Mode

When the user supplies only:

- a manuscript file or pasted manuscript text
- an article type

you should still proceed.

Default behavior in minimal mode:

1. infer the manuscript structure from the uploaded content
2. infer or ask for the target journal only if the current skill name does not already fix it
3. check structure, references, and declaration sections by default
4. return a missing-items list plus an organized manuscript skeleton when requested

## Routing

Route by official journal site, publisher imprint, submission system, or author guidelines page:

- Frontiers journals: use `formatting-frontiers`.
- MDPI journals: use `formatting-mdpi`.
- Wiley journals: use `formatting-wiley`.
- Elsevier or ScienceDirect journals: use `formatting-elsevier`.
- Springer Nature, BMC, or Nature Portfolio journals: use `formatting-springer-nature`.
- Taylor & Francis or Routledge journals: use `formatting-taylor-francis`.
- SAGE journals: use `formatting-sage`.
- Oxford University Press or Oxford Academic journals: use `formatting-oup`.
- PLOS journals: use `formatting-plos`.
- Unknown publisher or no target journal: use `formatting-generic`.

Read `references/publisher-routing.md` when publisher identity, aliases, or first-batch source URLs are needed.

## Universal Workflow

1. Verify the target journal and article type against the latest official author instructions.
2. Identify required files: main manuscript, title page, cover letter, figures, tables, supplementary files, reporting checklist, ethics documents, and response letter if revising.
3. Check manuscript structure, abstract type, keywords, headings, figures, tables, references, declarations, and reporting guideline compliance.
4. Preserve scientific meaning and all factual content.
5. Use placeholders for missing author, ethics, funding, trial registration, repository, DOI, PMID, and reference metadata.
6. Produce the requested output plus a submission-readiness checklist.

When the user does not list specific checkpoints, treat these as default checks:

- manuscript structure
- references
- Author Contributions
- Funding
- Institutional Review Board or ethics statement
- Informed Consent Statement when relevant
- Data Availability Statement
- Conflicts of Interest

## Output File Generation

When the user explicitly asks for a Word document or LaTeX manuscript skeleton, use `scripts/generate_manuscript.py`.

Read `references/manuscript-generator.md` and use `references/example-manuscript.json` as the schema example.

Supported file outputs:

- `.docx` Word manuscript skeleton
- `.tex` LaTeX manuscript skeleton

The generator supports:

- title page
- abstract
- keywords
- structured main sections
- declaration sections
- references placeholder

### Zotero Rules

If the user wants the references area to connect to Zotero:

- Use a Zotero-exported `.bib` file when available.
- Accept either `--zotero-bib <path>` or `ZOTERO_BIB_PATH`.
- If Zotero is not configured, do not invent references.
- If Zotero is not configured, tell the user how to configure it and leave a references placeholder.
- If the user says Zotero is mandatory, run the generator with `--zotero-mode required` so the script stops with a prompt instead of silently continuing.

## Universal Checklist

Check these modules for every journal:

| Module | Status | Problem | Required fix |
|---|---|---|---|
| Target journal and article type | Pass/Revise/Missing |  |  |
| Title and running title | Pass/Revise/Missing |  |  |
| Authors and affiliations | Pass/Revise/Missing |  |  |
| Abstract | Pass/Revise/Missing |  |  |
| Keywords | Pass/Revise/Missing |  |  |
| Main text structure | Pass/Revise/Missing |  |  |
| Figures and captions | Pass/Revise/Missing |  |  |
| Tables and legends | Pass/Revise/Missing |  |  |
| Supplementary material | Pass/Revise/Missing |  |  |
| In-text citations | Pass/Revise/Missing |  |  |
| References | Pass/Revise/Missing |  |  |
| Ethics and consent | Pass/Revise/Missing |  |  |
| Trial registration | Pass/Revise/Missing |  |  |
| Data availability | Pass/Revise/Missing |  |  |
| Author contributions | Pass/Revise/Missing |  |  |
| Funding | Pass/Revise/Missing |  |  |
| Conflicts of interest | Pass/Revise/Missing |  |  |
| AI-use disclosure | Pass/Revise/Missing |  |  |
| Reporting guideline | Pass/Revise/Missing |  |  |
| Submission files | Pass/Revise/Missing |  |  |

## Article Type Checks

For original research, expect Introduction, Methods, Results, Discussion, declarations, references, and figure/table material unless the journal says otherwise.

For reviews, expect a clear narrative structure, search method if applicable, declarations, and references.

For systematic reviews and meta-analyses, check PRISMA, registration such as PROSPERO when applicable, search strategy, eligibility criteria, selection process, extraction, risk of bias, synthesis method, and flow diagram.

For case reports, check CARE, patient consent, clinical timeline, diagnostic assessment, intervention, outcome, and patient perspective if required.

For clinical trials, check registry name, registration number, registration date, CONSORT when applicable, and ethics approval.

For animal studies, check ARRIVE when applicable and animal ethics approval.

## Reference Handling

Never invent or "complete" citation facts. Preserve citation content while changing style.

If metadata are missing, mark them explicitly:

- `[missing DOI]`
- `[missing page range]`
- `[missing volume/issue]`
- `[verify PMID]`
- `[verify journal abbreviation]`
- `[source needed]`

If the user asks for new references, search official bibliographic sources or ask the user for source papers before adding them.

## Behavior Rules

- Do not invent DOI, PMID, PMCID, trial registration, ethics approval, funding award, author details, correspondence email, ORCID, data repository links, or conflicts of interest.
- Do not change statistical results or scientific claims unless asked.
- Do not silently remove declarations; if not applicable, draft an "Not applicable" version only when the journal allows it and the user confirms the factual basis.
- Prefer official journal instructions over publisher-level references, and publisher-level references over generic rules.
- Record any unverified requirement in the output as "needs official confirmation".
