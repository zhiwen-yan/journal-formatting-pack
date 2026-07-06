# Project Plan

## Goal

Build a GitHub-ready skill pack that helps users generate and check journal manuscripts without requiring them to visit publisher websites for every request.

## Product Positioning

- Public GitHub repository
- Local skill pack for Codex
- Rule-library driven
- Official-template aware, but not a redistribution mirror for publisher files

## Core User Promise

Users should be able to:

1. upload a manuscript file or paste manuscript text
2. provide only a short prompt plus article type
3. receive a checklist, missing-items report, and Word/LaTeX manuscript skeleton

## Scope

### Included

- journal and publisher routing
- manuscript structure checks
- declaration checks
- reference placeholder handling
- Word skeleton generation
- LaTeX skeleton generation
- local rule profiles
- official source maps for maintenance

### Excluded

- publisher-template redistribution
- automatic end-user source updates
- fabricated references or declarations

## Repository Layers

### Skills

- `formatting-journal`
- `formatting-mdpi`
- `formatting-frontiers`
- `formatting-elsevier`
- `formatting-springer-nature`
- `formatting-wiley`
- `formatting-sage`
- `formatting-oup`
- `formatting-plos`
- `formatting-generic`
- `formatting-nutrients`
- `formatting-foods`
- `formatting-jcm`

### Rules

Machine-readable journal profiles under `rules/`.

### Templates

Project-owned skeletons and section snippets under `templates/`.

### Research

Official source scans and maintenance notes under `research/`.

## Delivery Phases

### Phase 1

- finalize skill routing
- support minimal prompts
- support direct manuscript uploads
- generate Word and LaTeX skeletons

### Phase 2

- deepen high-frequency journal rules
- improve journal-specific statement logic
- refine near-official visual defaults

### Phase 3

- expand publisher coverage
- add richer readiness audits
- improve strict-template workflow when users provide official files

## Maintenance Model

- repository owner updates rules manually
- users consume the latest published repository version
- official links are stored for maintenance, not for mandatory per-request fetching

## Safety Rules

- never invent ethics approvals, funding numbers, or bibliography metadata
- use placeholders for missing facts
- clearly separate unofficial skeletons from official publisher templates
