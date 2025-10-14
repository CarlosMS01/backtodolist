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
├── models.py
├── README.md
├── requirements.txt
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

---

## 🚀 Despliegue en Render para este proyecto

Esta sección describe cómo desplegar correctamente el backend en Render, asegurando compatibilidad, modularidad y seguridad.

### 📦 Requisitos previos del proyecto
- Repositorio en GitHub con los siguientes archivos en la raíz:
  - `app.py` con instancia `app`
  - `requirements.txt` con dependencias
  - `.gitignore` excluyendo `.env`

## 🧭 Pasos para desplegar este proyecto

1. Crear el servicio en Render
  - Accede a `Render Dashboard`
  - Haz clic en **"New Web Service"**
  - Selecciona **"Deploy from a Git repository"**
  - Conecta tu cuenta de GitHub y elige el repositorio
2. Configurar el entorno
  - **Name:** `backtodolist`
  - **Environment:** `Python 3`
  - **Branch:** `main`
  - **Root Directory:** (déjar vacío si los archivos están en la raíz)
  - Build Command:
  ```bash
  pip install -r requirements.txt
  ```
  - Start Command:
  ```bash
  gunicorn app:app
  ```
3. Agregar variables de entorno
En la sección Environment Variables, agrega:
| Variable           | Valor (ejemplo)                          |
|--------------------|------------------------------------------|
| DATABASE_URL       | postgres://usuario:clave@host/db         |
| JWT_SECRET_KEY     | clave_segura_123                         |
Esta tabla es perfecta para la sección de configuración de variables de entorno en Render.
4. Desplegar y validar
  - Render instalará dependencias y ejecutará el backend con Gunicorn
  - Accede a la URL pública que Render genera
  - El endpoint / debe responder con:
  ```bash
  To-Do List API funcionando. Versión actual: Octubre 2025
  ```

---

## 🛠️ Troubleshooting: Despliegue en Render

Para que el proyecto funcione correctamente en Render los `imports` deben verse asi:
```python
from database import init_app
```
Esto permite que Python reconozca los módulos correctamente desde la raíz del proyecto.
