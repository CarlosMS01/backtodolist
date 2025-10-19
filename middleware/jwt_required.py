from flask import request, jsonify, g
from functools import wraps
import jwt, os
from database import supabase

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('access_token')

        if not token:
            print("Token no encontrado en cookies")
            return jsonify({'error': 'Token requerido'}), 401

        try:
            payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
            user_id = payload.get('user_id')
            if not user_id:
                print("Token sin user_id")
                return jsonify({'error': 'Token inválido'}), 401

            result = supabase.table("users").select("id").eq("id", user_id).execute()
            if not result.data:
                print("Usuario no encontrado en Supabase")
                return jsonify({'error': 'Usuario no válido'}), 401

            g.user_id = user_id

        except jwt.ExpiredSignatureError:
            print("Token expirado")
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            print("Token inválido")
            return jsonify({'error': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return wrapper
