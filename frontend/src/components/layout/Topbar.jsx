import {
  Activity,
  ArrowRight,
  BrainCircuit,
  CheckCircle2,
  ChevronRight,
  CircleDot,
  HeartPulse,
  Menu,
  ShieldCheck,
  Sparkles,
  X,
} from "lucide-react";

export default function Topbar({
  online,
  view,
  setView,
  mobileOpen,
  setMobileOpen,
}) {
  const go = (target) => {
    setView(target);
    setMobileOpen(false);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <header className="topbar">
      <button
        type="button"
        className="brand"
        onClick={() => go("overview")}
        aria-label="MediPredict AI home"
      >
        <span className="brand-mark">
          <BrainCircuit size={21} />
        </span>

        <span className="brand-copy">
          <strong>MediPredict AI</strong>
          <small>I.T.S Engineering College</small>
        </span>
      </button>

      <nav className={`nav ${mobileOpen ? "is-open" : ""}`}>
        <button
          type="button"
          className={view === "overview" ? "active" : ""}
          onClick={() => go("overview")}
        >
          Overview
        </button>

        <button
          type="button"
          className={view === "assessment" ? "active" : ""}
          onClick={() => go("assessment")}
        >
          Assessment
        </button>

        <button
          type="button"
          className={view === "research" ? "active" : ""}
          onClick={() => go("research")}
        >
          Methodology
        </button>
      </nav>

      <div className="topbar-right">
        <div className={`api-status ${online ? "online" : ""}`}>
          <span />
          {online ? "API online" : "API offline"}
        </div>

        <button
          type="button"
          className="mobile-menu-button"
          onClick={() => setMobileOpen((value) => !value)}
          aria-label="Toggle navigation"
        >
          {mobileOpen ? <X size={20} /> : <Menu size={20} />}
        </button>
      </div>
    </header>
  );
}
