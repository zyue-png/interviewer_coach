#!/usr/bin/env python3
"""Extract readable text from PDF, DOCX, TXT, or Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree


def extract_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
    root = ElementTree.fromstring(xml)
    paragraphs = []
    for paragraph in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
        parts = [node.text or "" for node in paragraph.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t")]
        text = "".join(parts).strip()
        if text:
            paragraphs.append(text)
    return "\n".join(paragraphs)


def extract_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("处理 PDF 需要安装 pypdf：python3 -m pip install pypdf") from exc
    pages = []
    for page in PdfReader(str(path)).pages:
        pages.append(page.extract_text() or "")
    return "\n\n".join(pages)


def clean(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + ("\n" if text.strip() else "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract resume text for interview-coach.")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, help="写入文件；不提供时输出到 stdout")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"找不到输入文件：{args.input}")
    suffix = args.input.suffix.lower()
    if suffix == ".docx":
        text = extract_docx(args.input)
    elif suffix == ".pdf":
        text = extract_pdf(args.input)
    elif suffix in {".txt", ".md", ".markdown"}:
        text = args.input.read_text(encoding="utf-8")
    else:
        parser.error("仅支持 PDF、DOCX、TXT 和 Markdown 文件")
    text = clean(text)
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
