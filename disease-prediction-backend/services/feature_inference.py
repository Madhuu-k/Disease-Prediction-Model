from services.model_service import ML_ROUTING_FEATURES

def infer_ml_features(screening_answers: dict) -> dict:
    # -------------------------
    # Initialize ALL ML features to 0
    # -------------------------
    ml_features = {feature: 0 for feature in ML_ROUTING_FEATURES}

    # -------------------------
    # DIRECT MAPPINGS
    # -------------------------
    
    if screening_answers.get("fatigue"):
        ml_features["fatigue"] = 1

    if screening_answers.get("headache"):
        ml_features["headache"] = 1

    if screening_answers.get("loss_of_appetite"):
        ml_features["loss_of_appetite"] = 1
        ml_features["nausea"] = 1  # appetite loss often implies nausea

    if screening_answers.get("nausea"):
        ml_features["nausea"] = 1
        ml_features["vomiting"] = 1

    if screening_answers.get("abdominal_pain"):
        ml_features["abdominal_pain"] = 1

    if screening_answers.get("skin_rash"):
        ml_features["skin_rash"] = 1

    if screening_answers.get("chills"):
        ml_features["chills"] = 1
        ml_features["high_fever"] = 1

    # -------------------------
    # INDIRECT / COMPOSITE SIGNALS
    # -------------------------
    if screening_answers.get("fever"):
        ml_features["high_fever"] = 1
        ml_features["chills"] = 1

    if screening_answers.get("weight_loss"):
        ml_features["loss_of_appetite"] = 1

    # Yellowing usually not asked directly in Phase-1,
    # but may be inferred later from Phase-2
    if screening_answers.get("yellowish_skin"):
        ml_features["yellowish_skin"] = 1
        ml_features["yellowing_of_eyes"] = 1

    return ml_features
