import {
  ArrowRight,
  ArrowLeft,
  ChevronDown,
  Info,
  LoaderCircle,
} from "lucide-react";
import { FIELD_DEFINITIONS, getDisease } from "../../data/diseases";

function initialState(fields) {
  return Object.fromEntries(fields.map((field) => [field.name, ""]));
}

export function createInitialForm(disease) {
  return initialState(FIELD_DEFINITIONS[disease]);
}

function groupedFields(fields) {
  return fields.reduce((groups, field) => {
    if (!groups[field.group]) groups[field.group] = [];
    groups[field.group].push(field);
    return groups;
  }, {});
}

export default function DiseaseForm({
  diseaseId,
  values,
  setValues,
  onSubmit,
  onBack,
  loading,
  error,
}) {
  const disease = getDisease(diseaseId);
  const fields = FIELD_DEFINITIONS[diseaseId];
  const groups = groupedFields(fields);

  const handleChange = (name, value) => {
    setValues((current) => ({
      ...current,
      [name]: value,
    }));
  };

  const submit = (event) => {
    event.preventDefault();

    const missing = fields.filter(
      (field) =>
        values[field.name] === undefined ||
        values[field.name] === null ||
        values[field.name] === ""
    );

    if (missing.length > 0) {
      setValues((current) => ({
        ...current,
        __error: `${missing.length} required field${
          missing.length === 1 ? "" : "s"
        } still need attention.`,
      }));
      return;
    }

    setValues((current) => {
      const next = { ...current };
      delete next.__error;
      return next;
    });

    onSubmit();
  };

  const localError = values.__error;

  return (
    <section className="assessment-page">
      <div className="assessment-header">
        <button type="button" className="back-button" onClick={onBack}>
          <ArrowLeft size={17} />
          All conditions
        </button>

        <div className="assessment-title-row">
          <div>
            <span className="eyebrow">ASSESSMENT WORKSPACE</span>
            <h1>{disease.label}</h1>
            <p>{disease.description}</p>
          </div>

          <div className="feature-counter">
            <strong>{fields.length}</strong>
            <span>input features</span>
          </div>
        </div>
      </div>

      {(localError || error) && (
        <div className="form-error" role="alert">
          <Info size={18} />
          <div>
            <strong>{localError ? "Check the form" : "Prediction unavailable"}</strong>
            <span>{localError || error}</span>
          </div>
        </div>
      )}

      <form onSubmit={submit}>
        <div className="form-sections">
          {Object.entries(groups).map(([group, groupFields]) => (
            <div className="form-section-card" key={group}>
              <div className="form-section-heading">
                <div>
                  <span className="section-index">
                    {String(
                      Object.keys(groups).indexOf(group) + 1
                    ).padStart(2, "0")}
                  </span>
                  <div>
                    <h2>{group}</h2>
                    <p>Enter the values used by the production model.</p>
                  </div>
                </div>

                <ChevronDown size={17} />
              </div>

              <div className="field-grid">
                {groupFields.map((field) => (
                  <label className="field" key={field.name}>
                    <span className="field-label">
                      {field.label}
                      <span>*</span>
                    </span>

                    {field.type === "select" ? (
                      <select
                        value={values[field.name] ?? ""}
                        onChange={(event) =>
                          handleChange(field.name, event.target.value)
                        }
                        required
                      >
                        <option value="" disabled>
                          Select
                        </option>

                        {field.options.map((option) => (
                          <option key={String(option.value)} value={option.value}>
                            {option.label}
                          </option>
                        ))}
                      </select>
                    ) : (
                      <div className="input-shell">
                        <input
                          type="number"
                          inputMode="decimal"
                          step="any"
                          value={values[field.name] ?? ""}
                          onChange={(event) =>
                            handleChange(field.name, event.target.value)
                          }
                          placeholder={field.placeholder}
                          required
                        />
                        {field.unit && <span>{field.unit}</span>}
                      </div>
                    )}

                    <span className="field-key">{field.name}</span>
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="submit-bar">
          <div>
            <strong>Ready for assessment?</strong>
            <span>
              Your values are sent to the local/API prediction service for
              processing.
            </span>
          </div>

          <button
            type="submit"
            className="primary-button"
            disabled={loading}
          >
            {loading ? (
              <>
                <LoaderCircle className="spin" size={18} />
                Running model
              </>
            ) : (
              <>
                Run risk assessment
                <ArrowRight size={18} />
              </>
            )}
          </button>
        </div>
      </form>
    </section>
  );
}




