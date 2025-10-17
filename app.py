from flask import Flask
from flask_cors import CORS
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    register_blueprints(app)
    return app

app = create_app()

@app.route("/")
def home():
    return "To-Do List API funcionando. Versión actual: Octubre 2025"

if __name__ == "__main__":
    app.run(debug=False)
