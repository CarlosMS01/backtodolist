from flask_cors import CORS
from backtodolist.database import init_app, db
from backtodolist.routes import register_blueprints

def create_app():
    app = init_app()
    CORS(app, supports_credentials=True)
    register_blueprints(app)
    return app

app = create_app()

@app.route("/")
def home():
    return "To-Do Pro API funcionando. Versión actual: Octubre 2025"

if __name__ == "__main__":
    app.run(debug=False)
