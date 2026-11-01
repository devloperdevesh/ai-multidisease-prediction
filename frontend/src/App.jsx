import { useEffect, useState } from "react";
import {
  BarChart3, Bell, ChevronDown, FileText,
  HeartPulse, Home, Info, Menu, Search, ShieldCheck,
  Stethoscope, TableProperties, X, LogOut, UserRound
} from "lucide-react";
import { DISEASES } from "./data/diseases";
import { getDiseases, getHealth, predictDisease, getMetrics, getReports, createReport, deleteReport } from "./services/api";
import Overview from "./components/layout/Overview";
import Research from "./components/research/Research";
import DiseaseForm, { createInitialForm } from "./components/disease/DiseaseForm";
import RiskResult from "./components/prediction/RiskResult";
import WorkspaceLogin from "./components/layout/WorkspaceLogin";
import { PredictWorkspace, AnalyticsWorkspace, ReportsWorkspace } from "./components/layout/WorkspacePages";

const NAV = [
  ["overview", "Dashboard", Home],
  ["predict", "Predict Disease", Stethoscope],
  ["analytics", "Model Analytics", BarChart3],
  ["reports", "Reports", FileText],
  ["research", "Dataset & Research", TableProperties],
  ["about", "About", Info],
];

function App() {
  const [view, setView] = useState("overview");
  const [selectedDisease, setSelectedDisease] = useState(null);
  const [formValues, setFormValues] = useState({});
  const [result, setResult] = useState(null);
  const [apiDiseases, setApiDiseases] = useState([]);
  const [online, setOnline] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [metrics, setMetrics] = useState(null);
  const [savedReports, setSavedReports] = useState([]);
  const [savingReport, setSavingReport] = useState(false);
  const [reportSaved, setReportSaved] = useState(false);
  const [saveMessage, setSaveMessage] = useState("");
  const [reportsError, setReportsError] = useState("");
  const [mobileOpen, setMobileOpen] = useState(false);
  const [search, setSearch] = useState("");
  const [profile, setProfile] = useState(() => {
    try { return JSON.parse(localStorage.getItem("medipredict_workspace_profile") || "null"); }
    catch { return null; }
  });
  const [profileMenu, setProfileMenu] = useState(false);

  const saveProfile = (nextProfile) => {
    localStorage.setItem("medipredict_workspace_profile", JSON.stringify(nextProfile));
    setProfile(nextProfile);
  };
  const signOut = () => {
    localStorage.removeItem("medipredict_workspace_profile");
    setProfile(null);
    setProfileMenu(false);
  };

  useEffect(() => {
    let active = true;
    Promise.all([getHealth(), getDiseases()])
      .then(([, response]) => {
        if (!active) return;
        setOnline(true);
        setApiDiseases(response?.diseases || []);
      })
      .catch(() => { if (active) setOnline(false); });
    return () => { active = false; };
  }, []);

  useEffect(() => {
    let active = true;

    Promise.all([getMetrics(), getReports()])
      .then(([metricData, reportData]) => {
        if (!active) return;
        setMetrics(metricData);
        setSavedReports(reportData?.reports || []);
      })
      .catch((e) => {
        if (active) setReportsError(e?.message || "Could not load research data.");
      });

    return () => { active = false; };
  }, []);

  const refreshReports = async () => {
    const response = await getReports();
    setSavedReports(response?.reports || []);
  };

  const saveAssessment = async () => {
    if (!result || !selectedDisease || savingReport || reportSaved) return;

    setSavingReport(true);
    setSaveMessage("");
    try {
      await createReport({
        disease: selectedDisease,
        model: result.model,
        prediction: Number(result.prediction),
        risk_percentage: result.risk_percentage ?? null,
        risk_level: result.risk_level || "unknown",
      });
      await refreshReports();
      setReportSaved(true);
      setSaveMessage("Assessment saved. Raw assessment inputs were not stored.");
    } catch (e) {
      setSaveMessage(e?.message || "Unable to save this assessment.");
    } finally {
      setSavingReport(false);
    }
  };

  const removeSavedReport = async (id) => {
    try {
      await deleteReport(id);
      await refreshReports();
      setReportsError("");
    } catch (e) {
      setReportsError(e?.message || "Unable to delete report.");
    }
  };

  const navigate = (next) => {
    setMobileOpen(false);
    setView(next);
    if (!(["assessment", "result"].includes(next))) {
      setSelectedDisease(null);
      setResult(null);
      setError("");
    }
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const openDisease = (id) => {
    setSelectedDisease(id);
    setFormValues(createInitialForm(id));
    setResult(null);
    setError("");
    setView("assessment");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const runPrediction = async () => {
    setLoading(true);
    setError("");
    try {
      const payload = Object.fromEntries(Object.entries(formValues).filter(([key]) => key !== "__error"));
      for (const key of Object.keys(payload)) {
        if (typeof payload[key] === "string" && payload[key].trim() !== "" && Number.isFinite(Number(payload[key]))) {
          payload[key] = Number(payload[key]);
        }
      }
      const prediction = await predictDisease(selectedDisease, payload);
      setResult(prediction);
      setReportSaved(false);
      setSaveMessage("");
      setView("result");
      window.scrollTo({ top: 0, behavior: "smooth" });
    } catch (e) {
      setError(e?.message || "The model service returned an unexpected error.");
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setSelectedDisease(null); setFormValues({}); setResult(null); setError(""); setReportSaved(false); setSaveMessage("");
    setView("overview"); window.scrollTo({ top: 0, behavior: "smooth" });
  };

  if (!profile) return <WorkspaceLogin onContinue={saveProfile} />;

  return (
    <div className="dashboard-shell">
      <aside className={`sidebar ${mobileOpen ? "sidebar-open" : ""}`}>
        <button className="sidebar-brand" onClick={() => navigate("overview")} aria-label="MediPredict dashboard">
          <span className="brand-heart"><HeartPulse size={26} /></span>
          <span>MediPredict <b>AI</b></span>
        </button>
        <div className="sidebar-caption">WORKSPACE</div>
        <nav className="side-nav" aria-label="Main navigation">
          {NAV.map(([id, label, Icon]) => {
            const active = view === id || (id === "predict" && ["assessment", "result"].includes(view));
            return <button key={id} className={`side-link ${active ? "active" : ""}`} aria-current={active ? "page" : undefined} onClick={() => navigate(id)}>
              <Icon size={19} strokeWidth={2} /><span>{label}</span>
            </button>;
          })}
        </nav>
        <div className="sidebar-promo">
          <div className="promo-icon"><Stethoscope size={25} /></div>
          <strong>AI-assisted research</strong>
          <p>Four disease-specific machine-learning pipelines in one workspace.</p>
          <span className="promo-foot"><ShieldCheck size={14}/> Research use only</span>
        </div>
        <div className="sidebar-bottom"><span className={`status-dot ${online ? "online" : ""}`}/>{online ? "Prediction API connected" : "API connection unavailable"}</div>
      </aside>

      {mobileOpen && <button className="mobile-scrim" onClick={() => setMobileOpen(false)} aria-label="Close menu" />}
      <div className="dashboard-main">
        <header className="dashboard-topbar">
          <button className="mobile-toggle" onClick={() => setMobileOpen(v => !v)} aria-label="Toggle menu">{mobileOpen ? <X/> : <Menu/>}</button>
          <div className="topbar-title"><strong>MediPredict AI</strong><span>AI-Based Multi-Disease Risk Prediction System</span></div>
          <label className="global-search"><Search size={17}/><input value={search} onChange={e => setSearch(e.target.value)} placeholder="Search diseases, datasets, models..." /></label>
          <button className="icon-action" title="Notifications"><Bell size={19}/><i/></button>
          <div className="profile-wrap">
            <button className="profile-chip" onClick={() => setProfileMenu(v => !v)} aria-expanded={profileMenu}>
              <span>{profile.name.split(/\s+/).map(part => part[0]).slice(0,2).join("").toUpperCase()}</span>
              <div><strong>{profile.name}</strong><small>{profile.role || "Research workspace"}</small></div><ChevronDown size={16}/>
            </button>
            {profileMenu && <div className="profile-menu"><div className="profile-menu-heading"><UserRound size={16}/><span>{profile.name}</span></div><button onClick={signOut}><LogOut size={15}/> Switch workspace</button><small>Profile is stored locally in this browser.</small></div>}
          </div>
        </header>

        {view === "overview" && <Overview diseases={DISEASES} apiDiseases={apiDiseases} online={online} onSelectDisease={openDisease} search={search} userName={profile.name} />}
        {view === "predict" && <PredictWorkspace diseases={DISEASES} apiDiseases={apiDiseases} onSelectDisease={openDisease} />}
        {view === "analytics" && <AnalyticsWorkspace metrics={metrics} />}
        {view === "reports" && <ReportsWorkspace reports={savedReports} metrics={metrics} onDelete={removeSavedReport} error={reportsError} />}
        {view === "research" && <Research />}
        {view === "about" && <section className="content-page"><span className="dashboard-eyebrow">ABOUT THE PROJECT</span><h1>MediPredict AI</h1><p>A research and educational multi-disease risk prediction system developed at I.T.S Engineering College.</p><div className="info-panel"><ShieldCheck/><div><strong>Responsible use</strong><p>This application is a research prototype. It does not provide medical diagnosis, treatment recommendations, or emergency guidance.</p></div></div></section>}
        {view === "assessment" && selectedDisease && <DiseaseForm diseaseId={selectedDisease} values={formValues} setValues={setFormValues} onSubmit={runPrediction} onBack={() => navigate("predict")} loading={loading} error={error}/>}
        {view === "result" && selectedDisease && result && <RiskResult disease={DISEASES.find(d => d.id === selectedDisease)} result={result} onBack={() => setView("assessment")} onReset={reset} onSave={saveAssessment} saving={savingReport} saved={reportSaved} saveMessage={saveMessage}/>}
        <footer className="dashboard-footer"><span>© 2026 MediPredict AI · I.T.S Engineering College</span><span>Research prototype · Not for clinical use</span><a href="https://github.com/devloperdevesh/ai-multidisease-prediction" target="_blank" rel="noreferrer">GitHub repository <ChevronDown size={13}/></a></footer>
      </div>
    </div>
  );
}
export default App;
