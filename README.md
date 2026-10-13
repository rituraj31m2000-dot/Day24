# Security Event Classification

**Level:** Beginner | **Task:** Day 24 | **Track:** Cyber Security

## Project overview
This project demonstrates basic security-event triage by categorizing synthetic log events as **Normal**, **Suspicious**, or **Potentially Malicious** and recording a concise reason for each decision.

## Files
- `security_events_classified.csv` — 30 sample events with classifications and reasons; suitable for Excel or Google Sheets.
- `security_events_raw.csv` — the same event inputs without labels, for running the starter script.
- `classify_events.py` — a simple rule-based educational classifier.
- `linkedin_post.md` — draft post for sharing the project.
- `report.md` — short project report and methodology.

## How to use the dataset
1. Open `security_events_classified.csv` in Excel or import it into Google Sheets.
2. Filter by `classification` or `severity`.
3. Review the `classification_reason` column and adjust labels if more evidence changes the assessment.
4. Save your own copy before editing.

## Run the Python starter
Requires Python 3.9+ and no third-party packages.

```bash
python classify_events.py
```

The script reads `security_events_raw.csv` and writes `security_events_classified_output.csv`.

> Important: the script is intentionally a basic keyword/rule demonstration. Its output may differ from the curated labels in `security_events_classified.csv`. Do not use it to make real security decisions.

## Classification guidance
- **Normal:** Activity is consistent with an approved baseline or documented business process.
- **Suspicious:** Activity is unusual or needs verification, but evidence is insufficient to call it malicious.
- **Potentially Malicious:** Multiple strong indicators or a high-risk pattern warrant urgent investigation. This label is not proof of compromise.

## Suggested workflow
1. Review the alert and confirm timestamp, source, account/asset, and severity.
2. Compare with the expected baseline, change tickets, and known maintenance.
3. Correlate with identity, endpoint, network, and email logs.
4. Assign a provisional label and write the evidence-based reason.
5. Escalate high-risk events using the organization's incident response process.

## Limitations and ethics
All records are synthetic and use documentation-only IP ranges (192.0.2.0/24, 198.51.100.0/24, and 203.0.113.0/24). Names and events are fictional. This is a learning exercise, not a validated detection product. Never upload real logs containing personal data, credentials, tokens, or confidential company information to a public repository.

