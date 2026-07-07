---
name: formatting-springer-nature
description: Springer Nature, BMC, and Nature Portfolio formatting and submission-readiness assistant. Use when the user asks to format, check, revise, polish, or prepare manuscripts for Springer, Springer Nature, BMC, Nature Portfolio, Scientific Reports, or BioMed Central journals. Check journal-specific submission guidelines, article type, title page, abstract, keywords, main text, references, figures, tables, supplementary information, ethics, consent, competing interests, funding, author contributions, data availability, AI-use disclosure, reporting guidelines, and submission package.
---

# formatting-springer-nature

## Workflow

1. Confirm whether the target title is Springer, BMC, Nature Portfolio, Scientific Reports, or another Springer Nature journal family.
2. Read the journal-specific submission guidelines. Use `references/official-guidelines.md` as a source map for common Springer Nature and BMC patterns.
3. Check article-type requirements before applying generic IMRaD structure.
4. Audit declarations, reporting guidelines, references, figure/table handling, and supplementary information.
5. Return the requested checklist, revised sections, title page, declarations, cover letter, response letter, or package.

## Required Inputs

Ask for:

- Target journal.
- Journal family or publisher if known.
- Article type.
- Official submission guidelines URL.
- Manuscript file or text.
- Whether humans, animals, public data, clinical trial data, AI tools, supplementary information, or code/data repositories are involved.

## Checks

Check:

- Title page and separate title page requirements.
- Abstract structure and article-type limits.
- Main text headings.
- Figures, tables, captions, legends, and supplementary information.
- References and citation style required by the target journal.
- Ethics approval, consent, trial registration, competing interests, funding, author contributions, data availability, acknowledgments, and AI-use disclosure.
- Reporting guideline compliance for clinical, observational, animal, review, qualitative, economic, and prediction-model studies.

## Output

For BMC-style manuscripts, group declaration sections clearly. For Nature Portfolio-style manuscripts, verify the target journal instructions before applying BMC-style declaration ordering.

## Guardrails

Do not merge Springer, BMC, and Nature Portfolio rules when the target journal has a specific instruction page. Mark uncertain family-level rules as needing confirmation.
