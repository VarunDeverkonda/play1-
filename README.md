# Modiqo Data & AI Hackathon — Rote Plays

Two deterministic, reusable Plays prepared for the Modiqo Online Data & AI Hackathon.

## Plays

1. **Data Quality Report** — inspect a CSV, calculate deterministic quality metrics, and produce a structured report.
2. **Data Cleaning & Summary** — normalize a CSV, remove duplicate rows, handle missing values using declared rules, and produce a deterministic summary.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── .gitignore
├── plays/
│   ├── 01-data-quality-report/
│   │   ├── PLAY.md
│   │   └── input-contract.json
│   └── 02-data-cleaning-summary/
│       ├── PLAY.md
│       └── input-contract.json
└── fixtures/
    └── sample.csv
```

## Important

The two `PLAY.md` files describe the exact workflow, inputs, outputs, and deterministic rules. They are intentionally provider-neutral so they can be crystallized/exported through the installed Modiqo Rote/Play authoring flow without inventing an unsupported manifest format.

For the hackathon submission, run each workflow through Rote, verify the replay, then commit the resulting canonical Play artifacts/receipts to this repository.

## Hackathon requirements covered

- At least two distinct functional Plays.
- Reusable deterministic workflow definitions.
- Explicit inputs and outputs.
- Test fixture for repeatable verification.
- Documentation suitable for the submission repository.
