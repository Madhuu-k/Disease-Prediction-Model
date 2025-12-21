REQUIRED_FIELDS = [
    "age", "gender", "symptom_1", "symptom_2"
]

def validate_input(data):
    if not data:
        return "No JSON Provided"
    
    for field in REQUIRED_FIELDS:
        if field not in data:
            return f"Missig Fields: {field}"
        
    return None