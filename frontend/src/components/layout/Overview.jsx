import {
  Activity, ArrowRight, CircleDot, Database, HeartPulse, ShieldCheck, Target, FlaskConical,
  Droplet, Microscope, BrainCircuit
} from "lucide-react";

const BENCHMARKS = [
  { id:"diabetes", name:"Diabetes", model:"Logistic Regression", accuracy:70.78, f1:54.55, auc:0.8130, tone:"blue", icon:Droplet, source:"Pima Indians Diabetes" },
  { id:"heart", name:"Heart Disease", model:"Logistic Regression", accuracy:86.89, f1:86.67, auc:0.9513, tone:"rose", icon:HeartPulse, source:"UCI Heart Disease" },
  { id:"ckd", name:"CKD", model:"Logistic Regression", accuracy:98.75, f1:98.99, auc:1.0000, tone:"orange", icon:Activity, source:"UCI Chronic Kidney Disease" },
  { id:"breast_cancer", name:"Breast Cancer", model:"Logistic Regression", accuracy:96.49, f1:95.12, auc:0.9960, tone:"purple", icon:CircleDot, source:"Breast Cancer Wisconsin Diagnostic" },
];

export default function Overview({ diseases, apiDiseases, online, onSelectDisease, search="", userName="Researcher" }) {
  const query = search.trim().toLowerCase();
  const visible = diseases.filter(d => `${d.label} ${d.description}`.toLowerCase().includes(query));
  const avg = (BENCHMARKS.reduce((sum, item) => sum + item.accuracy, 0) / BENCHMARKS.length).toFixed(2);
  const apiCount = apiDiseases.length;

  return <main className="dashboard-content">
    <section className="welcome-row">
      <div><span className="dashboard-eyebrow">YOUR RESEARCH WORKSPACE</span><h1>Good to see you, {userName.split(" ")[0]} <span className="wave">👋</span></h1><p>Here’s your multi-disease model evaluation and prediction overview.</p></div>
      <div className="workspace-pill"><span className={`status-dot ${online ? "online" : ""}`}/><strong>{online ? "API connected" : "API offline"}</strong><i/>4 disease modules<i/>6 algorithms evaluated</div>
    </section>

    <section className="stat-grid" aria-label="Project summary">
      <article className="stat-card"><span className="stat-icon violet"><Database/></span><div><strong>04</strong><span>Public datasets</span><small>One per disease module</small></div></article>
      <article className="stat-card"><span className="stat-icon pink"><BrainCircuit/></span><div><strong>24</strong><span>Model experiments</span><small>6 algorithms × 4 datasets</small></div></article>
      <article className="stat-card"><span className="stat-icon mint"><Target/></span><div><strong>{avg}%</strong><span>Mean test accuracy</span><small>Unweighted mean · 4 test splits</small></div></article>
      <article className="stat-card"><span className="stat-icon amber"><ShieldCheck/></span><div><strong>41</strong><span>Automated tests passed</span><small>Latest recorded test run</small></div></article>
    </section>

    <section className="module-section" id="disease-modules">
      <div className="section-title-row"><div><span className="dashboard-eyebrow">ASSESSMENT MODULES</span><h2>Choose a disease to assess</h2><p>Open a module to enter its required dataset features and run the connected model.</p></div><span className="count-chip">{apiCount || 0}/4 APIs ready</span></div>
      <div className="dashboard-disease-grid">
        {visible.map(d => {
          const benchmark = BENCHMARKS.find(b => b.id === d.id);
          const Icon = benchmark?.icon || Activity;
          const ready = apiDiseases.some(x => x.id === d.id);
          return <article className={`dashboard-disease-card ${benchmark?.tone || "blue"}`} key={d.id}>
            <div className="disease-card-top"><span className="disease-symbol"><Icon size={25}/></span><span className={`module-status ${ready ? "ready" : ""}`}><i/>{ready ? "Model ready" : "API unavailable"}</span></div>
            <h3>{d.label}</h3><p>{d.description}</p>
            <div className="dataset-chip"><Database size={13}/>{benchmark?.source}</div>
            <div className="disease-card-bottom"><span>{apiDiseases.find(x=>x.id===d.id)?.feature_count ?? d.fields} input features</span><button onClick={()=>onSelectDisease(d.id)}>Predict {d.id==="ckd"?"CKD":d.id==="breast_cancer"?"Breast Cancer":d.label} <ArrowRight size={16}/></button></div>
          </article>;
        })}
        {visible.length === 0 && <div className="empty-search">No disease modules match “{search}”. Try another search term.</div>}
      </div>
    </section>

    <section className="dataset-snapshot-section">
      <div className="section-title-row"><div><span className="dashboard-eyebrow">DATA FOUNDATION</span><h2>Dataset snapshots</h2><p>Public benchmark datasets used in the current training run.</p></div><span className="count-chip">2,040 total records</span></div>
      <div className="dataset-snapshot-grid">
        <article className="dataset-snapshot blue"><span>DIABETES · PIMA</span><strong>768</strong><small>records · 8 predictors</small><div><i style={{width:"37.6%"}}/></div><small>Train 614 · Test 154</small></article>
        <article className="dataset-snapshot rose"><span>HEART · UCI</span><strong>303</strong><small>records · 13 predictors</small><div><i style={{width:"14.9%"}}/></div><small>Train 242 · Test 61</small></article>
        <article className="dataset-snapshot orange"><span>CKD · UCI</span><strong>400</strong><small>records · 24 predictors</small><div><i style={{width:"19.6%"}}/></div><small>Train 320 · Test 80</small></article>
        <article className="dataset-snapshot purple"><span>BREAST CANCER · WDBC</span><strong>569</strong><small>records · 30 predictors</small><div><i style={{width:"27.9%"}}/></div><small>Train 455 · Test 114</small></article>
      </div>
      <p className="dataset-snapshot-note">Dataset counts reflect the local benchmark files used for the recorded experiment. Train/test counts are the recorded stratified split sizes.</p>
    </section>

    <section className="insights-grid">
      <article className="panel benchmark-panel" id="model-performance">
        <div className="panel-heading"><div className="panel-heading-icon pink"><Target size={21}/></div><div><h2>Model performance</h2><p>Selected models · held-out test split</p></div><span className="panel-meta">REAL EVALUATION</span></div>
        <div className="table-scroll"><table className="performance-table"><thead><tr><th>Disease</th><th>Selected model</th><th>Accuracy</th><th>F1-score</th><th>ROC-AUC</th></tr></thead><tbody>
          {BENCHMARKS.map(row=><tr key={row.id}><td><span className={`table-disease-icon ${row.tone}`}><row.icon size={17}/></span><strong>{row.name}</strong></td><td>{row.model}</td><td><b className="accuracy-value">{row.accuracy.toFixed(2)}%</b></td><td>{(row.f1/100).toFixed(3)}</td><td>{row.auc.toFixed(3)}</td></tr>)}
        </tbody></table></div>
        <div className="benchmark-note"><FlaskConical size={15}/> Metrics are from the project’s recorded test results. Performance on these public datasets does not establish clinical validity or generalization to new populations.</div>
      </article>

      <article className="panel activity-panel">
        <div className="panel-heading"><div className="panel-heading-icon blue"><Activity size={21}/></div><div><h2>Prediction activity</h2><p>Live activity from this workspace</p></div></div>
        <div className="activity-empty"><span className="empty-chart-icon"><Microscope size={27}/></span><strong>No prediction history yet</strong><p>Once assessments are run, this area can show recorded prediction activity. No sample trend data is displayed.</p></div>
        <div className="activity-footer"><span><i className={`status-dot ${online ? "online" : ""}`}/>{online ? "Prediction service reachable" : "Waiting for API connection"}</span><span>History not configured</span></div>
      </article>
    </section>

    <section className="bottom-info-grid">
      <article className="info-tile"><span className="info-tile-icon"><FlaskConical/></span><div><strong>How the system works</strong><p>Input validation → preprocessing pipeline → selected classifier → model-estimated output.</p></div></article>
      <article className="info-tile"><span className="info-tile-icon"><ShieldCheck/></span><div><strong>Use responsibly</strong><p>For research and education only. Never use this prototype to make clinical decisions.</p></div></article>
    </section>
  </main>;
}
