from pathlib import Path
import pandas as pd

readme = Path("README.md").read_text(encoding="utf-8")
report = Path("docs/PROJECT_REPORT.md").read_text(encoding="utf-8")
evidence = Path("docs/MODEL_EVALUATION_EVIDENCE.md").read_text(encoding="utf-8")
status = Path("docs/IMPLEMENTATION_STATUS.md").read_text(encoding="utf-8")

checks = {
    "README screenshot gallery": "Application preview" in readme,
    "README academic documentation links": "PROJECT_REPORT.md" in readme,
    "Academic SDG section": "Sustainable Development Goal" in report,
    "Academic literature survey": "Literature survey" in report,
    "Academic research gap": "Research gap" in report,
    "Academic methodology": "methodology" in report.lower(),
    "Academic references": "References" in report,
    "24-model evidence section": "24-Experiment" in evidence,
    "Implementation status document": "Evidence confirmed" in status,
}

print("\n===== DOCUMENTATION CONTENT CHECK =====")
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL"), "-", name)

if not all(checks.values()):
    raise SystemExit("A required documentation section is missing.")

comparison = pd.read_csv("reports/results/model_comparison.csv")
cv = pd.read_csv("reports/results/repeated_cv_audit.csv")

assert len(comparison) == 24
assert len(cv) == 4

print("\nModel experiment records:", len(comparison))
print("Cross-validation records:", len(cv))
print("Documentation content checks passed.")
