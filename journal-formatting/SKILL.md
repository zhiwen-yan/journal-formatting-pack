---
name: journal-formatting
description: Universal academic journal formatting and submission-readiness router. Use when the user asks to format, check, revise, polish, package, or prepare a manuscript for journal submission, including SCI, SSCI, PubMed-indexed, medical, nursing, public health, nutrition, pharmacology, life science, clinical research, systematic review, meta-analysis, case report, review, protocol, or original research manuscripts. Route publisher-specific tasks to frontiers-formatting, mdpi-formatting, wiley-formatting, elsevier-formatting, springer-nature-formatting, taylor-francis-formatting, sage-formatting, oup-formatting, plos-formatting, or generic-journal-formatting.
---

# Journal Formatting

## Purpose

Use this skill as the entry point for journal submission preparation. Identify the target journal, publisher, article type, and available official guidance, then route to the most specific formatting skill.

Prefer the user's current author guidelines URL, PDF, Word template, LaTeX template, or submission-system checklist over any bundled reference because journal requirements change.

## Required Inputs

Before changing a manuscript, collect or infer:

1. Target journal name.
2. Publisher, if known.
3. Article type.
4. Official author guidelines URL, PDF, or template.
5. Manuscript file or text.
6. Reference style, if known.
7. Research type: human participants, animal study, public database, clinical trial, software/code, qualitative research, systematic review, meta-analysis, or case report.
8. Required output: checklist, revised manuscript, Word-ready structure, references, title page, declarations, cover letter, response letter, or full submission package.

Ask concise follow-up questions only for missing information that changes the formatting decision. If the target journal is unknown, use `generic-journal-formatting` and clearly mark journal-specific items as "confirm with target journal".

## Routing

Route by official journal site, publisher imprint, submission system, or author guidelines page:

- Frontiers journals: use `frontiers-formatting`.
- MDPI journals: use `mdpi-formatting`.
- Wiley journals: use `wiley-formatting`.
- Elsevier or ScienceDirect journals: use `elsevier-formatting`.
- Springer Nature, BMC, or Nature Portfolio journals: use `springer-nature-formatting`.
- Taylor & Francis or Routledge journals: use `taylor-francis-formatting`.
- SAGE journals: use `sage-formatting`.
- Oxford University Press or Oxford Academic journals: use `oup-formatting`.
- PLOS journals: use `plos-formatting`.
- Unknown publisher or no target journal: use `generic-journal-formatting`.

Read `references/publisher-routing.md` when publisher identity, aliases, or first-batch source URLs are needed.

## Universal Workflow

1. Verify the target journal and article type against the latest official author instructions.
2. Identify required files: main manuscript, title page, cover letter, figures, tables, supplementary files, reporting checklist, ethics documents, and response letter if revising.
3. Check manuscript structure, abstract type, keywords, headings, figures, tables, references, declarations, and reporting guideline compliance.
4. Preserve scientific meaning and all factual content.
5. Use placeholders for missing author, ethics, funding, trial registration, repository, DOI, PMID, and reference metadata.
6. Produce the requested output plus a submission-readiness checklist.

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
