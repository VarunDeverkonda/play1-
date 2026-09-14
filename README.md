# Modiqo Data & AI Hackathon — Rote Plays

Two deterministic, reusable Plays prepared for the Modiqo Online Data & AI Hackathon.

## Plays

1. **Data Quality Report** — inspect a CSV, calculate deterministic quality metrics, and produce a structured JSON + Markdown report.
2. **Data Cleaning & Summary** — normalize a CSV, remove duplicate rows, and produce a cleaned CSV plus deterministic JSON + Markdown summary.

## Repository layout

```text
.
├── README.md
├── SUBMISSION.md
├── LICENSE
├── .gitignore
├── fixtures/
│   └── sample.csv
├── scripts/
│   └── rote_plays.py
├── submission/
│   └── evidence.md
└── plays/
    ├── 01-data-quality-report/
    │   ├── PLAY.md
    │   ├── input-contract.json
    │   └── ROTE_CAPTURE.md
    └── 02-data-cleaning-summary/
        ├── PLAY.md
        ├── input-contract.json
        └── ROTE_CAPTURE.md
```

## Runnable implementation

`python3 scripts/rote_plays.py` contains the deterministic implementation steps used by both Plays. It uses only Python's standard library.

### Play 1

```bash
mkdir -p runs/quality
python3 scripts/rote_plays.py quality-scan fixtures/sample.csv runs/quality/quality_report.json
python3 scripts/rote_plays.py quality-render runs/quality/quality_report.json runs/quality/quality_report.md
```

### Play 2

```bash
mkdir -p runs/cleaning
python3 scripts/rote_plays.py clean-csv fixtures/sample.csv runs/cleaning/cleaned_data.csv
python3 scripts/rote_plays.py clean-summary fixtures/sample.csv runs/cleaning/cleaned_data.csv runs/cleaning/cleaning_summary.json
python3 scripts/rote_plays.py clean-render runs/cleaning/cleaning_summary.json runs/cleaning/cleaning_summary.md
```

## Turning the implementations into actual Rote Plays

The `ROTE_CAPTURE.md` files are capture recipes rather than invented Rote manifest syntax. Use the local Modiqo Play/Rote flow to capture these successful steps, verify the result, and settle the capture into a canonical saved Play. This preserves Rote as the source of truth for the actual saved Play artifact.

See [`SUBMISSION.md`](SUBMISSION.md) for the exact installation, capture, settle, replay, evidence, and final-submission checklist.

## Determinism

- No random sampling.
- Input is never mutated.
- Source column order is preserved.
- Duplicate handling is deterministic.
- Output JSON/Markdown does not embed machine-specific input/output paths.
- Identical input bytes produce the same logical report.
