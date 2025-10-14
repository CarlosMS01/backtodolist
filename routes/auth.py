from flask import Blueprint, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from database import db
from models import User
from utils.auth_utils import generate_token, validate_credentials, get_current_user
from utils.validators import is_valid_email, is_valid_password, is_valid_username

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# ---------------------------------------------------------------------------------------------

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    user = validate_credentials(email, password)
    if not user:
        return jsonify({'error': 'Credenciales inválidas'}), 401

    token = generate_token(user.id)

    response = make_response(jsonify({'message': 'Login exitoso'}))
    response.set_cookie(
        'access_token',
        token,
        httponly=True,
        secure=True,
        samesite='None',
        max_age=7200
    )
    return response

# ---------------------------------------------------------------------------------------------

@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = jsonify({'message': 'Sesión cerrada'})
    response.set_cookie(
        'access_token',
        '',
        httponly=True,
        secure=True,
        samesite='None',
        max_age=0
    )
    return response

# ---------------------------------------------------------------------------------------------

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if not (is_valid_username(username) and is_valid_email(email) and is_valid_password(password)):
        return jsonify({'error': 'Datos inválidos. Verifica nombre, email y contraseña'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email ya registrado'}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado correctamente'})

# ---------------------------------------------------------------------------------------------

@auth_bp.route("/me", methods=["GET"])
def me():
    user = get_current_user()
    if not user:
        return jsonify({"message": "No autenticado"}), 401
    return jsonify({"username": user.username})

# ---------------------------------------------------------------------------------------------