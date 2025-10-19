from flask import jsonify

def validate_task_data(data):
    if not data:
        return False, jsonify({'error': 'No se enviaron datos'}), 400

    title = data.get('title')
    if not title or not isinstance(title, str) or not title.strip():
        return False, jsonify({'error': 'El título es obligatorio y debe ser un texto'}), 400

    description = data.get('description', '')
    if not isinstance(description, str):
        return False, jsonify({'error': 'La descripción debe ser un texto'}), 400

    valid_statuses = ['pendiente', 'en progreso', 'completada']
    status = data.get('status', 'pendiente')
    if status not in valid_statuses:
        return False, jsonify({'error': f"El estado debe ser uno de: {', '.join(valid_statuses)}"}), 400

    valid_priorities = ['baja', 'media', 'alta']
    priority = data.get('priority', 'media')
    if priority not in valid_priorities:
        return False, jsonify({'error': f"La prioridad debe ser una de: {', '.join(valid_priorities)}"}), 400

    return True, None, None
