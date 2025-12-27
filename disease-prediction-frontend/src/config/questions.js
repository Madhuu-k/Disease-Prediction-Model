export const QUESTIONS = [

  // ============================================================
  // STEP 1: BASIC DEMOGRAPHICS (ALWAYS ASKED)
  // ============================================================
  {
    id: "age",
    label: "What is your age?",
    type: "number",
    required: true,
    step: 1
  },
  {
    id: "gender",
    label: "What is your gender?",
    type: "select",
    options: ["Male", "Female"],
    required: true,
    step: 1
  },
  {
    id: "weight",
    label: "What is your weight (in kg)?",
    type: "number",
    required: false,
    step: 1
  },

  // ============================================================
  // STEP 2: GENERAL HIGH-FREQUENCY SYMPTOMS (TRIAGE BASE)
  // ============================================================
  {
    id: "fever",
    label: "Do you have fever?",
    type: "boolean",
    step: 2
  },
  {
    id: "cough",
    label: "Do you have cough?",
    type: "boolean",
    step: 2
  },
  {
    id: "cold",
    label: "Do you have cold or nasal congestion?",
    type: "boolean",
    step: 2
  },
  {
    id: "headache",
    label: "Do you experience headache?",
    type: "boolean",
    step: 2
  },
  {
    id: "fatigue",
    label: "Do you feel unusual fatigue?",
    type: "boolean",
    step: 2
  },

  // ============================================================
  // STEP 3: SYSTEMIC / BODY-WIDE SYMPTOMS
  // ============================================================
  {
    id: "weight_loss",
    label: "Have you experienced unexplained weight loss?",
    type: "boolean",
    step: 3
  },
  {
    id: "loss_of_appetite",
    label: "Have you noticed loss of appetite?",
    type: "boolean",
    step: 3
  },
  {
    id: "night_sweats",
    label: "Do you experience night sweats?",
    type: "boolean",
    step: 3
  },

  // ============================================================
  // STEP 4: MEDICAL & LIFESTYLE HISTORY
  // ============================================================
  {
    id: "smoking",
    label: "Do you smoke?",
    type: "boolean",
    step: 4
  },
  {
    id: "alcohol",
    label: "Do you consume alcohol regularly?",
    type: "boolean",
    step: 4
  },
  {
    id: "chronic_disease",
    label: "Do you have any chronic medical condition?",
    type: "boolean",
    step: 4
  },

  // ============================================================
  // STEP 5: PHASE-2 — ROUTE-SPECIFIC QUESTIONS
  // ============================================================

  // ---------------- HEART / CARDIAC ----------------
  {
    id: "chest_pain",
    label: "Do you experience chest pain or discomfort?",
    type: "boolean",
    step: 5,
    route: "heart"
  },
  {
    id: "palpitations",
    label: "Do you experience palpitations?",
    type: "boolean",
    step: 5,
    route: "heart"
  },
  {
    id: "shortness_of_breath",
    label: "Do you experience shortness of breath?",
    type: "boolean",
    step: 5,
    route: "heart"
  },
  {
    id: "swelling_of_legs",
    label: "Do you have swelling in your legs or ankles?",
    type: "boolean",
    step: 5,
    route: "heart"
  },

  // ---------------- NEUROLOGICAL ----------------
  {
    id: "dizziness",
    label: "Do you experience dizziness?",
    type: "boolean",
    step: 5,
    route: "neuro"
  },
  {
    id: "loss_of_balance",
    label: "Do you experience loss of balance?",
    type: "boolean",
    step: 5,
    route: "neuro"
  },
  {
    id: "seizures",
    label: "Have you experienced seizures?",
    type: "boolean",
    step: 5,
    route: "neuro"
  },
  {
    id: "weakness_of_limbs",
    label: "Do you experience weakness in your arms or legs?",
    type: "boolean",
    step: 5,
    route: "neuro"
  },

  // ---------------- GASTROINTESTINAL ----------------
  {
    id: "abdominal_pain",
    label: "Do you experience abdominal pain?",
    type: "boolean",
    step: 5,
    route: "gastro"
  },
  {
    id: "nausea",
    label: "Do you experience nausea?",
    type: "boolean",
    step: 5,
    route: "gastro"
  },
  {
    id: "vomiting",
    label: "Do you experience vomiting?",
    type: "boolean",
    step: 5,
    route: "gastro"
  },
  {
    id: "diarrhoea",
    label: "Do you experience diarrhoea?",
    type: "boolean",
    step: 5,
    route: "gastro"
  },

  // ---------------- RESPIRATORY ----------------
  {
    id: "productive_cough",
    label: "Do you have cough with sputum?",
    type: "boolean",
    step: 5,
    route: "respiratory"
  },
  {
    id: "wheezing",
    label: "Do you experience wheezing?",
    type: "boolean",
    step: 5,
    route: "respiratory"
  },
  {
    id: "chest_tightness",
    label: "Do you experience chest tightness?",
    type: "boolean",
    step: 5,
    route: "respiratory"
  },

  // ---------------- INFECTIOUS / SYSTEMIC ----------------
  {
    id: "chills",
    label: "Do you experience chills?",
    type: "boolean",
    step: 5,
    route: "infectious"
  },
  {
    id: "persistent_fever",
    label: "Does your fever persist for several days?",
    type: "boolean",
    step: 5,
    route: "infectious"
  },
  {
    id: "body_aches",
    label: "Do you experience body aches?",
    type: "boolean",
    step: 5,
    route: "infectious"
  }
];
