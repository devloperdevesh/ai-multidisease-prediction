export const DISEASES = [
  {
    id: "diabetes",
    label: "Diabetes",
    short: "Diabetes mellitus",
    description:
      "Assess metabolic and demographic parameters associated with diabetes risk.",
    icon: "activity",
    accent: "blue",
    fields: 8,
  },
  {
    id: "heart",
    label: "Heart Disease",
    short: "Cardiovascular risk",
    description:
      "Evaluate cardiovascular parameters through the trained heart-disease model.",
    icon: "heart",
    accent: "rose",
    fields: 13,
  },
  {
    id: "ckd",
    label: "Chronic Kidney Disease",
    short: "Renal health",
    description:
      "Assess renal, blood, urine and clinical indicators used by the CKD model.",
    icon: "kidney",
    accent: "violet",
    fields: 24,
  },
  {
    id: "breast_cancer",
    label: "Breast Cancer",
    short: "Diagnostic features",
    description:
      "Evaluate digitized breast-mass measurements using the trained classification model.",
    icon: "scan",
    accent: "amber",
    fields: 30,
  },
];

const numeric = (
  name,
  label,
  placeholder,
  unit = "",
  group = "Clinical parameters"
) => ({
  name,
  label,
  type: "number",
  placeholder,
  unit,
  group,
});

const select = (name, label, options, group = "Clinical parameters") => ({
  name,
  label,
  type: "select",
  options,
  group,
});

export const FIELD_DEFINITIONS = {
  diabetes: [
    numeric("Pregnancies", "Pregnancies", "e.g. 2", "", "Patient profile"),
    numeric("Glucose", "Glucose", "e.g. 120", "mg/dL", "Metabolic profile"),
    numeric("BloodPressure", "Blood pressure", "e.g. 72", "mmHg", "Vital signs"),
    numeric("SkinThickness", "Skin thickness", "e.g. 23", "mm", "Body measurements"),
    numeric("Insulin", "Insulin", "e.g. 80", "µU/mL", "Metabolic profile"),
    numeric("BMI", "Body mass index", "e.g. 31.6", "kg/m²", "Body measurements"),
    numeric(
      "DiabetesPedigreeFunction",
      "Diabetes pedigree function",
      "e.g. 0.47",
      "",
      "Risk indicators"
    ),
    numeric("Age", "Age", "e.g. 33", "years", "Patient profile"),
  ],

  heart: [
    numeric("age", "Age", "e.g. 54", "years", "Patient profile"),
    select(
      "sex",
      "Sex",
      [
        { value: 0, label: "Female (0)" },
        { value: 1, label: "Male (1)" },
      ],
      "Patient profile"
    ),
    select(
      "cp",
      "Chest pain type",
      [
        { value: 1, label: "Type 1" },
        { value: 2, label: "Type 2" },
        { value: 3, label: "Type 3" },
        { value: 4, label: "Type 4" },
      ],
      "Symptoms"
    ),
    numeric("trestbps", "Resting blood pressure", "e.g. 130", "mmHg", "Vital signs"),
    numeric("chol", "Serum cholesterol", "e.g. 246", "mg/dL", "Laboratory"),
    select(
      "fbs",
      "Fasting blood sugar",
      [
        { value: 0, label: "≤ 120 mg/dL (0)" },
        { value: 1, label: "> 120 mg/dL (1)" },
      ],
      "Laboratory"
    ),
    select(
      "restecg",
      "Resting ECG",
      [
        { value: 0, label: "Category 0" },
        { value: 1, label: "Category 1" },
        { value: 2, label: "Category 2" },
      ],
      "Cardiac tests"
    ),
    numeric("thalach", "Maximum heart rate", "e.g. 150", "bpm", "Cardiac tests"),
    select(
      "exang",
      "Exercise-induced angina",
      [
        { value: 0, label: "No (0)" },
        { value: 1, label: "Yes (1)" },
      ],
      "Symptoms"
    ),
    numeric("oldpeak", "ST depression", "e.g. 1.2", "", "Cardiac tests"),
    select(
      "slope",
      "ST segment slope",
      [
        { value: 1, label: "Category 1" },
        { value: 2, label: "Category 2" },
        { value: 3, label: "Category 3" },
      ],
      "Cardiac tests"
    ),
    select(
      "ca",
      "Major vessels",
      [
        { value: 0, label: "0" },
        { value: 1, label: "1" },
        { value: 2, label: "2" },
        { value: 3, label: "3" },
      ],
      "Cardiac tests"
    ),
    select(
      "thal",
      "Thalassemia",
      [
        { value: 3, label: "3" },
        { value: 6, label: "6" },
        { value: 7, label: "7" },
      ],
      "Cardiac tests"
    ),
  ],

  ckd: [
    numeric("age", "Age", "e.g. 48", "years", "Patient profile"),
    numeric("bp", "Blood pressure", "e.g. 80", "mmHg", "Vital signs"),
    select(
      "sg",
      "Specific gravity",
      [
        { value: 1.005, label: "1.005" },
        { value: 1.01, label: "1.010" },
        { value: 1.015, label: "1.015" },
        { value: 1.02, label: "1.020" },
        { value: 1.025, label: "1.025" },
      ],
      "Urine analysis"
    ),
    select(
      "al",
      "Albumin",
      [0, 1, 2, 3, 4, 5].map((v) => ({ value: v, label: String(v) })),
      "Urine analysis"
    ),
    select(
      "su",
      "Sugar",
      [0, 1, 2, 3, 4, 5].map((v) => ({ value: v, label: String(v) })),
      "Urine analysis"
    ),
    select(
      "rbc",
      "Red blood cells",
      [
        { value: "normal", label: "Normal" },
        { value: "abnormal", label: "Abnormal" },
      ],
      "Urine analysis"
    ),
    select(
      "pc",
      "Pus cell",
      [
        { value: "normal", label: "Normal" },
        { value: "abnormal", label: "Abnormal" },
      ],
      "Urine analysis"
    ),
    select(
      "pcc",
      "Pus cell clumps",
      [
        { value: "notpresent", label: "Not present" },
        { value: "present", label: "Present" },
      ],
      "Urine analysis"
    ),
    select(
      "ba",
      "Bacteria",
      [
        { value: "notpresent", label: "Not present" },
        { value: "present", label: "Present" },
      ],
      "Urine analysis"
    ),
    numeric("bgr", "Blood glucose random", "e.g. 121", "mg/dL", "Laboratory"),
    numeric("bu", "Blood urea", "e.g. 36", "mg/dL", "Laboratory"),
    numeric("sc", "Serum creatinine", "e.g. 1.2", "mg/dL", "Laboratory"),
    numeric("sod", "Sodium", "e.g. 138", "mEq/L", "Laboratory"),
    numeric("pot", "Potassium", "e.g. 4.5", "mEq/L", "Laboratory"),
    numeric("hemo", "Hemoglobin", "e.g. 13.2", "g/dL", "Laboratory"),
    numeric("pcv", "Packed cell volume", "e.g. 40", "%", "Blood profile"),
    numeric("wbcc", "White blood cell count", "e.g. 8000", "/cmm", "Blood profile"),
    numeric("rbcc", "Red blood cell count", "e.g. 4.8", "mill/mm³", "Blood profile"),
    select(
      "htn",
      "Hypertension",
      [
        { value: "no", label: "No" },
        { value: "yes", label: "Yes" },
      ],
      "Clinical history"
    ),
    select(
      "dm",
      "Diabetes mellitus",
      [
        { value: "no", label: "No" },
        { value: "yes", label: "Yes" },
      ],
      "Clinical history"
    ),
    select(
      "cad",
      "Coronary artery disease",
      [
        { value: "no", label: "No" },
        { value: "yes", label: "Yes" },
      ],
      "Clinical history"
    ),
    select(
      "appet",
      "Appetite",
      [
        { value: "good", label: "Good" },
        { value: "poor", label: "Poor" },
      ],
      "Clinical history"
    ),
    select(
      "pe",
      "Pedal edema",
      [
        { value: "no", label: "No" },
        { value: "yes", label: "Yes" },
      ],
      "Clinical history"
    ),
    select(
      "ane",
      "Anemia",
      [
        { value: "no", label: "No" },
        { value: "yes", label: "Yes" },
      ],
      "Clinical history"
    ),
  ],

  breast_cancer: [
    ["radius1", "Radius", "Mean"],
    ["texture1", "Texture", "Mean"],
    ["perimeter1", "Perimeter", "Mean"],
    ["area1", "Area", "Mean"],
    ["smoothness1", "Smoothness", "Mean"],
    ["compactness1", "Compactness", "Mean"],
    ["concavity1", "Concavity", "Mean"],
    ["concave_points1", "Concave points", "Mean"],
    ["symmetry1", "Symmetry", "Mean"],
    ["fractal_dimension1", "Fractal dimension", "Mean"],

    ["radius2", "Radius", "Standard error"],
    ["texture2", "Texture", "Standard error"],
    ["perimeter2", "Perimeter", "Standard error"],
    ["area2", "Area", "Standard error"],
    ["smoothness2", "Smoothness", "Standard error"],
    ["compactness2", "Compactness", "Standard error"],
    ["concavity2", "Concavity", "Standard error"],
    ["concave_points2", "Concave points", "Standard error"],
    ["symmetry2", "Symmetry", "Standard error"],
    ["fractal_dimension2", "Fractal dimension", "Standard error"],

    ["radius3", "Radius", "Worst"],
    ["texture3", "Texture", "Worst"],
    ["perimeter3", "Perimeter", "Worst"],
    ["area3", "Area", "Worst"],
    ["smoothness3", "Smoothness", "Worst"],
    ["compactness3", "Compactness", "Worst"],
    ["concavity3", "Concavity", "Worst"],
    ["concave_points3", "Concave points", "Worst"],
    ["symmetry3", "Symmetry", "Worst"],
    ["fractal_dimension3", "Fractal dimension", "Worst"],
  ].map(([name, label, group]) =>
    numeric(name, label, "Enter value", "", group)
  ),
};

export const getDisease = (id) =>
  DISEASES.find((disease) => disease.id === id);
