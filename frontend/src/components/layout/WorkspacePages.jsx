import {
  Activity, ArrowRight, BarChart3, Download, FileText, FlaskConical,
  ShieldCheck, Database, Target, BrainCircuit, CircleHelp, Trash2
} from "lucide-react";

const DISEASE_LABELS = {
  diabetes: "Diabetes",
  heart: "Heart Disease",
  ckd: "Chronic Kidney Disease",
  breast_cancer: "Breast Cancer",
};

const DATASETS = [
  { name: "Pima Indians Diabetes", records: 768, features: 8, target: "Outcome", split: "614 / 154", tone: "blue" },
  { name: "UCI Heart Disease", records: 303, features: 13, target: "num ? binary", split: "242 / 61", tone: "rose" },
  { name: "UCI Chronic Kidney Disease", records: 400, features: 24, target: "class", split: "320 / 80", tone: "orange" },
  { name: "Breast Cancer Wisconsin Diagnostic", records: 569, features: 30, target: "Diagnosis", split: "455 / 114", tone: "purple" },
];

function PageHeader({ eyebrow, title, description, icon: Icon = Activity }) {
  return <div className="workspace-page-header"><span className="dashboard-eyebrow">{eyebrow}</span><div className="workspace-page-title"><span><Icon size={23}/></span><div><h1>{title}</h1><p>{description}</p></div></div></div>;
}

export function PredictWorkspace({ diseases, apiDiseases, onSelectDisease }) {
  return <main className="workspace-page">
    <PageHeader eyebrow="ASSESSMENT WORKSPACE" title="Choose a disease module" description="Select a module to enter its required features and run the connected research model." icon={Activity}/>
    <div className="predict-guidance"><ShieldCheck size={18}/><span><strong>Before you begin</strong> Use values from appropriate records. Do not enter guessed values. This research prototype is not a diagnostic tool.</span></div>
    <div className="workspace-module-grid">{diseases.map((d) => {
      const ready = apiDiseases.some((item) => item.id === d.id);
      const meta = DATASETS.find((x) => x.name.toLowerCase().includes(d.id === "breast_cancer" ? "breast" : d.id === "heart" ? "heart" : d.id === "ckd" ? "kidney" : "diabetes"));
      return <article className={`workspace-module-card ${d.accent || "blue"}`} key={d.id}>
        <div className="workspace-module-top"><span className="workspace-module-icon"><Activity size={23}/></span><span className={`module-status ${ready ? "ready" : ""}`}><i/>{ready ? "API schema available" : "API unavailable"}</span></div>
        <h2>{d.label}</h2><p>{d.description}</p>
        <div className="workspace-module-meta"><span><Database size={14}/>{meta?.name || "Public benchmark dataset"}</span><span>{apiDiseases.find((x) => x.id === d.id)?.feature_count ?? d.fields} required features</span></div>
        <button disabled={!ready} onClick={() => onSelectDisease(d.id)}>Open assessment <ArrowRight size={17}/></button>
      </article>;
    })}</div>
    <div className="workspace-help"><CircleHelp size={18}/><div><strong>Why are different fields shown for each disease?</strong><p>Each model uses a disease-specific public dataset and feature schema.</p></div></div>
  </main>;
}

function getSelectedRows(metrics) {
  const selected = metrics?.selected;
  if (!selected || typeof selected !== "object") return [];

  return Object.entries(selected).map(([id, item]) => ({
    id,
    disease: DISEASE_LABELS[id] || id,
    model: String(item.model || "?").replaceAll("_", " "),
    accuracy: Number(item.test_accuracy) * 100,
    precision: Number(item.test_precision) * 100,
    recall: Number(item.test_recall) * 100,
    f1: Number(item.test_f1) * 100,
    auc: Number(item.test_roc_auc),
  })).filter((row) => [row.accuracy, row.precision, row.recall, row.f1, row.auc].every(Number.isFinite));
}


const MODEL_LABELS = {
  logistic_regression: "Logistic Regression",
  decision_tree: "Decision Tree",
  random_forest: "Random Forest",
  svm: "SVM",
  knn: "KNN",
  xgboost: "XGBoost",
};

function getExperimentRows(experiments) {
  return experiments.map((item) => {
    const m = item.test_metrics || {};
    return {
      disease: item.disease,
      diseaseLabel: DISEASE_LABELS[item.disease] || item.disease,
      model: item.model,
      modelLabel: MODEL_LABELS[item.model] || String(item.model || "?").replaceAll("_", " "),
      accuracy: Number(m.accuracy) * 100,
      precision: Number(m.precision) * 100,
      recall: Number(m.recall) * 100,
      f1: Number(m.f1) * 100,
      auc: Number(m.roc_auc),
      trainingSeconds: Number(item.training_seconds),
    };
  }).filter((item) =>
    [item.accuracy, item.precision, item.recall, item.f1, item.auc].every(Number.isFinite)
  );
}

function MetricBar({ label, value, color }) {
  const safeValue = Math.max(0, Math.min(100, value));
  return <div className="analytics-bar-row">
    <span className="analytics-bar-label">{label}</span>
    <div className="analytics-bar-track">
      <div className="analytics-bar-fill" style={{ width: `${safeValue}%`, background: color }} />
    </div>
    <strong>{value.toFixed(1)}%</strong>
  </div>;
}


function MetricRing({ label, value, color }) {
  const safeValue = Number.isFinite(Number(value))
    ? Math.min(100, Math.max(0, Number(value)))
    : 0;
  const circumference = 213.63;
  const offset = circumference - (safeValue / 100) * circumference;

  return (
    <div className="analytics-ring-item">
      <div className="analytics-ring" style={{ "--ring-color": color }}>
        <svg viewBox="0 0 88 88" role="img" aria-label={`${label}: ${safeValue.toFixed(1)} percent`}>
          <circle className="analytics-ring-track" cx="44" cy="44" r="34" />
          <circle
            className="analytics-ring-progress"
            cx="44"
            cy="44"
            r="34"
            strokeDasharray={circumference}
            strokeDashoffset={offset}
          />
        </svg>
        <strong>{safeValue.toFixed(1)}<small>%</small></strong>
      </div>
      <span>{label}</span>
    </div>
  );
}

export function AnalyticsWorkspace({ metrics }) {
  const rows = getSelectedRows(metrics);
  const experiments = Array.isArray(metrics?.results) ? metrics.results : [];
  const experimentRows = getExperimentRows(experiments);

  const average = rows.length
    ? (rows.reduce((sum, row) => sum + row.accuracy, 0) / rows.length).toFixed(2)
    : "?";

  const metricSeries = [
    { key: "accuracy", label: "Accuracy", color: "#6488e8" },
    { key: "precision", label: "Precision", color: "#e66c9b" },
    { key: "recall", label: "Recall", color: "#45a98a" },
    { key: "f1", label: "F1-score", color: "#a17bd2" },
  ];

  const diseaseGroups = Object.keys(DISEASE_LABELS).map((id) => ({
    id,
    label: DISEASE_LABELS[id],
    models: experimentRows.filter((item) => item.disease === id),
  })).filter((group) => group.models.length);

  return <main className="workspace-page">
    <PageHeader
      eyebrow="MODEL EVALUATION"
      title="Model analytics"
      description="Explore recorded model performance across disease datasets and training experiments. These results are not clinical validation."
      icon={BarChart3}
    />

    {!metrics && <div className="predict-guidance">Loading model evaluation data...</div>}

    {metrics && rows.length === 0 && (
      <div className="report-empty panel">
        <h2>Evaluation data unavailable</h2>
        <p>The selected-model metrics could not be read from the training results.</p>
      </div>
    )}

    {rows.length > 0 && <>
      <div className="analytics-kpis">
        <article>
          <Target />
          <strong>{average}%</strong>
          <span>Mean selected-model accuracy</span>
        </article>
        <article>
          <BrainCircuit />
          <strong>{experiments.length}</strong>
          <span>Recorded training experiments</span>
        </article>
        <article>
          <Database />
          <strong>{new Set(experiments.map((item) => item.disease)).size}</strong>
          <span>Disease datasets represented</span>
        </article>
      </div>

      <section className="panel analytics-chart-panel analytics-radial-panel">
        <div className="panel-heading">
          <div className="panel-heading-icon pink"><Target size={21} /></div>
          <div>
            <h2>Disease-wise model performance</h2>
            <p>Selected models ? held-out test metrics</p>
          </div>
          <span className="panel-meta">4 PERFORMANCE METRICS</span>
        </div>

        <div className="analytics-radial-legend">
          {metricSeries.map((metric) => (
            <span key={metric.key}>
              <i style={{ background: metric.color }} />
              {metric.label}
            </span>
          ))}
        </div>

        <div className="analytics-radial-grid">
          {rows.map((row) => (
            <article className="analytics-radial-card" key={row.id}>
              <div className="analytics-radial-card-head">
                <div className="analytics-disease-symbol"><Activity size={19} /></div>
                <div className="analytics-radial-title">
                  <h3>{row.disease}</h3>
                  <span>Selected model performance</span>
                </div>
                <span className="analytics-model-chip">{row.model}</span>
              </div>

              <div className="analytics-rings-grid">
                {metricSeries.map((metric) => (
                  <MetricRing
                    key={metric.key}
                    label={metric.label}
                    value={row[metric.key]}
                    color={metric.color}
                  />
                ))}
              </div>

              <div className="analytics-card-foot">
                <span><i /> Recorded test-split results</span>
                <strong>{row.accuracy.toFixed(1)}% accuracy</strong>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="panel analytics-chart-panel">
        <div className="panel-heading">
          <div className="panel-heading-icon pink"><BrainCircuit size={21} /></div>
          <div>
            <h2>Algorithm ROC-AUC comparison</h2>
            <p>All recorded experiments ? grouped by disease</p>
          </div>
          <span className="panel-meta">{experimentRows.length} EXPERIMENTS</span>
        </div>

        {!experimentRows.length ? (
          <div className="report-empty">
            <h2>Experiment comparison unavailable</h2>
            <p>No valid per-experiment ROC-AUC values were found.</p>
          </div>
        ) : (
          <div className="analytics-algorithm-grid">
            {diseaseGroups.map((group) => (
              <article className="analytics-algorithm-card" key={group.id}>
                <h3>{group.label}</h3>
                {group.models.map((model) => (
                  <MetricBar
                    key={`${group.id}-${model.model}`}
                    label={model.modelLabel}
                    value={model.auc * 100}
                    color="#9876cf"
                  />
                ))}
              </article>
            ))}
          </div>
        )}

        <p className="analytics-chart-footnote">
          ROC-AUC is displayed as a percentage for readability. Values come from each experiment's recorded test metrics.
        </p>
      </section>

      <section className="panel analytics-table-panel">
        <div className="panel-heading">
          <div className="panel-heading-icon pink"><Target size={21} /></div>
          <div>
            <h2>Selected model performance</h2>
            <p>Metrics sourced from best_models.json</p>
          </div>
          <span className="panel-meta">RECORDED RESULTS</span>
        </div>
        <div className="table-scroll">
          <table className="performance-table analytics-table">
            <thead>
              <tr>
                <th>Disease</th><th>Selected model</th><th>Accuracy</th>
                <th>Precision</th><th>Recall</th><th>F1-score</th><th>ROC-AUC</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.id}>
                  <td><strong>{r.disease}</strong></td>
                  <td>{r.model}</td>
                  <td><b className="accuracy-value">{r.accuracy.toFixed(2)}%</b></td>
                  <td>{(r.precision / 100).toFixed(3)}</td>
                  <td>{(r.recall / 100).toFixed(3)}</td>
                  <td>{(r.f1 / 100).toFixed(3)}</td>
                  <td>{r.auc.toFixed(4)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </>}

    <section className="analytics-notes-grid">
      <article className="info-tile">
        <span className="info-tile-icon"><FlaskConical /></span>
        <div>
          <strong>Interpret metrics carefully</strong>
          <p>These metrics describe recorded test-split performance, not performance in a clinical population.</p>
        </div>
      </article>
      <article className="info-tile warning-tile">
        <span className="info-tile-icon"><ShieldCheck /></span>
        <div>
          <strong>CKD result needs scrutiny</strong>
          <p>The recorded CKD ROC-AUC is 1.0000. Review possible leakage, split methodology and external validation before drawing strong conclusions.</p>
        </div>
      </article>
    </section>
  </main>;
}


function downloadCsv(filename, header, rows) {
  const csv = [header, ...rows].map((row) =>
    row.map((cell) => `"${String(cell ?? "").replaceAll('"', '""')}"`).join(",")
  ).join("\r\n");

  const url = URL.createObjectURL(new Blob([csv], { type: "text/csv;charset=utf-8" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
}

export function ReportsWorkspace({ reports = [], metrics, onDelete, error }) {
  const evaluationRows = getSelectedRows(metrics);

  const exportEvaluation = () => {
    downloadCsv(
      "medipredict-model-evaluation.csv",
      ["Disease", "Selected model", "Accuracy (%)", "Precision (%)", "Recall (%)", "F1-score (%)", "ROC-AUC"],
      evaluationRows.map((r) => [r.disease, r.model, r.accuracy.toFixed(2), r.precision.toFixed(2), r.recall.toFixed(2), r.f1.toFixed(2), r.auc.toFixed(4)])
    );
  };

  const exportReports = () => {
    downloadCsv(
      "medipredict-saved-assessments.csv",
      ["Date (UTC)", "Disease", "Model", "Prediction class", "Risk percentage", "Risk band"],
      reports.map((r) => [r.created_at, DISEASE_LABELS[r.disease] || r.disease, r.model, r.prediction, r.risk_percentage ?? "", r.risk_level])
    );
  };

  return <main className="workspace-page">
    <PageHeader eyebrow="RESEARCH OUTPUTS" title="Reports & exports" description="Download recorded model evaluation results and assessments explicitly saved to this workspace." icon={FileText}/>
    {error && <div className="predict-guidance" role="alert">{error}</div>}
    <div className="report-feature-card">
      <div className="report-feature-icon"><FileText size={25}/></div>
      <div><span className="dashboard-eyebrow">MODEL EVALUATION</span><h2>Model evaluation summary</h2><p>Selected-model held-out metrics from the training artifacts.</p><small>Research results ? not a clinical performance certificate</small></div>
      <button disabled={!evaluationRows.length} onClick={exportEvaluation}><Download size={17}/> Download CSV</button>
    </div>
    <section className="panel analytics-table-panel">
      <div className="panel-heading"><div className="panel-heading-icon pink"><FileText size={21}/></div><div><h2>Saved assessment reports</h2><p>{reports.length} saved report(s) ? metadata only</p></div><button disabled={!reports.length} onClick={exportReports}><Download size={16}/> Export CSV</button></div>
      {!reports.length ? <div className="report-empty"><span><FileText size={25}/></span><h2>No saved prediction reports yet</h2><p>Run an assessment and select Save assessment to store its result metadata.</p></div> :
        <div className="table-scroll"><table className="performance-table">
          <thead><tr><th>Date (UTC)</th><th>Disease</th><th>Model</th><th>Prediction</th><th>Score</th><th>Band</th><th>Action</th></tr></thead>
          <tbody>{reports.map((r) => <tr key={r.id}>
            <td>{new Date(r.created_at).toLocaleString()}</td>
            <td>{DISEASE_LABELS[r.disease] || r.disease}</td>
            <td>{r.model}</td>
            <td>{r.prediction}</td>
            <td>{r.risk_percentage == null ? "?" : `${Number(r.risk_percentage).toFixed(1)}%`}</td>
            <td>{r.risk_level || "unknown"}</td>
            <td><button type="button" className="secondary-button" onClick={() => onDelete?.(r.id)} aria-label={`Delete report ${r.id}`}><Trash2 size={15}/> Delete</button></td>
          </tr>)}</tbody>
        </table></div>
      }
    </section>
    <div className="medical-note"><ShieldCheck size={20}/><div><strong>Privacy and research use</strong><p>Saved reports contain prediction metadata, not the submitted feature values. Avoid entering identifiable patient information into this research prototype.</p></div></div>
  </main>;
}
