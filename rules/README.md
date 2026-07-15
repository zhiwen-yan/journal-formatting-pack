# Rules Library

This folder stores machine-readable journal profiles used by generators, audits, and skill instructions.

## Authority

- Treat every rule as a dated cache of official requirements.
- Let the current journal instructions and article-type template override local values.
- Record official URLs and `last_checked`.
- Do not redistribute publisher-owned templates by default.
- Do not call a local fallback strict template formatting.

## Core Fields

- `journal`, `aliases`, `publisher`, `style`
- `guideline_url`, `layout_guide_url`, `reference_guide_url`
- `word_template_url`, `latex_template_url`, `template_variants`
- `last_checked`, `source_provenance`, `template_policy`
- `generator_policy`, including explicitly supported article types
- `default_article_type`, `article_type_sections`
- `abstract_rules`, `keyword_rules`
- `formatting`
- `front_matter_rules`
- `declaration_order`, `back_matter_rules`, `method_disclosures`
- `figure_rules`, `table_rules`
- `citation_rules`, `reference_rules`
- `optional_submission_elements`, `delivery_requirements`

Profiles may retain older fields such as `required_statements` for compatibility, but new conditional requirements should use structured objects.

## Conditional Rules

Use `required`, `required_when`, and `optional` instead of forcing every declaration into every manuscript. Keep human ethics, animal ethics, informed consent, trial registration, public-data analysis, and generative-AI disclosure distinct.

Missing factual inputs must become author queries. A rule profile must never supply an approval number, grant, author detail, repository link, conflict, DOI, or other manuscript fact.

## Formatting Values

Formatting values are fallback data for structural drafts and QA expectations. When `template_managed` is true, official template styles and section properties win. Record `fallback_scope` as `structural draft only` when the generator does not apply the official template.

## Validation

At minimum:

1. Parse every JSON profile.
2. Confirm generator inference for known journal aliases.
3. Test keyword, abstract, section, and declaration behavior.
4. Generate and reopen a DOCX.
5. Run package QA and full-page rendering for template migrations.
