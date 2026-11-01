import { useState } from "react";
import { Activity, ArrowRight, BrainCircuit, ShieldCheck, HeartPulse, UserRound, GraduationCap } from "lucide-react";

export default function WorkspaceLogin({ onContinue }) {
  const [name, setName] = useState("");
  const [role, setRole] = useState("Student / Researcher");
  const [accepted, setAccepted] = useState(false);
  const [error, setError] = useState("");

  const submit = (event) => {
    event.preventDefault();
    const cleanName = name.trim().replace(/\\s+/g, " ");
    if (cleanName.length < 2) return setError("Please enter your name (at least 2 characters).");
    if (!accepted) return setError("Please acknowledge the research-use notice to continue.");
    onContinue({ name: cleanName, role, createdAt: new Date().toISOString() });
  };

  return <main className="workspace-login">
    <div className="login-glow login-glow-one"/><div className="login-glow login-glow-two"/>
    <section className="login-brand"><span className="login-brand-icon"><HeartPulse size={27}/></span><span>MediPredict <b>AI</b></span></section>
    <div className="login-layout">
      <section className="login-intro">
        <span className="login-eyebrow"><Activity size={14}/> RESEARCH-GRADE MULTI-DISEASE ML</span>
        <h1>Understand the signals.<br/><em>Explore the models.</em></h1>
        <p>A unified workspace for four disease-specific machine-learning pipelines, transparent model evaluation and research-oriented assessment.</p>
        <div className="login-feature-list">
          <div><span><BrainCircuit/></span><div><strong>Four trained ML pipelines</strong><small>Diabetes · Heart · CKD · Breast Cancer</small></div></div>
          <div><span><ShieldCheck/></span><div><strong>Transparent evaluation</strong><small>Real held-out test metrics, not sample figures</small></div></div>
          <div><span><GraduationCap/></span><div><strong>Built for learning and research</strong><small>Educational prototype, not clinical diagnosis</small></div></div>
        </div>
      </section>
      <form className="login-card" onSubmit={submit}>
        <div className="login-card-icon"><UserRound size={23}/></div>
        <span className="login-card-kicker">YOUR PERSONAL WORKSPACE</span>
        <h2>Welcome to MediPredict AI</h2>
        <p>Enter your display name to personalise this workspace.</p>
        <label className="login-label" htmlFor="workspace-name">Full name</label>
        <div className="login-input-wrap"><UserRound size={17}/><input id="workspace-name" value={name} onChange={e => {setName(e.target.value);setError("");}} placeholder="e.g. Devesh Chauhan" autoComplete="name" maxLength={60} required/></div>
        <label className="login-label" htmlFor="workspace-role">I am using this for</label>
        <select id="workspace-role" value={role} onChange={e => setRole(e.target.value)}><option>Student / Researcher</option><option>Faculty / Educator</option><option>Developer</option><option>Other</option></select>
        <label className="login-consent"><input type="checkbox" checked={accepted} onChange={e => {setAccepted(e.target.checked);setError("");}}/><span>I understand this is a research and educational prototype, not a medical diagnosis tool.</span></label>
        {error && <div className="login-error" role="alert">{error}</div>}
        <button className="login-submit" type="submit">Enter workspace <ArrowRight size={17}/></button>
        <div className="login-privacy"><ShieldCheck size={14}/> No password or medical profile is collected here. Your display name is saved locally in this browser.</div>
        <div className="login-demo-note">Local workspace profile · No real account authentication</div>
      </form>
    </div>
    <footer className="login-footer">© 2026 MediPredict AI · I.T.S Engineering College <span>Research prototype · Not for clinical use</span></footer>
  </main>;
}
