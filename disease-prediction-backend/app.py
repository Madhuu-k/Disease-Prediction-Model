from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.predict import predict_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(predict_bp)
print(app.url_map)


if __name__ == "__main__":
    app.run(debug=True) 