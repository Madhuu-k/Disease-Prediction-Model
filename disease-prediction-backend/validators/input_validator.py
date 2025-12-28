from data.question_bank import PHASE1_QUESTIONS, PHASE2_QUESTIONS

PHASE1_IDS = {q["id"] for q in PHASE1_QUESTIONS}
PHASE2_IDS = set()

for group_questions in PHASE2_QUESTIONS.values():
    for q in group_questions:
        PHASE2_IDS.add(q["id"])
        
ALL_VALID_IDS = PHASE1_IDS.union(PHASE2_IDS)

def validate_user_input(data):
    if not isinstance(data, dict):
        return False, "Input must ne JSON Object"
    
    unknown_keys = set(data.keys()) - ALL_VALID_IDS
    if unknown_keys:
        return False, f"Unknown question IDs: {list(unknown_keys)}"

    for key, value in data.items():
        if value not in (0, 1, True, False):
            return False, f"Invalid value for '{key}'. Must be 0/1 or true/false."

    return True, data