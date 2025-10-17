from flask import Blueprint, request, jsonify, make_response
from flask_bcrypt import Bcrypt
from database import supabase
from utils.auth_utils import generate_token, decode_token
from utils.validators import is_valid_email, is_valid_password, is_valid_username

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# ---------------------------------------------------------------------------------------------

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    result = supabase.table("users").select("*").eq("email", email).execute()
    user = result.data[0] if result.data else None

    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({'error': 'Credenciales inválidas'}), 401

    token = generate_token(user["id"])

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

    existing = supabase.table("users").select("id").eq("email", email).execute()
    if existing.data:
        return jsonify({'error': 'Email ya registrado'}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    supabase.table("users").insert({
        "username": username,
        "email": email,
        "password": hashed_pw
    }).execute()

    return jsonify({'message': 'Usuario registrado correctamente'})

# ---------------------------------------------------------------------------------------------

@auth_bp.route("/me", methods=["GET"])
def me():
    token = request.cookies.get("access_token")
    if not token:
        return jsonify({"message": "No autenticado"}), 401

    user_id = decode_token(token)
    if not user_id:
        return jsonify({"message": "Token inválido"}), 401

    result = supabase.table("users").select("username").eq("id", user_id).execute()
    user = result.data[0] if result.data else None

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    return jsonify({"username": user["username"]})

# ---------------------------------------------------------------------------------------------