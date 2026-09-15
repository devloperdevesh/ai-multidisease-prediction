import { BrainCircuit, Database, FlaskConical, ShieldCheck } from "lucide-react";

export default function Research() {
  return (
    <main className="research-page">
      <section className="research-hero">
        <span className="eyebrow">
          <FlaskConical size={13} />
          RESEARCH METHODOLOGY
        </span>

        <h1>
          Built as an ML system,
          <span> not just a prediction page.</span>
        </h1>

        <p>
          MediPredict AI combines disease-specific datasets, preprocessing
          pipelines, comparative model evaluation and production inference
          behind a single interface.
        </p>
      </section>

      <section className="research-grid">
        <article>
          <Database size={21} />
          <span>01</span>
          <h2>Data</h2>
          <p>
            Publicly available disease datasets are normalized into consistent
            training interfaces while preserving disease-specific feature
            semantics.
          </p>
        </article>

        <article>
          <FlaskConical size={21} />
          <span>02</span>
          <h2>Preprocessing</h2>
          <p>
            Missing-value handling, categorical encoding and numerical scaling
            are encapsulated inside the persisted ML pipeline.
          </p>
        </article>

        <article>
          <BrainCircuit size={21} />
          <span>03</span>
          <h2>Model selection</h2>
          <p>
            Logistic Regression, Decision Tree, Random Forest, SVM, KNN and
            XGBoost are evaluated for each disease.
          </p>
        </article>

        <article>
          <ShieldCheck size={21} />
          <span>04</span>
          <h2>Inference</h2>
          <p>
            The production API loads the selected model artifact and returns a
            model-estimated probability with an explicit non-diagnostic
            disclaimer.
          </p>
        </article>
      </section>

      <section className="research-note">
        <div>
          <span className="section-kicker">SYSTEM PRINCIPLE</span>
          <h2>Reproducibility over visual claims.</h2>
        </div>

        <p>
          The interface is intentionally designed to make the underlying
          engineering visible: exact disease schemas, persisted pipelines,
          model selection and API-based inference.
        </p>
      </section>
    </main>
  );
}
