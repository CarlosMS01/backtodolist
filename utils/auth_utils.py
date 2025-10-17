import os, jwt
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------------------------

def generate_token(user_id: str, expires_in: int = 7200) -> str:
    jwt_secret = os.getenv('JWT_SECRET')
    if not jwt_secret:
        raise RuntimeError("JWT_SECRET no definido en el entorno")

    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(seconds=expires_in)
    }

    return jwt.encode(payload, jwt_secret, algorithm='HS256')

# ---------------------------------------------------------------------------------------------

def decode_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
        return payload.get('user_id')
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None
