from flask import Blueprint, request, jsonify
from validators.input_validator import validate_phase1_input
from services.model_service import get_phase2_features

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    if not data: return jsonify({"error" : "No input  provided"}), 400
    
    is_valid, result = validate_phase1_input(data)
    if not is_valid:
        return jsonify({"error" : result}), 400
    
    phase2_groups = get_phase2_features(result)
    
    return jsonify({
        "phase2_groups" : phase2_groups
    })     