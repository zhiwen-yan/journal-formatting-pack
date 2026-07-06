# Official Source Scan

This folder stores a repeatable scan of official journal-submission guideline pages and template-entry pages.

Files:

- `scan_official_sources.py`: fetches curated official URLs and records basic metadata.
- `scan-results.json`: machine-readable scan output.
- `scan-summary.md`: human-readable summary of what was fetched and what still needs manual follow-up.

Use:

```powershell
python .\research\official-source-scan\scan_official_sources.py
```

Why this exists:

- publisher rules change
- template entry pages move
- some sites expose journal-specific pages rather than a single publisher-wide template library
- some download links are embedded dynamically or require manual navigation
