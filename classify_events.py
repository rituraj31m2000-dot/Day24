#!/usr/bin/env python3
"""
Rule-based starter classifier for the synthetic training dataset.
This is an educational example, not a production detection system.
"""
import csv
from pathlib import Path

INPUT = Path(__file__).with_name("security_events_raw.csv")
OUTPUT = Path(__file__).with_name("security_events_classified_output.csv")

MALICIOUS_TERMS = (
    "command-and-control", "impossible-travel", "after account disabled",
    "mailbox forwarding rule", "ransomware", "data exfiltration",
    "personal file-sharing", "mfa denied repeatedly", "api token created"
)
SUSPICIOUS_TERMS = (
    "failed logins", "new country", "newly seen domain", "large download",
    "unsigned executable", "administrator role", "suspicious attachment",
    "encoded command", "typo-squatted", "service account login",
    "unfamiliar device", "agent stopped", "blocked requests"
)

def classify(description: str, context: str, severity: str) -> tuple[str, str]:
    text = f"{description} {context}".lower()
    if any(term in text for term in MALICIOUS_TERMS):
        return "Potentially Malicious", "Matched a high-risk training rule; validate with additional evidence."
    if any(term in text for term in SUSPICIOUS_TERMS) or severity.strip().lower() == "high":
        return "Suspicious", "Matched a review rule; investigate context before concluding."
    return "Normal", "No high-risk training rule matched; confirm the activity is expected."

def main():
    if not INPUT.exists():
        raise SystemExit(f"Input file not found: {INPUT.name}")
    with INPUT.open(newline="", encoding="utf-8") as src:
        rows = list(csv.DictReader(src))
    fields = list(rows[0].keys()) + ["classification", "classification_reason"] if rows else []
    with OUTPUT.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            label, reason = classify(row.get("event_description", ""),
                                     row.get("context", ""),
                                     row.get("severity", ""))
            row["classification"] = label
            row["classification_reason"] = reason
            writer.writerow(row)
    print(f"Wrote {len(rows)} rows to {OUTPUT.name}")

if __name__ == "__main__":
    main()
