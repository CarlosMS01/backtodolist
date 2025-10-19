from flask import Blueprint, request, jsonify, g
from database import supabase
from middleware.jwt_required import jwt_required
from utils.tasks_validators import validate_task_data

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
@jwt_required
def create_task():
    data = request.get_json()

    is_valid, error_response, status_code = validate_task_data(data)
    if not is_valid:
        return error_response, status_code

    title = data.get('title')
    description = data.get('description', '')
    status = data.get('status', 'pendiente')
    priority = data.get('priority', 'media')

    result = supabase.table("tasks").insert({
        "title": title,
        "description": description,
        "status": status,
        "priority": priority,
        "user_id": g.user_id
    }).execute()

    if not result.data:
        print("Supabase no devolvió datos al insertar")
        return jsonify({'error': 'Error al crear la tarea'}), 500

    return jsonify({'message': 'Tarea creada correctamente'}), 201

@tasks_bp.route('/tasks', methods=['GET'])
@jwt_required
def get_tasks():
    result = supabase.table("tasks").select("*").eq("user_id", g.user_id).execute()

    if not result.data:
        return jsonify({'error': 'Error al obtener tareas'}), 500

    return jsonify(result.data), 200
