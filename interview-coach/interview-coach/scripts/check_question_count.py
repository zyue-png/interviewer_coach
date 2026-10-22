#!/usr/bin/env python3
"""Check whether a generated interview report contains 8–12 questions."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


QUESTION_HEADING = re.compile(r"^\s*#{1,6}\s*Q\s*\d+[.、:：)]", re.I)
QUESTION_LABEL = re.compile(r"^\s*(?:问题|题目)\s*\d+[.、:：)]")
NUMBERED_QUESTION = re.compile(r"^\d+[.、)]\s+\S+")


def count_questions(text: str) -> int:
    count = 0
    in_question_section = False
    for line in text.splitlines():
        if re.match(r"^##\s+", line):
            in_question_section = bool(re.search(r"面试问题|问题", line))
            continue
        if QUESTION_HEADING.match(line) or QUESTION_LABEL.match(line):
            count += 1
        elif in_question_section and NUMBERED_QUESTION.match(line):
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Check interview question count.")
    parser.add_argument("report", type=Path, help="生成的 Markdown 或文本报告")
    parser.add_argument("--min", type=int, default=8)
    parser.add_argument("--max", type=int, default=12)
    args = parser.parse_args()
    text = args.report.read_text(encoding="utf-8")
    count = count_questions(text)
    print(f"question_count={count}; expected={args.min}-{args.max}")
    if not args.min <= count <= args.max:
        print("FAIL: question count is outside the accepted range.", file=sys.stderr)
        return 1
    print("PASS: question count is within the accepted range.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
