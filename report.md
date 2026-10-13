# Project Report: Security Event Classification

## 1. Objective
Build a small, understandable dataset and workflow for triaging security events into Normal, Suspicious, or Potentially Malicious categories.

## 2. Scope
The project contains 30 fictional events covering authentication, endpoint, network, data access, email, web, and privilege activity. Each row includes context, severity, a provisional classification, and a reason.

## 3. Method
Classification is based on the described event plus contextual signals. Known, approved activity is generally Normal; anomalies needing validation are Suspicious; stronger patterns such as likely command-and-control communication, impossible travel, unexplained external mailbox forwarding, mass file changes, or possible exfiltration are Potentially Malicious.

## 4. Tools
- Excel or Google Sheets for filtering, reviewing, and summarizing the dataset.
- Python 3 for an optional simple keyword-based starter script.
- GitHub for versioning and presenting project files.

## 5. Results
The curated dataset includes 30 events across three labels. The classifications are illustrative triage judgments, not ground truth. Analysts should update them when corroborating evidence becomes available.

## 6. Quality checks
- Every event has a classification and a reason.
- Severity is separate from classification.
- The classification does not claim certainty where context is incomplete.
- Example IPs use documentation-only ranges.

## 7. Conclusion
The exercise practices structured triage, evidence-based reasoning, and clear documentation. A realistic next step is to add fields for analyst confidence, investigation status, supporting log references, and final disposition.

## 8. Limitations
The sample is synthetic, small, and not representative of all enterprise activity. The keyword script is intentionally simplistic and can produce false positives and false negatives. It must not be used as a production security control.
