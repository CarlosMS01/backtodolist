from flask import Blueprint, request, jsonify, g
from database import supabase
from middleware.jwt_required import jwt_required
from utils.tasks_validators import validate_task_data

tasks_bp = Blueprint('tasks', __name__)

# ---------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------

@tasks_bp.route('/tasks', methods=['GET'])
@jwt_required
def get_tasks():
    result = supabase.table("tasks").select("*").eq("user_id", g.user_id).execute()

    if not result.data:
        return jsonify({'error': 'Error al obtener tareas'}), 404

    return jsonify(result.data), 200

# ---------------------------------------------------------------------------------------------

@tasks_bp.route('/tasks/<int:id>', methods=['GET'])
@jwt_required
def get_task(id):
    result = supabase.table("tasks").select("*").eq("id", id).eq("user_id", g.user_id).single().execute()

    if not result.data:
        return jsonify({'error': 'Tarea no encontrada'}), 404

    return jsonify(result.data), 200

# ---------------------------------------------------------------------------------------------

@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required
def update_task(id):
    data = request.get_json()

    is_valid, error_response, status_code = validate_task_data(data)
    if not is_valid:
        return error_response, status_code
    
    update_fields = {
        "title": data.get('title'),
        "description": data.get('description'),
        "status": data.get('status'),
        "priority": data.get('priority')
    }

    result = supabase.table("tasks").update(update_fields).eq("id", id).eq("user_id", g.user_id).execute()

    if not result.data:
        return jsonify({'error': 'Tarea no encontrada o no actualizada'}), 404

    return jsonify({'message': 'Tarea actualizada'}), 200

# ---------------------------------------------------------------------------------------------

@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required
def delete_task(id):
    result = supabase.table("tasks").delete().eq("id", id).eq("user_id", g.user_id).execute()

    if not result.data:
        return jsonify({'error': 'Tarea no encontrada o no eliminada'}), 404

    return jsonify({'message': 'Tarea eliminada'}), 200