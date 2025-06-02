from flask import request, jsonify
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash
from models.user import User
from config.mongodb import mongo

def login_services():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_data = mongo.db.users.find_one({"username": username})
    if user_data and check_password_hash(user_data['password_hash'], password):
        user = User(user_data)
        login_user(user)
        return jsonify({"message": "Login exitoso!", "user_id": user.id}), 200
    return jsonify({"message": "Nombre de usuario o contraseña incorrectos"}), 401

def register_services():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if mongo.db.users.find_one({"username": username}):
        return jsonify({"message": "El nombre de usuario ya existe"}), 400
    
    password_hash = generate_password_hash(password)
    user = {
        "username": username,
        "password_hash": password_hash,
    }
    mongo.db.users.insert_one(user)
    return jsonify({"message": "Usuario registrado exitosamente"}), 201