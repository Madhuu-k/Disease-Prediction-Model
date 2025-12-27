from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.predict import predict_bp

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True, silent=True)

        if data is None:
            return jsonify({"error": "Invalid or missing JSON"}), 415

        print("Received data:", data)

        return jsonify({
            "route_detected": "heart",
            "confidence": 0.82,
            "message": "Backend successfully connected"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)