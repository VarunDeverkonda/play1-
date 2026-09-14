# Final Hackathon Submission Guide

## 1. What is in this repository

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

The scripts are the deterministic implementation. The `ROTE_CAPTURE.md` files are the exact capture recipes used to turn those implementation steps into canonical saved Plays through the local Rote/Play flow.

## 2. Install Play/Rote

Use the official Play installer on Linux/macOS or inside WSL2 on Windows:

```bash
curl -fsSL https://getrote.dev/playoffs/install.sh | sh
```

Restart the supported harness after installation.

## 3. Warm-up

Start the agent and invoke Play:

```text
$play
```

Complete the low-risk Hello flow if prompted.

## 4. Capture Play 1

From this repository, ask Play to create the outcome:

```text
$play create a reusable deterministic Data Quality Report Play using this repository's plays/01-data-quality-report/ROTE_CAPTURE.md. The reusable input is input_csv. It must create quality_report.json and quality_report.md, never mutate the input, preserve column order, and produce identical output for identical input bytes.
```

If Play offers **Explore and create**, approve it. When the Rote capture workspace is returned, execute the two steps from `ROTE_CAPTURE.md` and verify the JSON output.

When the work is visibly complete, settle the exact capture handle returned by Play:

```text
$play settle <CAPTURE_HANDLE> created the deterministic Data Quality Report with JSON and Markdown outputs and verified the result
```

Then accept the save/release offer appropriate for the hackathon. Record the resulting canonical Play reference/URI in `submission/evidence.md`.

## 5. Capture Play 2

Repeat with:

```text
$play create a reusable deterministic Data Cleaning and Summary Play using this repository's plays/02-data-cleaning-summary/ROTE_CAPTURE.md. The reusable input is input_csv. It must create cleaned_data.csv, cleaning_summary.json, and cleaning_summary.md, never mutate the input, preserve column order, keep the first duplicate, and produce identical output for identical input bytes.
```

Approve Explore and create when offered, execute the three implementation steps, verify the JSON, then settle the returned capture handle:

```text
$play settle <CAPTURE_HANDLE> created the deterministic Data Cleaning and Summary Play and verified the cleaned CSV and summaries
```

Record the resulting canonical Play reference/URI.

## 6. Replay proof

For each saved Play, run it twice with the same `fixtures/sample.csv` input. Verify:

- the same files are produced;
- the JSON is valid;
- the output shape is unchanged;
- the source CSV is unchanged;
- the second run does not require a new exploration/capture;
- the saved Play's exact version is inspected and approved before execution.

## 7. Evidence to collect

Create `submission/evidence.md` after the actual Rote runs. Include:

- canonical Play 1 reference/URI;
- canonical Play 2 reference/URI;
- capture IDs/receipts if shown by Rote;
- screenshot of Play 1 inspection and successful replay;
- screenshot of Play 2 inspection and successful replay;
- screenshot showing deterministic second replay;
- short before/after output examples;
- final GitHub commit containing the verified artifacts/receipts.

Do not commit credentials, tokens, private Rote state, or `.rote-play` state.

## 8. 90-second demo script

**0–15s:** Explain the problem: repeated data tasks waste agent time when the same successful path is rediscovered.

**15–30s:** Show the repository and the two distinct Plays.

**30–50s:** Run/inspect Data Quality Report on `fixtures/sample.csv` and show the JSON/Markdown result.

**50–70s:** Run/inspect Data Cleaning & Summary and show the cleaned CSV plus summary.

**70–85s:** Replay one saved Play with the same input and show that the deterministic path is reused.

**85–90s:** State the value proposition: successful execution becomes reusable muscle memory—faster, cheaper, and more reliable on repeated work.

## 9. Submission checklist

- [ ] Local Rote/Play installed and verified.
- [ ] Hello-world warm-up completed.
- [ ] Play 1 captured through Rote.
- [ ] Play 1 settled into a canonical saved Play.
- [ ] Play 1 replay verified.
- [ ] Play 2 captured through Rote.
- [ ] Play 2 settled into a canonical saved Play.
- [ ] Play 2 replay verified.
- [ ] Both Plays have reusable input(s).
- [ ] Both Plays have stable output shapes.
- [ ] Evidence screenshots collected.
- [ ] Canonical references/receipts added to `submission/evidence.md`.
- [ ] No secrets or private local state committed.
- [ ] Final GitHub repository is public and opens correctly.
