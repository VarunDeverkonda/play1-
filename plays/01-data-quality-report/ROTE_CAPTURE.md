# Rote capture recipe — Data Quality Report

This file is the capture-ready recipe for the actual Rote Play. It deliberately uses two effect-bearing steps so the captured trajectory demonstrates reusable execution rather than a single monolithic command.

## Outcome

Given `input_csv`, create `quality_report.json` and `quality_report.md` without modifying the input.

## Exact steps

Run from repository root:

```bash
mkdir -p runs/quality
python3 scripts/rote_plays.py quality-scan "$INPUT_CSV" runs/quality/quality_report.json
python3 scripts/rote_plays.py quality-render runs/quality/quality_report.json runs/quality/quality_report.md
```

For the first capture, use:

```text
INPUT_CSV=fixtures/sample.csv
```

## Verification

```bash
python3 -m json.tool runs/quality/quality_report.json >/dev/null
```

Then replay the saved Play with the same fixture and confirm the output files are byte-for-byte stable.

## Suggested Play description

> Analyze a CSV deterministically and produce a reusable data-quality JSON report plus Markdown report. Preserve source order, do not mutate the input, and use fixed rules for missing values, types, duplicates, and percentages.

## Save criteria

The captured Rote trajectory should contain:

1. input binding for `input_csv`;
2. JSON report generation;
3. Markdown report generation;
4. successful verification;
5. stable output paths and shape.

After successful capture, use Play's normal `settle` flow so Rote/Play creates the canonical saved Play from the verified capture rather than treating this Markdown file as the Play artifact itself.
