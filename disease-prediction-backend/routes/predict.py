from flask import Blueprint, request, jsonify
from validators.input_validator import validate_input
from services.model_service import predict_disease

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    error = validate_input(data)
    if error:
        return jsonify({"error":error}), 400
    
    result = predict_disease(data)
    return jsonify(result)      