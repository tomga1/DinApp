# app.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_cors import CORS
from flask_login import LoginManager
from config.mongodb import init_app, mongo
from routes.ingresos import ingresos
from routes.auth import auth
from bson.objectid import ObjectId
from models.user import User

load_dotenv()

app = Flask(__name__)
app.secret_key = 'clave_secreta'
init_app(app) 
CORS(app)

login_manager = LoginManager()
login_manager.login_view =  'login'
login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data:
        return User(user_data)
    return None


app.register_blueprint(ingresos, url_prefix='/ingresos')
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
