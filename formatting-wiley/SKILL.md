---
name: formatting-wiley
description: Wiley journal formatting and submission-readiness assistant. Use when the user asks to format, check, revise, polish, or prepare manuscripts for Wiley journals, including nursing, medical, public health, life science, clinical, and social science journals. Check journal-specific author guidelines, article type, title page, abstract, keywords, main text, references, figures, tables, supporting information, ethics approval, consent, data availability, author contributions, funding, conflict of interest, acknowledgments, AI-use disclosure, and reporting guideline compliance.
---

# Wiley Formatting

## Workflow

1. Confirm the exact Wiley journal and article type.
2. Read the current journal-specific author guidelines. Wiley requirements vary heavily by title, so treat `references/official-guidelines.md` as a source map, not a complete rulebook.
3. Check whether the journal uses free-format submission, a structured template, or strict article-type limits.
4. Audit manuscript structure, references, figures, tables, supporting information, declarations, and reporting guidelines.
5. Prepare the requested checklist, revised manuscript sections, cover letter, response letter, or submission package.

## Required Inputs

Ask for:

- Target Wiley journal.
- Article type.
- Journal author guidelines URL.
- Manuscript file or text.
- Reference style, if known.
- Whether humans, animals, public data, clinical trials, qualitative data, AI tools, or supplementary files are involved.

## Checks

Check:

- Title page and blinded/unblinded submission requirements.
- Abstract type and word limit from the journal page.
- Main headings required by the article type.
- Reference style and journal abbreviation rules.
- Figure, table, and supporting information requirements.
- Ethics approval, consent, data availability, author contributions, funding, conflicts of interest, acknowledgments, and AI-use disclosure.
- Reporting guideline: CONSORT, STROBE, PRISMA, CARE, ARRIVE, TRIPOD, RECORD, COREQ, CHEERS, or another guideline required by the journal.

## Output

Always separate "confirmed from official guideline" from "needs journal confirmation" when the user has not provided a current URL.

## Guardrails

Do not infer journal-specific word limits, abstract types, reference styles, or anonymization rules without the current author guidelines.
