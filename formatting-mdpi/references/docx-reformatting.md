# MDPI Existing-DOCX Reformatting

Read this file when the input is an existing `.docx`. This workflow is separate from creating a new skeleton.

## 1. Freeze Scope

- Preserve the source file and write to a new output path.
- Record whether the request is format-only or also authorizes copyediting.
- Treat changes to scientific claims, methods, sample counts, dates, statistics, citations, and conclusions as content edits.
- Put every content edit in a separate change log and obtain author confirmation when it was not explicitly requested.

## 2. Select And Record The Official Template

1. Verify the exact journal and article type on the live instructions page.
2. Resolve the template link displayed for that article type; do not construct a URL from the journal slug.
3. Follow redirects and record:
   - instructions URL
   - final template URL
   - journal and article type
   - retrieval timestamp
   - SHA-256
4. Save the template in a task-local working directory.
5. Convert `.dot` or `.dotx` to `.docx` with Word or LibreOffice before opening it with `python-docx`.
6. Reopen the converted file and verify expected MDPI styles, A4 or required page size, margins, line numbering, and header/footer content.

If download or conversion fails, ask the user to upload the official template. Without a verified template, label the output `structure-only draft`.

## 3. Inventory The Source

Run `../scripts/qa_docx.py --input <source.docx>` and retain its report. Also inspect:

- paragraphs and visible text
- sections, page breaks, headers, footers, and line numbering
- style histogram and direct formatting
- inline and anchored drawings
- image formats, displayed sizes, intrinsic pixels, and effective resolution
- editable tables, merged cells, widths, and repeat-header settings
- OMML or MathType equations
- hyperlinks and bookmarks
- simple and complex fields, including Zotero and EndNote fields
- footnotes, endnotes, comments, tracked insertions/deletions, and custom XML
- captions, cross-references, numbered lists, and bibliography numbering

Do not remove custom XML, relationships, or field codes merely because they look unfamiliar.

## 4. Choose A Safe Transformation Strategy

Prefer one of these tested strategies:

- Build on the official template package, remove only confirmed sample body content, then insert the manuscript while mapping styles and relationships.
- Apply template-derived styles to a copy of the source only when styles, numbering, theme, header/footer relationships, and section properties are remapped together and covered by preservation tests.

Do not copy only `styles.xml` nodes or raw header/footer XML without their numbering, theme, media, hyperlink, and relationship dependencies.

Never generalize a one-off formatter that uses fixed paragraph indexes, author names, table indexes, figure filenames, or a hand-written journal-abbreviation map.

## 5. Map The Manuscript

### Front matter

- Preserve the article type, title, full author names, affiliation markers, and correspondence markers.
- Rebuild author–affiliation mapping from source facts only.
- Use visible author queries for missing address, postal code, country, email, ORCID, equal-contribution, or corresponding-author data.
- Preserve publisher-owned DOI, editor, received/accepted, and page placeholders from the official template.

### Abstract and keywords

- Apply journal- and article-type-specific abstract labels and word target.
- Keep structured labels as inline bold runs when the template does so.
- Preserve scientific wording unless content editing is authorized.
- Enforce keyword minimum/maximum and separator without inventing terms.

### Main text

- Map headings to official MDPI heading styles and verify numbering at levels 1, 1.1, and 1.1.1.
- Avoid duplicate numbering on repeat runs.
- Keep equations editable and adjacent explanatory text intact.
- Keep cross-references and bookmarks functional.

### Figures

- Place each figure near its first citation and keep captions below.
- Preserve aspect ratio and prefer author-supplied originals over embedded previews.
- Compute effective resolution from intrinsic pixels and displayed size; warn instead of upscaling.
- Combine and describe multi-panel figures consistently.
- Add useful alt text and record permissions or credit queries.
- Verify that figure numbers and in-text citations are complete and ordered.

### Tables

- Keep tables editable and put captions above.
- Fit the printable width, repeat header rows, and preserve merged cells.
- Keep text at or above the journal minimum.
- Explain abbreviations, symbols, tests, and units in table notes.
- Do not use manuscript-specific fixed widths without checking actual content.

### Citations and references

- Preserve citation-manager fields.
- Check that every numeric citation resolves and every reference is cited.
- Check first-appearance order, ranges, duplicates, and caption citations.
- Put numeric citations relative to punctuation as required by the journal.
- Format only from verified metadata; never invent DOI, pages, issue, accessed date, or ISO 4 abbreviation.

### Back matter

- Use the journal rule profile for order and conditional requirements.
- Mark missing CRediT roles, funding facts, ethics committee/protocol/date, consent basis, data/code access, acknowledgments, conflicts, and AI-use facts as author queries.
- Use “Not applicable” only when factually true and allowed by current instructions.

## 6. Package QA

After every material edit:

1. Save to a new file.
2. Reopen with `python-docx` or Word.
3. Run ZIP integrity checks and confirm every `r:id` or image embed has a valid relationship.
4. Run `qa_docx.py --input <output> --source <source> --rules <journal.json>`.
5. Review text-similarity and object-count deltas. Explain every intentional difference.
6. Confirm no unresolved template sample text, broken fields, or untracked author queries.

## 7. Render QA

Render the final DOCX to PDF and page PNGs. Inspect every page at full resolution, not only a contact sheet. Check:

- blank or nearly blank pages
- clipped or overflowing text and tables
- split captions or captions separated from objects
- stretched, cropped, blurry, or substituted images
- orphan headings, widows, and excessive whitespace
- font substitution and symbol corruption
- header/footer, page number, and line-number behavior
- reference hanging indents and numbering
- cross-platform differences between Word and LibreOffice

When LibreOffice incorrectly numbers header/footer lines, record the compatibility workaround and verify that body line numbering remains continuous.

## 8. Deliver And Label Honestly

Deliver the formatted DOCX with:

- formatting audit
- author-query list
- content/change log
- template provenance record

Use `template-matched and verified` only when the official template, package checks, and full-page render review all passed. Any unresolved factual placeholder changes the status to `template-matched with author queries`.
