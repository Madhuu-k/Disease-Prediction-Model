from flask import Flask
from flask_cors import CORS
from routes.predict import predict_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # register blueprint
    app.register_blueprint(predict_bp)
    
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)