from .auth import auth_bp
from .tasks import tasks_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tasks_bp, url_prefix='/api')