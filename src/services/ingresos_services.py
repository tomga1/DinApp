from flask import request, jsonify
from config.mongodb import mongo
from datetime import datetime

def crear_ingresos_services():
    data = request.get_json() or {}

    #extraer y validar los campos necesarios

    fecha_str = data.get('fecha')
    try:
        fecha = datetime.fromisoformat(fecha_str) if fecha_str else datetime.utcnow()
    except ValueError:
        return jsonify({"error": "Formato de fecha inválido"}), 400

    title = data.get('title')
    if not title:
        return jsonify({"error": "El campo 'title' es obligatorio"}), 400
    

    ingreso = {
        'title': title,
        'description': data.get('description'),
        'monto': data.get('monto'),
        'id_usuario': data.get('id_usuario'),
        'observacion': data.get('observacion', ''),
        'fecha': fecha,
        'done': False
    }

    response = mongo.db.ingresos.insert_one(ingreso)
    ingreso['_id'] = str(response.inserted_id)
    ingreso['fecha'] = ingreso['fecha'].isoformat()

    return jsonify(ingreso), 201


