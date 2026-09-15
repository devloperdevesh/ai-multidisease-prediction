import {
  Activity,
  ArrowRight,
  BrainCircuit,
  CheckCircle2,
  CircleDot,
  HeartPulse,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

const ICONS = {
  activity: Activity,
  heart: HeartPulse,
  kidney: Activity,
  scan: CircleDot,
};

export default function DiseaseCard({
  disease,
  backendDisease,
  selected,
  onSelect,
}) {
  const Icon = ICONS[disease.icon] || Activity;

  return (
    <button
      type="button"
      className={`disease-card ${selected ? "is-selected" : ""}`}
      onClick={onSelect}
    >
      <div className={`disease-card-icon ${disease.accent}`}>
        <Icon size={22} strokeWidth={1.8} />
      </div>

      <div className="disease-card-body">
        <div className="disease-card-topline">
          <span>{disease.short}</span>
          {backendDisease && (
            <span className="ready-badge">
              <CheckCircle2 size={12} />
              Ready
            </span>
          )}
        </div>

        <h3>{disease.label}</h3>

        <p>{disease.description}</p>

        <div className="disease-card-footer">
          <span>
            {backendDisease?.feature_count ?? disease.fields} features
          </span>

          <span className="open-module">
            Open assessment
            <ArrowRight size={15} />
          </span>
        </div>
      </div>
    </button>
  );
}
