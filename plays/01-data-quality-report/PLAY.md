# Play 1 — Data Quality Report

## Outcome

Given a CSV file, produce a deterministic data-quality report without modifying the source file.

## Input

- `input_csv`: path to the CSV file.

## Workflow

1. Read the CSV as tabular data.
2. Record row count and column count.
3. For every column:
   - determine the observed data type;
   - count missing/blank values;
   - count distinct values;
   - calculate missing percentage.
4. Count fully duplicated rows.
5. Identify columns containing duplicate values.
6. Produce a stable JSON report with columns sorted in their original order.
7. Produce a human-readable Markdown report from the same JSON result.
8. Leave the source CSV unchanged.

## Determinism rules

- Do not sample rows.
- Preserve source column order.
- Use fixed rounding: percentages to 2 decimal places.
- Sort generated lists lexicographically unless the source order is explicitly required.
- The same input bytes must produce the same report.

## Outputs

- `quality_report.json`
- `quality_report.md`

## Success criteria

The Play succeeds only when both output files are generated and the JSON report can be parsed successfully.
