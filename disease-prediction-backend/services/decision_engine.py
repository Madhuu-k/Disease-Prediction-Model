from data.question_bank import PHASE_2_QUESTIONS

# =========================
# DOMAIN TRIGGERS (PHASE 1 → PHASE 2)
# =========================

SIGNAL_MAP = {

    "heart": ["chest_pain", "palpitations", "breathlessness"],

    "vascular": ["cold_hands_and_feets", "fatigue", "weight_loss"],

    "neuro": ["dizziness", "loss_of_balance", "weakness_of_limbs"],

    "skin": ["itching", "skin_rash"],

    "gastro": ["stomach_pain", "vomiting", "acidity"],

    "respiratory": ["cough", "fever", "breathlessness"]
}

def detect_active_domain(phase1_answers):
    active_domains = []
    for domain, signals in SIGNAL_MAP.items():
        for signal in signals:
            if phase1_answers.get(signal) is True:
                active_domains.append(domain)
                break
            
    return active_domains   

def get_phase2_questions(phase1_answers):
    active_domains = detect_active_domain(phase1_answers)
    
    phase2_questions = {}
    
    for domain in active_domains:
        phase2_questions[domain] = PHASE_2_QUESTIONS.get(domain, {})
        
    return phase2_questions