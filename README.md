# 📝 Backend para ToDo List con Flask

Este proyecto es un backend seguro y modular para una aplicación de tareas (ToDo List). Incluye autenticación con JWT, registro de usuarios, y operaciones CRUD para gestionar tareas. Está diseñado para ser desplegado fácilmente y validado desde el frontend.

## 💻 Tecnologías utilizadas

- **Flask 3.1.2** – Framework principal
- **Flask-Bcrypt 1.0.1** – Encriptación de contraseñas
- **Flask-SQLAlchemy 3.1.1** – ORM para base de datos
- **Flask-Cors 6.0.1** – Permitir peticiones desde frontend
- **python-dotenv 1.1.1** – Manejo de variables de entorno
- **PyJWT 2.10.1** – Autenticación con tokens JWT
- **psycopg2-binary 2.9.11** – Conexión con PostgreSQL

## 📦 Instalación local

```bash
git clone https://github.com/CarlosMS01/backtodolist.git
cd backtodolist

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## 📁 Estructura de carpetas

```bash
backtodolist/
├── routes/
│   ├── __init__.py
│   └── auth.py
├── utils/
│   ├── __init__.py
│   ├── auth_utils.py
│   └── validators.py
├──  __init__.py
├── .env
├── .gitignore
├── app.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
```

## 📝 Estructura del proyecto

Este backend está organizado como paquete Python para blindar imports y facilitar despliegue.

- Cada carpeta contiene `__init__.py` para evitar errores de importación.
- Archivo .gitignore para evitar subir archivos innecesarios o sensibles al repositorio.

### 🧩 `routes/__init__.py`
Centraliza el registro de rutas en la aplicación Flask:

```python
from .auth import auth_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/auth")
```

### 🔐 `routes/auth.py`
Define las rutas `/login` y `/logout` usando `Blueprint`. Implementa autenticación segura con JWT y cookies HTTP-only:

- `login()`: valida credenciales y genera token JWT.
- `logout()`: elimina el token del navegador.
- Usa `bcrypt` para verificar contraseñas encriptadas.
- Integra validadores y utilidades desde `utils`.

### 🧠 `utils/validators.py`
Funciones para validar datos de entrada:

- `is_valid_email(email)`: verifica formato de correo.
- `is_valid_password(password)`: exige mínimo 8 caracteres y al menos un número.
- `is_valid_username(username)`: exige mínimo 3 caracteres.

### 🔑 `utils/auth_utils.py`
Encapsula la lógica de autenticación:

- `generate_token(user_id)`: crea un token JWT con expiración configurable.
- `validate_credentials(email, password)`: consulta el usuario en la base de datos y verifica la contraseña con `bcrypt`.

## 🔐 Seguridad y Validación

Este proyecto implementa validaciones robustas y pruebas automatizadas para prevenir ataques comunes como inyecciones SQL.

- Se validan campos como `email`, `password` y `username` antes de procesarlos.
- Se utiliza SQLAlchemy para evitar interpolación directa de datos en consultas.

## 🚀 Ejecución

```bash
python -m backtodolist.app
```