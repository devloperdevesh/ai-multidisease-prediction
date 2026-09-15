import {
  Activity,
  CircleDot,
  ChevronRight,
  ArrowRight,
  BrainCircuit,
  CheckCircle2,
  HeartPulse,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

export default function Overview({
  diseases,
  apiDiseases,
  online,
  onSelectDisease,
}) {
  return (
    <>
      <main>
        <section className="hero">
          <div className="hero-copy">
            <div className="eyebrow">
              <Sparkles size={13} />
              RESEARCH-GRADE MULTI-DISEASE ML
            </div>

            <h1>
              A clearer way to explore
              <span> health risk signals.</span>
            </h1>

            <p className="hero-lead">
              MediPredict AI brings four disease-specific machine-learning
              pipelines into one focused assessment workspace.
            </p>

            <div className="hero-actions">
              <button
                type="button"
                className="primary-button"
                onClick={() => onSelectDisease("diabetes")}
              >
                Start assessment
                <ArrowRight size={18} />
              </button>

              <button
                type="button"
                className="text-button"
                onClick={() => {
                  document
                    .getElementById("how-it-works")
                    ?.scrollIntoView({ behavior: "smooth" });
                }}
              >
                See how it works
              </button>
            </div>

            <div className="hero-trust">
              <CheckCircle2 size={15} />
              <span>Four production prediction pipelines</span>
            </div>
          </div>

          <div className="hero-product-card">
            <div className="product-card-header">
              <div>
                <span>LIVE WORKSPACE</span>
                <strong>Model orchestration</strong>
              </div>

              <div className={`live-chip ${online ? "online" : ""}`}>
                <span />
                {online ? "Connected" : "Offline"}
              </div>
            </div>

            <div className="model-visual">
              <div className="model-core">
                <BrainCircuit size={35} />
                <strong>AI</strong>
                <span>Inference</span>
              </div>

              <div className="model-node node-one">
                <Activity size={17} />
                <span>Diabetes</span>
              </div>

              <div className="model-node node-two">
                <HeartPulse size={17} />
                <span>Heart</span>
              </div>

              <div className="model-node node-three">
                <Activity size={17} />
                <span>CKD</span>
              </div>

              <div className="model-node node-four">
                <CircleDot size={17} />
                <span>Breast</span>
              </div>

              <div className="orbit orbit-one" />
              <div className="orbit orbit-two" />
            </div>

            <div className="product-card-footer">
              <span>
                <ShieldCheck size={14} />
                Disease-specific pipelines
              </span>
              <span>6 algorithms evaluated</span>
            </div>
          </div>
        </section>

        <section className="metrics-strip">
          <div>
            <strong>04</strong>
            <span>Disease modules</span>
          </div>
          <div>
            <strong>06</strong>
            <span>Algorithms evaluated</span>
          </div>
          <div>
            <strong>01</strong>
            <span>Unified API</span>
          </div>
          <div>
            <strong>ML</strong>
            <span>Pipeline-based inference</span>
          </div>
        </section>

        <section className="section" id="assessment">
          <div className="section-heading">
            <div>
              <span className="section-kicker">ASSESSMENT MODULES</span>
              <h2>Choose a condition.</h2>
              <p>
                Each module maps directly to its disease-specific production
                model.
              </p>
            </div>

            <div className="module-count">
              <strong>{apiDiseases.length || diseases.length}</strong>
              <span>active modules</span>
            </div>
          </div>

          <div className="disease-grid">
            {diseases.map((disease) => {
              const backendDisease = apiDiseases.find(
                (item) => item.id === disease.id
              );

              return (
                <button
                  type="button"
                  className="disease-card"
                  key={disease.id}
                  onClick={() => onSelectDisease(disease.id)}
                >
                  <div className={`disease-card-icon ${disease.accent}`}>
                    {disease.id === "heart" ? (
                      <HeartPulse size={23} />
                    ) : disease.id === "breast_cancer" ? (
                      <CircleDot size={23} />
                    ) : (
                      <Activity size={23} />
                    )}
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
                        {backendDisease?.feature_count ?? disease.fields}{" "}
                        features
                      </span>

                      <span className="open-module">
                        Assess
                        <ArrowRight size={15} />
                      </span>
                    </div>
                  </div>
                </button>
              );
            })}
          </div>
        </section>

        <section className="method-section" id="how-it-works">
          <div className="method-intro">
            <span className="section-kicker">HOW IT WORKS</span>
            <h2>
              From parameters
              <br />
              to model output.
            </h2>
            <p>
              A consistent software architecture connects disease-specific
              inputs to persisted machine-learning pipelines.
            </p>
          </div>

          <div className="pipeline">
            {[
              ["01", "Clinical parameters", "Disease-specific input"],
              ["02", "Preprocessing", "Imputation + encoding + scaling"],
              ["03", "Production model", "Persisted trained pipeline"],
              ["04", "Risk insight", "Model-estimated probability"],
            ].map(([number, title, text], index) => (
              <div className="pipeline-item" key={number}>
                <div className="pipeline-number">{number}</div>
                <div>
                  <strong>{title}</strong>
                  <span>{text}</span>
                </div>
                {index < 3 && <ChevronRight className="pipeline-arrow" size={18} />}
              </div>
            ))}
          </div>
        </section>

        <section className="disclaimer">
          <ShieldCheck size={21} />
          <div>
            <strong>Important medical disclaimer</strong>
            <p>
              MediPredict AI provides preliminary risk predictions for research
              and educational purposes only. Results are not medical diagnoses
              and should not replace professional medical advice, examination,
              or treatment.
            </p>
          </div>
        </section>
      </main>
    </>
  );
}







