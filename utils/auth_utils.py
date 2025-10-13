import os, jwt, re
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from backtodolist.models import User

bcrypt = Bcrypt()

# ---------------------------------------------------------------------------------------------

def generate_token(user_id: int, expires_in: int = 7200) -> str:
    jwt_secret = os.getenv('JWT_SECRET')
    if not jwt_secret:
        raise RuntimeError("JWT_SECRET no definido en el entorno")

    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(seconds=expires_in)
    }

    return jwt.encode(payload, jwt_secret, algorithm='HS256')

# ---------------------------------------------------------------------------------------------

def validate_credentials(email: str, password: str) -> User | None:
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        return user
    return None
