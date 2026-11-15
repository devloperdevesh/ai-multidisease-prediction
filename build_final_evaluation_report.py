from pathlib import Path
import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

root = Path(".")
results = root / "reports" / "results"

comparison = pd.read_csv(results / "model_comparison.csv")
cv = pd.read_csv(results / "repeated_cv_audit.csv")

with open(results / "best_models.json", encoding="utf-8-sig") as f:
    best = json.load(f)

if len(comparison) != 24:
    raise SystemExit(f"Expected 24 model rows, found {len(comparison)}")

if comparison["disease"].nunique() != 4:
    raise SystemExit("Expected results for exactly 4 diseases")

if comparison.groupby("disease")["model"].nunique().min() != 6:
    raise SystemExit("At least one disease does not have 6 algorithms")

output = results / "medipredict_model_evaluation.xlsx"

with pd.ExcelWriter(output, engine="openpyxl") as writer:
    comparison.to_excel(writer, sheet_name="All 24 Experiments", index=False)
    cv.to_excel(writer, sheet_name="Cross Validation", index=False)

    # Preserve the exact selected-model JSON as auditable source data.
    json_rows = [
        {"JSON source": "best_models.json", "Content": json.dumps(best, indent=2, ensure_ascii=False)}
    ]
    pd.DataFrame(json_rows).to_excel(
        writer, sheet_name="Best Models Source", index=False
    )

wb = load_workbook(output)

for ws in wb.worksheets:
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="243B53")
        cell.alignment = Alignment(wrap_text=True, vertical="center")

    for column in ws.columns:
        letter = get_column_letter(column[0].column)
        max_len = max(
            (len(str(cell.value)) for cell in column if cell.value is not None),
            default=10
        )
        ws.column_dimensions[letter].width = min(max(max_len + 2, 14), 42)

wb.save(output)

print("Excel report:", output)
print("All model rows:", len(comparison))
print("Disease groups:", comparison["disease"].nunique())
print("Algorithms per disease:")
print(comparison.groupby("disease")["model"].nunique().to_string())
print("Cross-validation rows:", len(cv))
print("Selected best-model JSON preserved.")
