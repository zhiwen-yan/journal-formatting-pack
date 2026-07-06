#!/usr/bin/env python
import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional
from urllib.parse import urljoin

import requests


OUTPUT_DIR = Path(__file__).resolve().parent
JSON_PATH = OUTPUT_DIR / "scan-results.json"
MD_PATH = OUTPUT_DIR / "scan-summary.md"


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}


@dataclass
class Target:
    id: str
    publisher: str
    label: str
    kind: str
    url: str
    notes: str = ""


TARGETS: List[Target] = [
    Target("mdpi-authors", "MDPI", "MDPI Authors", "guidelines", "https://www.mdpi.com/authors"),
    Target("mdpi-latex", "MDPI", "MDPI LaTeX Hub", "template-entry", "https://www.mdpi.com/authors/latex"),
    Target("mdpi-nutrients", "MDPI", "Nutrients Instructions", "journal-instructions", "https://www.mdpi.com/journal/nutrients/instructions"),
    Target("mdpi-foods", "MDPI", "Foods Instructions", "journal-instructions", "https://www.mdpi.com/journal/foods/instructions"),
    Target("mdpi-jcm", "MDPI", "JCM Instructions", "journal-instructions", "https://www.mdpi.com/journal/jcm/instructions"),
    Target("frontiers-author-guidelines", "Frontiers", "Author Guidelines", "guidelines", "https://www.frontiersin.org/guidelines/author-guidelines"),
    Target("frontiers-nutrition-article-types", "Frontiers", "Frontiers in Nutrition Article Types", "journal-instructions", "https://www.frontiersin.org/journals/nutrition/for-authors/article-types"),
    Target("frontiers-pharmacology-article-types", "Frontiers", "Frontiers in Pharmacology Article Types", "journal-instructions", "https://www.frontiersin.org/journals/pharmacology/for-authors/article-types"),
    Target("elsevier-policies", "Elsevier", "Policies and Guidelines for Authors", "guidelines", "https://www.elsevier.com/researcher/author/policies-and-guidelines"),
    Target("elsevier-latex", "Elsevier", "LaTeX Instructions for Authors", "template-entry", "https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions"),
    Target("elsevier-your-paper-your-way", "Elsevier", "Guide for Authors - Your Paper Your Way", "guidelines", "https://www.elsevier.com/subject/next/guide-for-authors"),
    Target("springer-template-support", "Springer Nature", "Templates and Style Files", "template-entry", "https://support.springernature.com/en/support/solutions/articles/6000081241-templates-and-style-files-for-journal-article-preparation"),
    Target("springer-latex-support", "Springer Nature", "LaTeX Author Support", "template-entry", "https://www.springernature.com/gp/authors/campaigns/latex-author-support"),
    Target("springer-writing-manuscript", "Springer Nature", "Writing a Manuscript", "guidelines", "https://www.springernature.com/gp/authors/campaigns/writing-a-manuscript"),
    Target("taf-formatting-templates", "Taylor & Francis", "Formatting and Templates", "template-entry", "https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/formatting-and-templates/"),
    Target("taf-layout-guide", "Taylor & Francis", "Journal Manuscript Layout Guide", "guidelines", "https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/journal-manuscript-layout-guide/"),
    Target("taf-instructions-for-authors", "Taylor & Francis", "Instructions for Authors Guide", "guidelines", "https://authorservices.taylorandfrancis.com/publishing-your-research/making-your-submission/get-familiar-with-the-instructions-for-authors/"),
    Target("sage-sage-open", "SAGE", "Sage Open Submission Guidelines", "journal-instructions", "https://journals.sagepub.com/author-instructions/sgo", "SAGE template guidance is usually journal-level, not a single publisher-wide template page."),
    Target("sage-clinical-trials", "SAGE", "Clinical Trials Submission Guidelines", "journal-instructions", "https://journals.sagepub.com/author-instructions/ctj", "This page explicitly mentions Word and LaTeX templates."),
    Target("oup-general", "Oxford University Press", "Preparing and Submitting Your Manuscript", "guidelines", "https://academic.oup.com/pages/for-authors/journals/preparing-and-submitting-your-manuscript"),
    Target("oup-bioinformatics", "Oxford University Press", "Bioinformatics Author Guidelines", "journal-instructions", "https://academic.oup.com/bioinformatics/pages/author-guidelines", "OUP requirements are strongly journal-specific."),
    Target("oup-brain", "Oxford University Press", "Brain General Instructions", "journal-instructions", "https://academic.oup.com/brain/pages/general_instructions", "OUP requirements are strongly journal-specific."),
    Target("plos-one-guidelines", "PLOS", "PLOS ONE Submission Guidelines", "journal-instructions", "https://journals.plos.org/plosone/s/submission-guidelines"),
    Target("plos-one-latex", "PLOS", "PLOS ONE LaTeX", "template-entry", "https://journals.plos.org/plosone/s/latex"),
    Target("plos-one-getting-started", "PLOS", "PLOS ONE Getting Started", "guidelines", "https://journals.plos.org/plosone/s/getting-started"),
    Target("wiley-small", "Wiley", "Small Author Guidelines", "journal-instructions", "https://onlinelibrary.wiley.com/page/journal/16136829/homepage/author-guidelines", "Wiley guidance is reliably available on journal-level author-guidelines pages."),
    Target("wiley-clinical-case-reports", "Wiley", "Clinical Case Reports Author Guidelines", "journal-instructions", "https://onlinelibrary.wiley.com/page/journal/20500904/homepage/forauthors.html", "Wiley guidance is reliably available on journal-level forauthors pages."),
]


LINK_RE = re.compile(
    r"<a\b[^>]*href=[\"'](?P<href>[^\"']+)[\"'][^>]*>(?P<text>.*?)</a>",
    re.IGNORECASE | re.DOTALL,
)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")

KEYWORDS = (
    "template",
    "latex",
    "word",
    "docx",
    "overleaf",
    "guideline",
    "instructions",
    "submission",
    "author-guidelines",
    "for-authors",
    "forauthors",
    "guide-for-authors",
    "article-types",
    "manuscript",
    "style",
)


def clean_text(value: str) -> str:
    value = TAG_RE.sub(" ", value)
    value = SPACE_RE.sub(" ", value)
    return value.strip()


def extract_title(html: str) -> Optional[str]:
    match = TITLE_RE.search(html)
    if not match:
        return None
    return clean_text(match.group(1))


def extract_links(base_url: str, html: str) -> List[dict]:
    items = []
    seen = set()
    for match in LINK_RE.finditer(html):
        href = match.group("href").strip()
        text = clean_text(match.group("text"))
        if not href or href.startswith("#"):
            continue
        full_url = urljoin(base_url, href)
        haystack = f"{full_url} {text}".lower()
        if not any(keyword in haystack for keyword in KEYWORDS):
            continue
        if full_url in seen:
            continue
        seen.add(full_url)
        items.append({"text": text or "[no anchor text]", "url": full_url})
    return items[:12]


def classify_fetch(status_code: Optional[int], content_type: str, title: Optional[str], body: str) -> str:
    if status_code is None:
        return "request_failed"
    if status_code >= 400:
        return "http_error"
    body_l = body.lower()
    title_l = (title or "").lower()
    challenge_markers = ("just a moment", "access denied", "captcha", "attention required")
    if any(marker in title_l or marker in body_l for marker in challenge_markers):
        return "blocked"
    if "text/html" in content_type:
        return "fetched_html"
    return "fetched_file"


def fetch_target(session: requests.Session, target: Target) -> dict:
    result = asdict(target)
    result["checked_at_utc"] = datetime.now(timezone.utc).isoformat()
    result["status_code"] = None
    result["content_type"] = None
    result["final_url"] = None
    result["title"] = None
    result["fetch_status"] = None
    result["interesting_links"] = []
    result["error"] = None
    result["limitation"] = ""

    try:
        response = session.get(target.url, timeout=30, allow_redirects=True)
        result["status_code"] = response.status_code
        result["content_type"] = response.headers.get("Content-Type", "")
        result["final_url"] = response.url
        body = response.text[:600000]
        title = extract_title(body)
        result["title"] = title
        result["interesting_links"] = extract_links(response.url, body)
        result["fetch_status"] = classify_fetch(
            response.status_code,
            result["content_type"],
            title,
            body,
        )
    except Exception as exc:  # pragma: no cover
        result["fetch_status"] = "request_failed"
        result["error"] = str(exc)
        body = ""

    limitation_bits = []
    if target.publisher in {"Wiley", "SAGE", "Oxford University Press"}:
        limitation_bits.append("journal-specific requirements vary substantially")
    if target.publisher in {"Wiley", "SAGE"}:
        limitation_bits.append("no single stable publisher-wide template library page was confirmed in this scan")
    if result["fetch_status"] in {"blocked", "request_failed", "http_error"}:
        limitation_bits.append("needs manual follow-up")
    if result["kind"] == "template-entry" and not result["interesting_links"]:
        limitation_bits.append("download link may be embedded dynamically or require manual navigation")
    if target.notes:
        limitation_bits.append(target.notes)
    result["limitation"] = "; ".join(dict.fromkeys(limitation_bits))
    return result


def build_markdown(results: List[dict]) -> str:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ok_rows = []
    followup_rows = []
    for item in results:
        links_preview = "<br>".join(
            f"- [{link['text']}]({link['url']})" for link in item["interesting_links"][:4]
        )
        row = {
            "publisher": item["publisher"],
            "label": item["label"],
            "kind": item["kind"],
            "status": item["fetch_status"],
            "url": item["url"],
            "title": item["title"] or "",
            "notes": item["limitation"] or "",
            "links": links_preview or "-",
        }
        if item["fetch_status"] in {"fetched_html", "fetched_file"}:
            ok_rows.append(row)
        else:
            followup_rows.append(row)

    lines = [
        "# Official Source Scan",
        "",
        f"Generated: {generated}",
        "",
        "This folder records which official guideline pages and template-entry pages are directly fetchable now, plus where manual follow-up is still needed.",
        "",
        "## Fetchable Now",
        "",
        "| Publisher | Source | Kind | Status | Notes |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ok_rows:
        notes = row["notes"] or row["title"]
        lines.append(
            f"| {row['publisher']} | [{row['label']}]({row['url']}) | {row['kind']} | {row['status']} | {notes} |"
        )

    lines.extend(
        [
            "",
            "## Needs Manual Follow-Up",
            "",
            "| Publisher | Source | Kind | Status | Notes |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    if followup_rows:
        for row in followup_rows:
            notes = row["notes"] or row["title"] or "manual inspection needed"
            lines.append(
                f"| {row['publisher']} | [{row['label']}]({row['url']}) | {row['kind']} | {row['status']} | {notes} |"
            )
    else:
        lines.append("| - | - | - | - | No blocked targets in this run. |")

    lines.extend(
        [
            "",
            "## Link Hints From Fetched Pages",
            "",
        ]
    )
    for item in results:
        lines.append(f"### {item['publisher']} - {item['label']}")
        lines.append("")
        lines.append(f"- Source: [{item['url']}]({item['url']})")
        lines.append(f"- Status: `{item['fetch_status']}`")
        if item["title"]:
            lines.append(f"- Title: {item['title']}")
        if item["final_url"] and item["final_url"] != item["url"]:
            lines.append(f"- Final URL: [{item['final_url']}]({item['final_url']})")
        if item["limitation"]:
            lines.append(f"- Notes: {item['limitation']}")
        if item["interesting_links"]:
            lines.append("- Extracted links:")
            for link in item["interesting_links"][:8]:
                lines.append(f"  - [{link['text']}]({link['url']})")
        else:
            lines.append("- Extracted links: none captured by keyword scan")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    session = requests.Session()
    session.headers.update(HEADERS)

    results = [fetch_target(session, target) for target in TARGETS]

    JSON_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    MD_PATH.write_text(build_markdown(results), encoding="utf-8")

    print(f"Wrote {JSON_PATH}")
    print(f"Wrote {MD_PATH}")


if __name__ == "__main__":
    main()
