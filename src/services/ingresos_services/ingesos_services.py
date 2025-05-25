from flask import request, jsonify, Response
from config.mongodb import mongo
from datetime import datetime
from bson import json_util, ObjectId

def crear_ingresos_services():
    data = request.get_json() or {}

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


def get_all_ingresos():
    data = mongo.db.ingresos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def get_ingreso_xid(id):
    data = mongo.db.ingresos.find_one({"_id": ObjectId(id)})
    result = json_util.dumps(data)
    if not data:
        return jsonify({"error": "Ingreso no encontrado"}), 404
    return Response(result, mimetype='application/json')


def update_ingreso_id(id):
    data = request.get_json() or {}
    if not data:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

    response = mongo.db.ingresos.update_one({'_id': ObjectId(id)}, {'$set': data})

    if response.modified_count >= 1:
        return jsonify({"message": "Ingreso actualizado exitosamente"}), 200
    else:
        return jsonify({"error": "No se encontró el ingreso o no se realizaron cambios"}), 404    
    

def delete_ingreso_id(id):
    response = mongo.db.ingresos.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return jsonify({"message": "Ingreso eliminado exitosamente"}), 200
    else:
        return jsonify({"error": "No se encontró el ingreso"}), 404