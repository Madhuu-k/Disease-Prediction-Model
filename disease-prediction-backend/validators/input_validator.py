from services.model_service import phase1_features

def validate_phase1_input(data):
    if not isinstance(data, dict): return False, "Input must be JSON Object"
    
    cleaned_data = {}
    
    for feature in phase1_features:
        value = data.get(feature, 0)
        
        if value not in (0, 1):
            return False, f"Invalid value for feature {feature}, Must be 0 or 1"
        
        cleaned_data[feature] = value
        
    extra_fields = set(data.keys()) - set(phase1_features)
    if extra_fields: return False, f"Unknown Fields detcted: {list(extra_fields)}"
        
    return True, cleaned_data