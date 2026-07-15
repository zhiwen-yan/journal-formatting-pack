# User Guide

## What This Pack Does

This skill pack helps users:

- check journal manuscript structure
- check required declaration sections
- generate Word manuscript skeletons
- generate LaTeX manuscript skeletons
- prepare a cleaner submission draft with placeholders for missing items
- migrate an existing DOCX into a verified official template when the journal-specific skill supports it

## What Users Need To Provide

### Minimum Input

- a manuscript file or manuscript text
- an article type

### Optional Input

- target journal, if not already implied by the skill name
- official template file, if the user wants a stricter template-based result
- Zotero `.bib` file for bibliography support

## Simplest Prompt

```text
Please use formatting-nutrients to check and organize this manuscript.
Article type: Original Research
```

The user can then upload a `.docx`, `.tex`, `.md`, or `.txt` manuscript file.

## Supported User Workflows

### 1. Minimal journal-specific prompt

```text
Please use formatting-nutrients to check and organize this manuscript.
Article type: Original Research
```

### 2. Publisher-level prompt

```text
Please use formatting-mdpi to check and organize this manuscript.
Target journal: Nutrients
Article type: Original Research
```

### 3. Universal router prompt

```text
Please use formatting-journal to check and organize this manuscript.
Target journal: Frontiers in Nutrition
Article type: Review
```

### 4. Strict template mode

```text
Please use formatting-mdpi to generate a manuscript that is as close as possible to the provided template.
Target journal: Journal of Clinical Medicine
Article type: Article
```

The skill should first resolve the official template from the current journal instructions. If automated access is blocked, the user should upload the template.

### 5. Metabolites existing-DOCX mode

```text
Please use formatting-metabolites to migrate this manuscript into the current official Metabolites Article template.
Keep the work format-only, preserve figures/tables/equations/citation fields, and list every missing fact as an author query.
```

## Default Checks

For supported journal skills, users do not need to list these every time. The skill should check them by default:

1. main manuscript structure
2. reference section
3. Author Contributions
4. Funding
5. Institutional Review Board Statement
6. Informed Consent Statement
7. Data Availability Statement
8. Conflicts of Interest

## Expected Outputs

Depending on the request, the skill can return:

- missing-items checklist
- revised section outline
- draft declaration blocks
- Word manuscript skeleton
- LaTeX manuscript skeleton
- formatted DOCX plus formatting audit, author queries, change log, and template provenance

## Notes On Templates

- users do not need an official template for an audit or structural draft
- strict template output requires the current official journal- and article-type-specific template
- local rule profiles and generators create structural drafts; they do not prove template matching
- every transformed DOCX should be reopened, structurally audited, rendered, and inspected page by page
