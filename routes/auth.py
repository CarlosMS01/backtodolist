from flask import Blueprint, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from backtodolist.database import db
from backtodolist.models import User
from backtodolist.utils.auth_utils import generate_token, validate_credentials
from backtodolist.utils.validators import is_valid_email, is_valid_password, is_valid_username

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