import { useEffect, useState } from "react";
import {
  ArrowRight,
  BrainCircuit,
  CheckCircle2,
  ShieldCheck,
} from "lucide-react";

import { DISEASES } from "./data/diseases";
import { getDiseases, getHealth, predictDisease } from "./services/api";

import Topbar from "./components/layout/Topbar";
import Overview from "./components/layout/Overview";
import Research from "./components/research/Research";
import DiseaseForm, {
  createInitialForm,
} from "./components/disease/DiseaseForm";
import RiskResult from "./components/prediction/RiskResult";

function App() {
  const [view, setView] = useState("overview");
  const [selectedDisease, setSelectedDisease] = useState(null);
  const [formValues, setFormValues] = useState({});
  const [result, setResult] = useState(null);

  const [apiDiseases, setApiDiseases] = useState([]);
  const [online, setOnline] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    let active = true;

    Promise.all([getHealth(), getDiseases()])
      .then(([, diseaseResponse]) => {
        if (!active) return;
        setOnline(true);
        setApiDiseases(diseaseResponse?.diseases || []);
      })
      .catch((requestError) => {
        if (!active) return;
        setOnline(false);
        setError(
          "The frontend is running, but the prediction API could not be reached."
        );
      });

    return () => {
      active = false;
    };
  }, []);

  const openDisease = (disease) => {
    setSelectedDisease(disease);
    setFormValues(createInitialForm(disease));
    setResult(null);
    setError("");
    setView("assessment");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const runPrediction = async () => {
    setLoading(true);
    setError("");

    try {
      const payload = Object.fromEntries(
        Object.entries(formValues).filter(([key]) => key !== "__error")
      );

      const fields = Object.keys(payload);

      const diseaseFields = payload;

      Object.keys(diseaseFields).forEach((key) => {
        const value = diseaseFields[key];

        if (value !== "" && value !== null && !Number.isNaN(Number(value))) {
          const numericField =
            typeof value === "string" &&
            /^-?\d+(\.\d+)?$/.test(value.trim());

          if (numericField) {
            diseaseFields[key] = Number(value);
          }
        }
      });

      const prediction = await predictDisease(selectedDisease, diseaseFields);

      setResult(prediction);
      setView("result");
      window.scrollTo({ top: 0, behavior: "smooth" });
    } catch (requestError) {
      setError(
        requestError?.message ||
          "The model service returned an unexpected error."
      );
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setSelectedDisease(null);
    setFormValues({});
    setResult(null);
    setError("");
    setView("overview");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <div className="app-shell">
      <Topbar
        online={online}
        view={view === "result" ? "assessment" : view}
        setView={(nextView) => {
          setView(nextView);
          if (nextView !== "assessment") {
            setSelectedDisease(null);
            setResult(null);
          }
        }}
        mobileOpen={mobileOpen}
        setMobileOpen={setMobileOpen}
      />

      {view === "overview" && (
        <Overview
          diseases={DISEASES}
          apiDiseases={apiDiseases}
          online={online}
          onSelectDisease={openDisease}
        />
      )}

      {view === "research" && <Research />}

      {view === "assessment" && selectedDisease && (
        <DiseaseForm
          diseaseId={selectedDisease}
          values={formValues}
          setValues={setFormValues}
          onSubmit={runPrediction}
          onBack={() => {
            setError("");
            setView("overview");
          }}
          loading={loading}
          error={error}
        />
      )}

      {view === "result" && selectedDisease && result && (
        <RiskResult
          disease={DISEASES.find((item) => item.id === selectedDisease)}
          result={result}
          onBack={() => setView("assessment")}
          onReset={reset}
        />
      )}

      <footer className="footer">
        <div className="footer-brand">
          <span className="footer-mark">
            <BrainCircuit size={16} />
          </span>
          <div>
            <strong>MediPredict AI</strong>
            <span>AI-Based Multi-Disease Prediction</span>
          </div>
        </div>

        <div className="footer-meta">
          <span>Research Project · 2026</span>
          <span>I.T.S Engineering College · AKTU</span>
        </div>

        <a
          href="https://github.com/devloperdevesh/ai-multidisease-prediction"
          target="_blank"
          rel="noreferrer"
          className="github-link"
        >
          <BrainCircuit size={16} />
          Repository
        </a>
      </footer>
    </div>
  );
}

export default App;



