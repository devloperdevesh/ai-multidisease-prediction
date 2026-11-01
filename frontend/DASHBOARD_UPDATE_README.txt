MEDIPREDICT AI — FRONTEND DASHBOARD UPDATE

What changed
- Reworked the existing React frontend into the pink/white dashboard layout based on the supplied reference.
- Kept the existing Flask API contract (/api/health, /api/diseases, /api/predict/<disease>).
- Kept the existing disease form, prediction result, research methodology components and Vite proxy.
- Dashboard benchmark table uses the recorded test metrics supplied for this project:
  Diabetes: 70.78% accuracy, F1 0.5455, ROC-AUC 0.8130
  Heart: 86.89% accuracy, F1 0.8667, ROC-AUC 0.9513
  CKD: 98.75% accuracy, F1 0.9899, ROC-AUC 1.0000
  Breast cancer: 96.49% accuracy, F1 0.9512, ROC-AUC 0.9960
- 88.23% is the unweighted mean of those four test accuracies.
- The prediction activity panel intentionally shows an empty state because no persistent prediction-history endpoint/database was included in the uploaded frontend archive. It does not invent chart data.
- Summary card shows 41 tests passed based on the latest test result shared in the conversation.

Apply on Windows
1. Extract this ZIP.
2. Copy the contents of its frontend folder into:
   C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\frontend
   Allow overwrite for the updated source files.
3. Keep the backend running in its existing terminal.
4. Open a new PowerShell terminal:
   cd "C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\frontend"
   npm.cmd run build
   npm.cmd run dev -- --host 127.0.0.1
5. Open http://127.0.0.1:5173

Important
- Do not extract this ZIP over the project root; extract/merge its frontend folder into the existing frontend directory only.
- No Python backend/model files were changed.
- This package intentionally excludes node_modules and dist; use the existing Windows node_modules and rebuild.
