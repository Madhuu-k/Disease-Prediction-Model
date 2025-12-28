from flask import request, jsonify, Blueprint
from services.explanation_service import explain_prediction
from validators.input_validator import validate_user_input
from services.feature_inference import infer_ml_features
from services.model_service import get_phase2_groups
from services.disease_service import predict_disease
from data.question_bank import PHASE2_QUESTIONS

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    user_input = request.get_json()
    if not user_input:
        return jsonify({"error" : "Empty Body Request"}), 400
    
    valid, result = validate_user_input(user_input)
    if not valid:
        return jsonify({"error" : result}), 400
    
    ml_features = infer_ml_features(result)
    
    phase2_groups = get_phase2_groups(ml_features)
    phase2_questions = {}
    
    for group in phase2_groups:
        if group in PHASE2_QUESTIONS:
            phase2_questions[group] = PHASE2_QUESTIONS[group]
            
    has_phase2_answers = any(
        q["id"] in result
        for questions in PHASE2_QUESTIONS.values()
        for q in questions
    )
            
    response = {
        "phase2_groups": phase2_groups,
        "phase2_questions": phase2_questions,
        "ml_feature_inputs": ml_features
    }

    if has_phase2_answers:
        disease_predictions = predict_disease(ml_features)
        for d in disease_predictions:
            d["reasons"] = explain_prediction(d["disease"], ml_features)
            
        response["disease_predictions"] = disease_predictions

    return jsonify(response)