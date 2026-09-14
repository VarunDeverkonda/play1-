#!/usr/bin/env python3
"""Deterministic implementation steps used by the two hackathon Plays.

No third-party packages are required. Rote can capture these as shell/Python
steps and replay them with the same input contract.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable


def read_csv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("CSV is empty")
    header = rows[0]
    if not header or any(not h for h in header):
        raise ValueError("CSV must have a non-empty header")
    width = len(header)
    data = []
    for n, row in enumerate(rows[1:], start=2):
        if len(row) != width:
            raise ValueError(f"Row {n} has {len(row)} fields; expected {width}")
        data.append(row)
    return header, data


def is_number(value: str) -> bool:
    if value == "":
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False


def observed_type(values: Iterable[str]) -> str:
    vals = [v for v in values if v != ""]
    if not vals:
        return "unknown"
    if all(is_number(v) for v in vals):
        return "number"
    return "string"


def quality_scan(input_csv: Path, output_json: Path) -> None:
    header, rows = read_csv(input_csv)
    row_count = len(rows)
    columns = []
    duplicate_columns = []
    for i, name in enumerate(header):
        values = [row[i] for row in rows]
        missing = sum(v == "" for v in values)
        distinct = len(set(values))
        info = {
            "name": name,
            "observed_type": observed_type(values),
            "missing_count": missing,
            "missing_percent": round((missing / row_count * 100) if row_count else 0.0, 2),
            "distinct_count": distinct,
        }
        columns.append(info)
        if distinct < row_count:
            duplicate_columns.append(name)

    duplicate_rows = row_count - len({tuple(row) for row in rows})
    report = {
        "input": str(input_csv),
        "row_count": row_count,
        "column_count": len(header),
        "columns": columns,
        "duplicate_row_count": duplicate_rows,
        "columns_with_duplicate_values": sorted(duplicate_columns),
    }
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def render_quality(input_json: Path, output_md: Path) -> None:
    report = json.loads(input_json.read_text(encoding="utf-8"))
    lines = [
        "# Data Quality Report",
        "",
        f"- Rows: **{report['row_count']}**",
        f"- Columns: **{report['column_count']}**",
        f"- Duplicate rows: **{report['duplicate_row_count']}**",
        "",
        "## Columns",
        "",
        "| Column | Type | Missing | Missing % | Distinct |",
        "|---|---|---:|---:|---:|",
    ]
    for c in report["columns"]:
        lines.append(f"| {c['name']} | {c['observed_type']} | {c['missing_count']} | {c['missing_percent']:.2f}% | {c['distinct_count']} |")
    lines += ["", "## Duplicate-value columns", ""]
    dupes = report["columns_with_duplicate_values"]
    lines.append("None" if not dupes else "\n".join(f"- `{x}`" for x in dupes))
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def clean_csv(input_csv: Path, output_csv: Path) -> None:
    header, rows = read_csv(input_csv)
    normalized = [[cell.strip() for cell in row] for row in rows]
    seen = set()
    kept = []
    for row in normalized:
        key = tuple(row)
        if key not in seen:
            seen.add(key)
            kept.append(row)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(kept)


def missing_count(rows) -> int:
    return sum(cell == "" for row in rows for cell in row)


def cleaning_summary(input_csv: Path, cleaned_csv: Path, output_json: Path) -> None:
    header_before, rows_before = read_csv(input_csv)
    header_after, rows_after = read_csv(cleaned_csv)
    if header_before != header_after:
        raise ValueError("Cleaned CSV changed the column order/header")
    report = {
        "input": str(input_csv),
        "output": str(cleaned_csv),
        "original_row_count": len(rows_before),
        "cleaned_row_count": len(rows_after),
        "duplicates_removed": len(rows_before) - len(rows_after),
        "missing_values_before": missing_count(rows_before),
        "missing_values_after": missing_count(rows_after),
        "columns": header_after,
    }
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def render_cleaning(input_json: Path, output_md: Path) -> None:
    report = json.loads(input_json.read_text(encoding="utf-8"))
    lines = [
        "# Data Cleaning Summary",
        "",
        f"- Original rows: **{report['original_row_count']}**",
        f"- Cleaned rows: **{report['cleaned_row_count']}**",
        f"- Duplicates removed: **{report['duplicates_removed']}**",
        f"- Missing values before: **{report['missing_values_before']}**",
        f"- Missing values after: **{report['missing_values_after']}**",
        "",
        "## Columns",
        "",
    ]
    lines.extend(f"- `{c}`" for c in report["columns"])
    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)

    q = sub.add_parser("quality-scan")
    q.add_argument("input_csv", type=Path)
    q.add_argument("output_json", type=Path)

    qr = sub.add_parser("quality-render")
    qr.add_argument("input_json", type=Path)
    qr.add_argument("output_md", type=Path)

    c = sub.add_parser("clean-csv")
    c.add_argument("input_csv", type=Path)
    c.add_argument("output_csv", type=Path)

    s = sub.add_parser("clean-summary")
    s.add_argument("input_csv", type=Path)
    s.add_argument("cleaned_csv", type=Path)
    s.add_argument("output_json", type=Path)

    sr = sub.add_parser("clean-render")
    sr.add_argument("input_json", type=Path)
    sr.add_argument("output_md", type=Path)

    args = p.parse_args()
    if args.command == "quality-scan":
        quality_scan(args.input_csv, args.output_json)
    elif args.command == "quality-render":
        render_quality(args.input_json, args.output_md)
    elif args.command == "clean-csv":
        clean_csv(args.input_csv, args.output_csv)
    elif args.command == "clean-summary":
        cleaning_summary(args.input_csv, args.cleaned_csv, args.output_json)
    else:
        render_cleaning(args.input_json, args.output_md)


if __name__ == "__main__":
    main()
