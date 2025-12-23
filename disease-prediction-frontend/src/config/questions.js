export const QUESTIONS = [

  // ================= STEP 1: BASIC DEMOGRAPHICS =================
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
    label: "What is your weight (KG)?",
    type: "number",
    required: true,
    step: 1
  },

  // ================= STEP 2: COMMON GENERAL SYMPTOMS =================
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

  // ================= STEP 3: SYSTEMIC / BODY-WIDE SYMPTOMS =================
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
    id: "sweating",
    label: "Do you experience high/mild sweating?",
    type: "boolean",
    step: 3
  },

  // ================= STEP 4: MEDICAL & LIFESTYLE HISTORY =================
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

  // ================= STEP 5: ORGAN-SPECIFIC SYMPTOMS =================
  {
    id: "chest_pain",
    label: "Do you experience chest pain or discomfort?",
    type: "boolean",
    step: 5
  },
  {
    id: "abdominal_pain",
    label: "Do you experience abdominal pain?",
    type: "boolean",
    step: 5
  },
  {
    id: "shortness_of_breath",
    label: "Do you experience shortness of breath?",
    type: "boolean",
    step: 5
  }
];
