# 📝 Backend para ToDo List con Flask

Este proyecto es un backend seguro y modular para una aplicación de tareas (ToDo List). Incluye autenticación con JWT, registro de usuarios, y operaciones CRUD para gestionar tareas. Está diseñado para ser desplegado fácilmente y validado desde el frontend.

## 🚀 Tecnologías utilizadas

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

## 📝 Estructura del proyecto

Este backend está organizado como paquete Python para blindar imports y facilitar despliegue.

- Cada carpeta contiene `__init__.py` para evitar errores de importación.
- Archivo .gitignore para evitar subir archivos innecesarios o sensibles al repositorio.

## Ejecución

```bash
python -m backtodolist.app
```