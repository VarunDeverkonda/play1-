# Rote capture recipe — Data Cleaning & Summary

This is the capture-ready recipe for the second actual Rote Play. It uses three effect-bearing steps: cleaning, structured summary, and Markdown rendering.

## Outcome

Given `input_csv`, create a cleaned CSV plus deterministic JSON and Markdown summaries without mutating the input.

## Exact steps

Run from repository root:

```bash
mkdir -p runs/cleaning
python3 scripts/rote_plays.py clean-csv "$INPUT_CSV" runs/cleaning/cleaned_data.csv
python3 scripts/rote_plays.py clean-summary "$INPUT_CSV" runs/cleaning/cleaned_data.csv runs/cleaning/cleaning_summary.json
python3 scripts/rote_plays.py clean-render runs/cleaning/cleaning_summary.json runs/cleaning/cleaning_summary.md
```

For the first capture, use:

```text
INPUT_CSV=fixtures/sample.csv
```

## Verification

```bash
python3 -m json.tool runs/cleaning/cleaning_summary.json >/dev/null
```

Confirm the original CSV is unchanged and the cleaned CSV has duplicates removed and surrounding whitespace normalized.

## Suggested Play description

> Clean a CSV deterministically by trimming string cells, treating empty strings as missing, removing exact duplicate rows while keeping the first occurrence, and producing a structured JSON and Markdown summary. Never mutate the input or reorder columns/rows unexpectedly.

## Save criteria

The captured Rote trajectory should contain:

1. input binding for `input_csv`;
2. cleaned CSV creation;
3. summary JSON creation;
4. Markdown summary creation;
5. successful verification;
6. stable output shape.

After successful capture, use Play's normal `settle` flow so Rote/Play creates the canonical saved Play from the verified capture.
