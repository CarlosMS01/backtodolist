# backend/database.py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def init_app():
    load_dotenv()
    app = Flask(__name__)

    database_url = os.getenv('DATABASE_URL')
    if not database_url or not database_url.startswith("postgresql"):
        raise RuntimeError("DATABASE_URL no está definido en el entorno. Verifica tu archivo .env.")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app
