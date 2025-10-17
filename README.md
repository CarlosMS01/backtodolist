# 📝 Backend para ToDo List con Flask

Este proyecto es un backend seguro y modular para una aplicación de tareas (ToDo List). Incluye autenticación con JWT, registro de usuarios, y operaciones CRUD para gestionar tareas. Está diseñado para ser desplegado fácilmente y validado desde el frontend.

## 💻 Tecnologías utilizadas

### 🧱 Framework y lenguaje
- **Python 3.13.1** – Lenguaje principal
- **Flask 3.1.2** – Framework backend

### 📦 Librerías clave
- **Flask-Bcrypt** – Encriptación de contraseñas
- **Flask-SQLAlchemy** – ORM para base de datos
- **Flask-Cors** – Permitir peticiones desde frontend
- **python-dotenv** – Manejo de variables de entorno
- **PyJWT** – Autenticación con tokens JWT
- **psycopg2-binary** – Conexión con PostgreSQL
- **gunicorn 21.2.0** – Servidor WSGI para producción en Render

### 🛠️ Herramientas de desarrollo
- **Git** – Control de versiones
- **Postman** – Pruebas de endpoints
- **VS Code** – Editor de código

## 📦 Instalación local

```bash
git clone https://github.com/CarlosMS01/backtodolist.git
cd backtodolist

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## 🚀 Ejecución

```bash
python backtodolist/app.py
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
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
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
- `register()`: registra un nuevo usuario con los campos `email`, `password` y `username`.
- `me()`: obtiene el usuario correspondiente.
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
- `decode_token`: Verifica si un token JWT es válido y, si lo es, extrae el `user_id` del payload..

## 🔐 Seguridad y Validación

Este proyecto implementa validaciones robustas y pruebas automatizadas para prevenir ataques comunes como inyecciones SQL.

- Se validan campos como `email`, `password` y `username` antes de procesarlos.
- Se utiliza SQLAlchemy para evitar interpolación directa de datos en consultas.

---
