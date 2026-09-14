# Play 2 — Data Cleaning & Summary

## Outcome

Given a CSV file, create a cleaned copy and a deterministic summary.

## Input

- `input_csv`: path to the CSV file.

## Workflow

1. Read the CSV.
2. Trim leading/trailing whitespace from string cells.
3. Treat empty strings as missing values.
4. Remove exact duplicate rows, keeping the first occurrence.
5. For numeric columns, preserve numeric values and do not invent replacements.
6. For text columns, leave non-missing values unchanged after trimming.
7. Create a cleaned CSV.
8. Generate a summary containing:
   - original row count;
   - cleaned row count;
   - duplicates removed;
   - missing-value count before cleaning;
   - missing-value count after cleaning;
   - column names.
9. Write the summary as stable JSON and Markdown.

## Determinism rules

- Keep original column order.
- Keep first occurrence when duplicates exist.
- Never randomly sample or reorder rows.
- Use fixed UTF-8 output.
- The same input bytes must produce the same cleaned CSV and summary.

## Outputs

- `cleaned_data.csv`
- `cleaning_summary.json`
- `cleaning_summary.md`

## Success criteria

The Play succeeds only when the cleaned CSV and both summary files are produced and the JSON summary is valid.
