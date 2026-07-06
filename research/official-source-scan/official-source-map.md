# Official Source Map

This note interprets the latest scan and separates three situations:

1. `request-fetchable`: direct scripted fetch worked
2. `browser-fetchable`: page is reachable in browser/search, but scripted fetch was blocked or unstable
3. `journal-specific/manual`: there is no single stable publisher-wide template hub, so the exact journal page still needs to be selected

Last reviewed: 2026-07-07.

## MDPI

- Status: `browser-fetchable`
- Main rules page: [MDPI Authors](https://www.mdpi.com/authors)
- Main LaTeX page: [Preparing Manuscripts in LaTeX](https://www.mdpi.com/authors/latex)
- Key journal pages:
  - [Nutrients Instructions](https://www.mdpi.com/journal/nutrients/instructions)
  - [Foods Instructions](https://www.mdpi.com/journal/foods/instructions)
  - [JCM Instructions](https://www.mdpi.com/journal/jcm/instructions)
- Direct template links confirmed from the journal instruction pages:
  - Nutrients Word: [nutrients-template.dot](https://www.mdpi.com/files/word-templates/nutrients-template.dot)
  - Foods Word: [foods-template.dot](https://www.mdpi.com/files/word-templates/foods-template.dot)
  - JCM Word: [jcm-template.dot](https://www.mdpi.com/files/word-templates/jcm-template.dot)
- Direct LaTeX package links confirmed from the MDPI LaTeX page:
  - [MDPI ACS Citation Style](https://mdpi-res.com/data/MDPI_template_ACS.zip?v=20260623)
  - [MDPI APA Citation Style](https://mdpi-res.com/data/MDPI_template_APA.zip?v=20260623)
  - [MDPI Chicago Citation Style](https://mdpi-res.com/data/MDPI_template_Chicago.zip?v=20260623)
  - [MDPI LyX Template](https://mdpi-res.com/data/MDPI_template_lyx.zip?v=20260623)
- Practical note: MDPI blocked our direct request client, but the official pages and template entry points are still reachable through browser-style access.

## Frontiers

- Status: `request-fetchable` plus `browser-fetchable`
- General rules:
  - [Author Guidelines](https://www.frontiersin.org/guidelines/author-guidelines)
- Journal/article-type pages:
  - [Frontiers in Nutrition Article Types](https://www.frontiersin.org/journals/nutrition/for-authors/article-types)
  - [Frontiers in Pharmacology Article Types](https://www.frontiersin.org/journals/pharmacology/for-authors/article-types)
- Direct templates exposed on the author-guidelines page:
  - [Frontiers Word Templates](https://www.frontiersin.org/Design/zip/Frontiers_Word_Templates.zip)
  - [Frontiers LaTeX Templates](https://www.frontiersin.org/design/zip/Frontiers_LaTeX_Templates.zip)
- Practical note: article-type pages fetch cleanly. The general author-guidelines page is reachable and exposes direct template zip links.

## Elsevier

- Status: `request-fetchable`
- Rules:
  - [Policies and Guidelines for Authors](https://www.elsevier.com/researcher/author/policies-and-guidelines)
  - [Guide for Authors - Your Paper Your Way](https://www.elsevier.com/subject/next/guide-for-authors)
- Template entry:
  - [LaTeX Instructions for Authors](https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions)
- Direct template files found:
  - [elsarticle.zip](https://assets.ctfassets.net/o78em1y1w4i4/4MpsJHO0MOJ2xZuwGTAbOZ/7bc64af36477c5d6cfce335a1f872363/elsarticle.zip)
  - [els-cas-templates.zip](https://assets.ctfassets.net/o78em1y1w4i4/5uFmLZJTPDMAUjFnHRpjj8/6f19a979146eb93263763d87a894ab0d/els-cas-templates.zip)
  - [ecrc-template.tex](https://assets.ctfassets.net/o78em1y1w4i4/27zowmUKIvbiPUxbbnVFFK/4ca39b5f4d636af37e783f0625bd81f3/ecrc-template.tex)
- Practical note: Elsevier is the cleanest target for direct automation in this scan.

## Springer Nature

- Status: `request-fetchable` on support pages, `browser-fetchable` on some campaign pages
- Support pages:
  - [Templates and Style Files for Journal Article Preparation](https://support.springernature.com/en/support/solutions/articles/6000081241-templates-and-style-files-for-journal-article-preparation)
  - [LaTeX Template Package for Article/Book Submissions](https://support.springernature.com/en/support/solutions/articles/6000250920-latex-template-package-for-article-book-submissions)
  - [Submit a LaTeX Manuscript Using Overleaf](https://support.springernature.com/en/support/solutions/articles/6000127538-submit-a-latex-manuscript-to-a-springer-nature-journal-using-overleaf)
  - [Writing a Journal Manuscript](https://support.springernature.com/en/support/solutions/articles/6000234503-writing-a-journal-manuscript)
- Browser-only/campaign page:
  - [LaTeX Author Support](https://www.springernature.com/gp/authors/campaigns/latex-author-support)
- Practical note: prefer the support-center URLs for automation. They are more stable than the campaign pages.

## Taylor & Francis

- Status: `request-fetchable`
- Rules and template entry:
  - [Formatting and Templates](https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/formatting-and-templates/)
  - [Journal Manuscript Layout Guide](https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/journal-manuscript-layout-guide/)
  - [Instructions for Authors Guide](https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/get-familiar-with-the-instructions-for-authors/)
- Direct files found:
  - [Template Instructions PDF](http://www.tandf.co.uk/journals/authors/template/TF_Template_Word_Windows_2016_instructions.pdf)
  - [Template ZIP](https://authstaging.wpengine.com/wp-content/uploads/2020/12/TF_Template_Word_Windows_2016.zip)
- Practical note: strong candidate for direct automated rule/template harvesting.

## SAGE

- Status: `browser-fetchable`, `journal-specific/manual`
- Example journal pages:
  - [Sage Open Submission Guidelines](https://journals.sagepub.com/author-instructions/sgo)
  - [Clinical Trials Submission Guidelines](https://journals.sagepub.com/author-instructions/ctj)
- What we confirmed:
  - SAGE journal pages are reachable and contain concrete formatting rules
  - Word is typically preferred
  - LaTeX is accepted in at least some journals
  - template links are referred to through the journal author gateway rather than one unified publisher template hub
- Practical note: SAGE can be supported well, but the automation should resolve to the actual journal page first.

## Oxford University Press

- Status: `browser-fetchable`, `journal-specific/manual`
- General page:
  - [Preparing and Submitting Your Manuscript](https://academic.oup.com/pages/for-authors/journals/preparing-and-submitting-your-manuscript)
- Example journal pages:
  - [Bioinformatics Author Guidelines](https://academic.oup.com/bioinformatics/pages/author-guidelines)
  - [Brain General Instructions](https://academic.oup.com/brain/pages/general_instructions)
- What we confirmed:
  - OUP explicitly says formatting requirements differ by journal
  - Word or LaTeX submission is supported at the general level
  - declarations, data policy, and style details still need journal-level confirmation
- Practical note: OUP should be treated as a journal-specific family, not a one-template publisher.

## PLOS

- Status: `request-fetchable`
- Rules and template entry:
  - [PLOS ONE Submission Guidelines](https://journals.plos.org/plosone/s/submission-guidelines)
  - [PLOS ONE LaTeX](https://journals.plos.org/plosone/s/latex)
  - [PLOS ONE Getting Started](https://journals.plos.org/plosone/s/getting-started)
- Practical note: PLOS is another good automation target for direct fetching.

## Wiley

- Status: `browser-fetchable`, `journal-specific/manual`
- Example journal pages:
  - [Small Author Guidelines](https://onlinelibrary.wiley.com/page/journal/16136829/homepage/author-guidelines)
  - [Clinical Case Reports Author Guidelines](https://onlinelibrary.wiley.com/page/journal/20500904/homepage/forauthors.html)
- What we confirmed:
  - Wiley journal pages are reachable and contain concrete author instructions
  - there is no single stable publisher-wide template library page confirmed in this scan
  - URL patterns vary between `author-guidelines` and `forauthors.html`
- Practical note: Wiley should be supported by journal-page resolution, not by assuming one unified template endpoint.

## Best Automation Targets Right Now

These are the easiest families to automate first:

1. Elsevier
2. Taylor & Francis
3. PLOS
4. Frontiers
5. MDPI, if we allow browser-style fallback instead of plain request-only fetching

## Still Not Ideal for Fully Uniform Automation

These can be supported, but should be modeled as journal-specific lookups:

1. Wiley
2. SAGE
3. Oxford University Press
4. Springer Nature, when journal-specific template rules diverge from the generic support pages
