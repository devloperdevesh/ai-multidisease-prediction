# MediPredict AI — Frontend navigation and UX update

This update is based on the supplied `frontend.zip` and the existing React + Vite + Flask architecture. It does not replace the Python backend, trained model artifacts, datasets, or training reports.

## What changed

- Sidebar navigation now opens distinct views: Dashboard, Predict Disease, Model Analytics, Reports, Dataset & Research, and About.
- Fixed the previous navigation behaviour where Predict Disease and Model Analytics only scrolled the overview page, making the sidebar appear non-functional.
- Predict Disease now has a dedicated module-selection workspace. Each module opens the existing disease-specific form and calls the existing Flask prediction endpoint.
- Model Analytics now has its own page with recorded held-out test metrics (accuracy, precision, recall, F1-score, ROC-AUC).
- Reports now provides a CSV export of the recorded evaluation summary and clearly states that individual prediction history is not persisted in this version.
- The disease assessment form's back action returns to Predict Disease.
- Added a custom MediPredict heart/ECG favicon and refined page styles, focus states, responsive layouts, and empty-state messaging.

## Run on Windows PowerShell

Terminal 1 — backend (keep open):

```powershell
cd "C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
.\.venv\Scripts\Activate.ps1
$env:PYTHONPATH = (Get-Location).Path
python -m app.api.server
```

Terminal 2 — frontend:

```powershell
cd "C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\frontend"
npm.cmd install
npm.cmd run build
npm.cmd run dev -- --host 127.0.0.1
```

Open `http://127.0.0.1:5173/`.

## Data integrity notes

- Evaluation metrics shown in the UI are the recorded project training results; they are not clinical validation.
- Prediction counts, unique-user counts, and patient activity charts are intentionally not fabricated.
- The current profile entry is a local display profile, not secure authentication.
- Prediction history is not persisted by this frontend update. Reports clearly communicate that limitation.
- CKD's recorded ROC-AUC of 1.0000 should receive further leakage and external-validation review before strong claims are made.
