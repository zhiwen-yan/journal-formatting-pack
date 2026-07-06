from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt


DECLARATION_ORDER = [
    ("author_contributions", "Author Contributions"),
    ("funding", "Funding"),
    ("institutional_review_board_statement", "Institutional Review Board Statement"),
    ("informed_consent_statement", "Informed Consent Statement"),
    ("data_availability_statement", "Data Availability Statement"),
    ("acknowledgments", "Acknowledgments"),
    ("conflicts_of_interest", "Conflicts of Interest"),
    ("ai_use_disclosure", "AI-Use Disclosure"),
]

NUMERIC_REFERENCE_STYLES = {"vancouver", "ama", "numeric", "numbered", "mdpi"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Word or LaTeX manuscript skeleton from structured JSON input."
    )
    parser.add_argument("--input", required=True, help="Path to the manuscript JSON input.")
    parser.add_argument(
        "--output-format",
        required=True,
        choices=["word", "latex"],
        help="Output format: word (.docx) or latex (.tex).",
    )
    parser.add_argument("--output", help="Destination file path.")
    parser.add_argument("--style", help="Style profile such as generic or mdpi.")
    parser.add_argument("--journal", help="Journal name override.")
    parser.add_argument("--article-type", help="Article type override.")
    parser.add_argument(
        "--zotero-mode",
        choices=["auto", "required", "disabled"],
        default="auto",
        help="How to handle Zotero bibliography configuration.",
    )
    parser.add_argument(
        "--zotero-bib",
        help="Path to a Zotero-exported .bib file. If omitted, the script checks ZOTERO_BIB_PATH.",
    )
    return parser.parse_args()


def load_payload(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def article_sections(style: str, article_type: str) -> list[dict[str, Any]]:
    normalized = article_type.strip().lower()
    if "review" in normalized and "systematic" in normalized:
        titles = [
            "Introduction",
            "Methods",
            "Results",
            "Discussion",
            "Conclusions",
        ]
    elif "review" in normalized:
        titles = [
            "Introduction",
            "Main Sections",
            "Discussion",
            "Conclusions",
        ]
    elif "case report" in normalized:
        titles = [
            "Introduction",
            "Case Presentation",
            "Discussion",
            "Conclusions",
        ]
    else:
        titles = [
            "Introduction",
            "Materials and Methods" if style == "mdpi" else "Methods",
            "Results",
            "Discussion",
            "Conclusions",
        ]
    return [{"title": title, "paragraphs": [f"TODO: Draft the {title.lower()} section."]} for title in titles]


def default_declarations() -> dict[str, str]:
    return {
        "author_contributions": "TODO: Describe each author's contribution.",
        "funding": "TODO: State the funding source or write 'This research received no external funding.'",
        "institutional_review_board_statement": "TODO: Provide IRB approval details or confirm not applicable.",
        "informed_consent_statement": "TODO: Provide informed consent details or confirm not applicable.",
        "data_availability_statement": "TODO: Describe data availability or access restrictions.",
        "acknowledgments": "TODO: Add acknowledgments or delete if not applicable.",
        "conflicts_of_interest": "TODO: State conflicts of interest or write 'The authors declare no conflict of interest.'",
        "ai_use_disclosure": "TODO: State whether AI tools were used in drafting, editing, coding, or analysis.",
    }


def normalize_authors(payload: dict[str, Any]) -> list[dict[str, Any]]:
    authors = payload.get("authors") or []
    if authors:
        return authors
    return [
        {
            "name": "TODO: Author Name",
            "affiliations": [1],
            "email": "TODO: corresponding.author@example.com",
            "corresponding": True,
        }
    ]


def normalize_affiliations(payload: dict[str, Any]) -> list[dict[str, Any]]:
    affiliations = payload.get("affiliations") or []
    if affiliations:
        return affiliations
    return [{"id": 1, "text": "TODO: Author affiliation"}]


def normalize_payload(
    payload: dict[str, Any],
    output_format: str,
    default_style: str | None = None,
    default_journal: str | None = None,
    default_article_type: str | None = None,
) -> dict[str, Any]:
    style = (payload.get("style") or default_style or "generic").strip().lower()
    article_type = payload.get("article_type") or default_article_type or "Original Research"
    journal = payload.get("journal") or default_journal or "TODO: Target Journal"
    keywords = payload.get("keywords") or ["TODO keyword 1", "TODO keyword 2", "TODO keyword 3"]
    sections = payload.get("sections") or article_sections(style, article_type)
    declarations = default_declarations()
    declarations.update(payload.get("declarations") or {})
    normalized = {
        "style": style,
        "output_format": output_format,
        "journal": journal,
        "article_type": article_type,
        "title": payload.get("title") or "TODO: Manuscript Title",
        "running_title": payload.get("running_title") or "",
        "language": payload.get("language") or "English",
        "reference_style": payload.get("reference_style") or ("MDPI" if style == "mdpi" else "Numeric"),
        "authors": normalize_authors(payload),
        "affiliations": normalize_affiliations(payload),
        "corresponding_author_note": payload.get("corresponding_author_note") or "",
        "abstract": payload.get("abstract") or "TODO: Provide the abstract.",
        "keywords": keywords,
        "sections": sections,
        "declarations": declarations,
        "notes": payload.get("notes") or [],
    }
    return normalized


def resolve_output_path(args: argparse.Namespace, payload: dict[str, Any]) -> Path:
    extension = ".docx" if args.output_format == "word" else ".tex"
    if args.output:
        output_path = Path(args.output)
    else:
        stem = payload["journal"].lower().replace(" ", "-").replace("/", "-")
        output_path = Path.cwd() / f"{stem}-manuscript{extension}"
    if output_path.suffix.lower() != extension:
        output_path = output_path.with_suffix(extension)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def resolve_zotero(args: argparse.Namespace, payload: dict[str, Any]) -> dict[str, Any]:
    if args.zotero_mode == "disabled":
        return {
            "enabled": False,
            "path": None,
            "message": "Zotero integration disabled. References section will remain a placeholder.",
        }

    candidate = args.zotero_bib or payload.get("zotero_bib") or os.getenv("ZOTERO_BIB_PATH")
    if candidate:
        bib_path = Path(candidate).expanduser()
        if bib_path.exists():
            return {
                "enabled": True,
                "path": bib_path,
                "message": f"Zotero bibliography source detected: {bib_path}",
            }

    prompt = (
        "Zotero not configured. Provide --zotero-bib <path-to-exported-bib> or set ZOTERO_BIB_PATH. "
        "Leaving the references area as a placeholder."
    )
    if args.zotero_mode == "required":
        raise SystemExit(
            "Zotero not configured. Provide --zotero-bib <path-to-exported-bib> or set ZOTERO_BIB_PATH before running with --zotero-mode required."
        )
    return {"enabled": False, "path": None, "message": prompt}


def get_affiliation_text(affiliations: list[dict[str, Any]], affiliation_id: int) -> str:
    for item in affiliations:
        if item.get("id") == affiliation_id:
            return str(item.get("text") or "")
    return f"TODO: affiliation {affiliation_id}"


def author_line(authors: list[dict[str, Any]]) -> str:
    return ", ".join(str(author.get("name") or "TODO: Author Name") for author in authors)


def corresponding_author_text(authors: list[dict[str, Any]]) -> str:
    for author in authors:
        if author.get("corresponding"):
            name = author.get("name") or "TODO: Corresponding Author"
            email = author.get("email") or "TODO: corresponding.author@example.com"
            return f"{name} ({email})"
    first = authors[0]
    return f"{first.get('name') or 'TODO: Corresponding Author'} (TODO: corresponding.author@example.com)"


def declaration_rows(declarations: dict[str, str]) -> list[tuple[str, str]]:
    rows = []
    for key, title in DECLARATION_ORDER:
        rows.append((title, declarations.get(key) or f"TODO: Complete {title}."))
    return rows


def add_docx_title_page(document: Document, payload: dict[str, Any]) -> None:
    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run(payload["title"])
    run.bold = True
    run.font.size = Pt(16)

    if payload["running_title"]:
        running = document.add_paragraph()
        running.alignment = WD_ALIGN_PARAGRAPH.CENTER
        running.add_run(f"Running title: {payload['running_title']}")

    meta = document.add_paragraph()
    meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    meta.add_run(f"Journal: {payload['journal']}\nArticle type: {payload['article_type']}")

    authors = document.add_paragraph()
    authors.alignment = WD_ALIGN_PARAGRAPH.CENTER
    authors.add_run(author_line(payload["authors"]))

    for affiliation in payload["affiliations"]:
        para = document.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.add_run(f"{affiliation.get('id')}. {affiliation.get('text')}")

    corresponding = document.add_paragraph()
    corresponding.alignment = WD_ALIGN_PARAGRAPH.CENTER
    corresponding.add_run(f"Corresponding author: {corresponding_author_text(payload['authors'])}")

    if payload["corresponding_author_note"]:
        document.add_paragraph(payload["corresponding_author_note"])

    document.add_page_break()


def add_docx_sections(document: Document, sections: list[dict[str, Any]], level: int = 1) -> None:
    heading_level = min(level, 9)
    for section in sections:
        document.add_heading(section.get("title") or "TODO: Section Title", level=heading_level)
        for paragraph in section.get("paragraphs") or ["TODO: Add section content."]:
            document.add_paragraph(paragraph)
        if section.get("subsections"):
            add_docx_sections(document, section["subsections"], level + 1)


def generate_docx(payload: dict[str, Any], output_path: Path, zotero: dict[str, Any]) -> None:
    document = Document()
    normal = document.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)

    add_docx_title_page(document, payload)

    document.add_heading("Abstract", level=1)
    document.add_paragraph(payload["abstract"])

    document.add_heading("Keywords", level=1)
    document.add_paragraph(", ".join(payload["keywords"]))

    add_docx_sections(document, payload["sections"])

    document.add_heading("Declarations", level=1)
    for title, value in declaration_rows(payload["declarations"]):
        para = document.add_paragraph()
        para.add_run(f"{title}: ").bold = True
        para.add_run(value)

    document.add_heading("References", level=1)
    if zotero["enabled"]:
        document.add_paragraph(
            f"{zotero['message']}. Refresh citations and bibliography from Zotero in Word before submission."
        )
    else:
        document.add_paragraph(zotero["message"])
    document.add_paragraph("TODO: Insert or refresh the final bibliography here.")

    document.save(output_path)


def latex_escape(text: str) -> str:
    replacements = {
        "\\": "\\textbackslash{}",
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
        "~": "\\textasciitilde{}",
        "^": "\\textasciicircum{}",
    }
    result = text
    for source, target in replacements.items():
        result = result.replace(source, target)
    return result


def latex_section_command(level: int) -> str:
    if level <= 1:
        return "section"
    if level == 2:
        return "subsection"
    return "subsubsection"


def build_latex_sections(sections: list[dict[str, Any]], level: int = 1) -> list[str]:
    lines: list[str] = []
    for section in sections:
        command = latex_section_command(level)
        lines.append(f"\\{command}{{{latex_escape(section.get('title') or 'TODO: Section Title')}}}")
        for paragraph in section.get("paragraphs") or ["TODO: Add section content."]:
            lines.append(latex_escape(paragraph))
            lines.append("")
        if section.get("subsections"):
            lines.extend(build_latex_sections(section["subsections"], level + 1))
    return lines


def biblatex_style(reference_style: str) -> str:
    normalized = reference_style.strip().lower()
    return "numeric" if normalized in NUMERIC_REFERENCE_STYLES else "authoryear"


def generate_latex(payload: dict[str, Any], output_path: Path, zotero: dict[str, Any]) -> None:
    lines = [
        "\\documentclass[12pt]{article}",
        "\\usepackage[margin=1in]{geometry}",
        "\\usepackage[hidelinks]{hyperref}",
    ]
    if zotero["enabled"]:
        lines.extend(
            [
                f"\\usepackage[backend=biber,style={biblatex_style(payload['reference_style'])}]{{biblatex}}",
                f"\\addbibresource{{{latex_escape(str(zotero['path']))}}}",
            ]
        )
    lines.extend(
        [
            "",
            "\\begin{document}",
            "\\begin{titlepage}",
            "\\centering",
            f"{{\\LARGE \\textbf{{{latex_escape(payload['title'])}}}\\\\[1em]}}",
        ]
    )
    if payload["running_title"]:
        lines.append(f"{{\\large Running title: {latex_escape(payload['running_title'])}\\\\[0.5em]}}")
    lines.append(f"{{\\large Journal: {latex_escape(payload['journal'])}\\\\}}")
    lines.append(f"{{\\large Article type: {latex_escape(payload['article_type'])}\\\\[1em]}}")
    lines.append(f"{{\\large {latex_escape(author_line(payload['authors']))}\\\\[1em]}}")
    for affiliation in payload["affiliations"]:
        lines.append(
            f"{{\\normalsize {affiliation.get('id')}. {latex_escape(str(affiliation.get('text') or ''))}\\\\}}"
        )
    lines.append("")
    lines.append(
        f"{{\\normalsize Corresponding author: {latex_escape(corresponding_author_text(payload['authors']))}\\\\}}"
    )
    if payload["corresponding_author_note"]:
        lines.append(f"{{\\normalsize {latex_escape(payload['corresponding_author_note'])}\\\\}}")
    lines.extend(["\\vfill", "\\end{titlepage}", ""])
    lines.extend(["\\begin{abstract}", latex_escape(payload["abstract"]), "\\end{abstract}", ""])
    lines.append(f"\\noindent\\textbf{{Keywords:}} {latex_escape(', '.join(payload['keywords']))}")
    lines.append("")
    lines.extend(build_latex_sections(payload["sections"]))
    lines.extend(["\\section*{Declarations}", ""])
    for title, value in declaration_rows(payload["declarations"]):
        lines.append(f"\\subsection*{{{latex_escape(title)}}}")
        lines.append(latex_escape(value))
        lines.append("")
    if zotero["enabled"]:
        lines.append(f"% {latex_escape(zotero['message'])}")
        lines.append("\\printbibliography")
    else:
        lines.extend(
            [
                "\\section*{References}",
                latex_escape(zotero["message"]),
                "",
                "TODO: Insert the final reference list here or configure Zotero before compiling.",
            ]
        )
    lines.extend(["", "\\end{document}", ""])
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main(
    default_style: str | None = None,
    default_journal: str | None = None,
    default_article_type: str | None = None,
) -> int:
    args = parse_args()
    payload = load_payload(Path(args.input))
    normalized = normalize_payload(
        payload,
        output_format=args.output_format,
        default_style=args.style or default_style,
        default_journal=args.journal or default_journal,
        default_article_type=args.article_type or default_article_type,
    )
    output_path = resolve_output_path(args, normalized)
    zotero = resolve_zotero(args, payload)
    if args.output_format == "word":
        generate_docx(normalized, output_path, zotero)
    else:
        generate_latex(normalized, output_path, zotero)
    print(f"Generated {args.output_format} manuscript skeleton: {output_path}")
    print(zotero["message"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
