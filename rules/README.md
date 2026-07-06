# Rules Library

This folder stores machine-readable journal profiles used by the manuscript generators and by the skill instructions.

## Design Principles

- rules are maintained by the repository owner
- users should not need to update rules themselves
- official links are recorded for maintenance and verification
- official template files are not redistributed here by default

## Current Format

JSON rule profiles such as:

- `rules/mdpi/nutrients.json`
- `rules/mdpi/foods.json`
- `rules/mdpi/jcm.json`
- `rules/frontiers/frontiers-in-nutrition.json`
- `rules/plos/plos-one.json`

## Fields

- `journal`
- `publisher`
- `style`
- `guideline_url`
- `word_template_url`
- `latex_template_url`
- `last_checked`
- `reference_style`
- `keyword_rules`
- `formatting`
- `required_statements`
- `article_type_sections`

These profiles are intended to drive local generation defaults and to reduce the need for per-request manual guideline fetching.
