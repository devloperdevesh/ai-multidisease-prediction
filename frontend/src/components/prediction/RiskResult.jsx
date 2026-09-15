import {
  Activity,
  ArrowLeft,
  CheckCircle2,
  CircleAlert,
  RotateCcw,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

export default function RiskResult({
  disease,
  result,
  onBack,
  onReset,
}) {
  const percentage = Math.max(
    0,
    Math.min(100, Number(result?.risk_percentage ?? 0))
  );

  const level = result?.risk_level || "unknown";
  const elevated = Number(result?.prediction) === 1;

  const levelLabel =
    level === "high"
      ? "High"
      : level === "moderate"
        ? "Moderate"
        : level === "low"
          ? "Low"
          : "Model output";

  return (
    <section className="result-page">
      <button type="button" className="back-button" onClick={onBack}>
        <ArrowLeft size={17} />
        Back to assessment
      </button>

      <div className="result-header">
        <div>
          <span className="eyebrow">MODEL OUTPUT</span>
          <h1>Assessment complete</h1>
          <p>
            {disease.label} · production prediction pipeline
          </p>
        </div>

        <div className="result-status">
          <CheckCircle2 size={16} />
          Completed
        </div>
      </div>

      <div className="result-grid">
        <div className="risk-card">
          <div className="risk-card-top">
            <div>
              <span className="section-kicker">MODEL-ESTIMATED SCORE</span>
              <h2>{percentage.toFixed(1)}%</h2>
              <p>
                Probability estimate returned by the selected machine-learning
                pipeline.
              </p>
            </div>

            <div
              className={`risk-ring ${level}`}
              style={{ "--score": `${percentage * 3.6}deg` }}
              aria-label={`Model-estimated score ${percentage.toFixed(1)} percent`}
            >
              <div>
                <strong>{Math.round(percentage)}</strong>
                <span>%</span>
              </div>
            </div>
          </div>

          <div className={`result-band ${level}`}>
            <div className="result-band-icon">
              {elevated ? (
                <CircleAlert size={19} />
              ) : (
                <CheckCircle2 size={19} />
              )}
            </div>

            <div>
              <strong>
                {elevated ? "Elevated risk signal" : "Lower risk signal"}
              </strong>
              <span>
                Display band: {levelLabel}. This is a non-clinical presentation
                band, not a medical threshold.
              </span>
            </div>
          </div>
        </div>

        <aside className="result-details">
          <div className="detail-card">
            <span className="detail-label">MODEL</span>
            <strong>{result?.model || "—"}</strong>
            <small>Selected production model</small>
          </div>

          <div className="detail-card">
            <span className="detail-label">PREDICTION CLASS</span>
            <strong>{String(result?.prediction ?? "—")}</strong>
            <small>Classifier output</small>
          </div>

          <div className="detail-card">
            <span className="detail-label">SERVICE</span>
            <strong>MediPredict API</strong>
            <small>Live model inference endpoint</small>
          </div>
        </aside>
      </div>

      <div className="result-actions">
        <button type="button" className="secondary-button" onClick={onReset}>
          <RotateCcw size={17} />
          New assessment
        </button>
      </div>

      <div className="medical-note">
        <ShieldCheck size={20} />
        <div>
          <strong>Research and education only</strong>
          <p>
            MediPredict AI provides preliminary risk predictions. This result
            is not a medical diagnosis and should not replace examination,
            professional medical advice, or treatment.
          </p>
        </div>
      </div>
    </section>
  );
}
