# MDPI Official Guidelines

Last checked: 2026-07-15.

Use these official starting points:

- MDPI author resources: https://www.mdpi.com/authors
- MDPI layout guide: https://www.mdpi.com/authors/layout
- MDPI reference guide: https://www.mdpi.com/authors/references
- Metabolites instructions: https://www.mdpi.com/journal/metabolites/instructions
- Nutrients instructions: https://www.mdpi.com/journal/nutrients/instructions
- Foods instructions: https://www.mdpi.com/journal/foods/instructions
- Journal of Clinical Medicine instructions: https://www.mdpi.com/journal/jcm/instructions

## Source Priority

Use sources in this order:

1. Current journal- and article-type-specific instructions and template.
2. Current MDPI publisher-level guidance.
3. Local rule profile.
4. Local structural fallback.

Do not present a local fallback as strict MDPI formatting.

## Template Acquisition

1. Select the journal and article type first.
2. Open the live instructions page and resolve the displayed Word or LaTeX template link.
3. Follow redirects; do not construct `{journal}-template.dot` URLs.
4. Record the instructions URL, final template URL, retrieval time, article type, and SHA-256.
5. Convert `.dot` or `.dotx` to `.docx` in a task-local directory before using `python-docx`.
6. Verify style names, page size, margins, header/footer, numbering, and line-number settings.

Template links can change without a new URL. Recheck them for every strict-formatting task. If automated access is blocked, use the browser session or ask the user to upload the template.

## Verify Every Run

- article-type structure and whether Conclusions or combined Results/Discussion are optional
- abstract type, labels, and whether the word limit is hard or advisory
- keyword minimum, maximum, and separator
- author–affiliation, correspondence, equal-contribution, and ORCID conventions
- figure/table/equation placement, captions, resolution, editability, and numbering
- citation placement, first-appearance order, reference pattern, and journal abbreviations
- conditional ethics, consent, trial, animal, data, funding, conflict, and AI-use statements
- cover letter, graphical abstract, highlights, reporting checklist, and supplementary files

## Common Back Matter

Many MDPI research articles use this order, but the exact journal rule wins:

1. Supplementary Materials
2. Author Contributions
3. Funding
4. Institutional Review Board Statement
5. Informed Consent Statement
6. Data Availability Statement
7. Acknowledgments
8. Conflicts of Interest
9. Optional abbreviations or appendices
10. References

Do not flatten conditional requirements into a mandatory list. Ethics and consent depend on the study; Data Availability is frequently required for all articles; AI disclosure depends on the current policy and actual use.

## Safety

Use “Not applicable” only when the authors confirm the factual basis and the journal allows it. Never invent author metadata, approvals, grants, registrations, repository links, conflicts, or reference facts.
