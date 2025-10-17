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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
