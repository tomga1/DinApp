# config/mongodb.py
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo

# 1) Carga el .env
load_dotenv()

# 2) Obtiene la URI
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("La variable MONGO_URI no está definida en el .env")

# 3) Crea la extensión (pero no aún ligada a la app)
mongo = PyMongo()

def init_app(app):
    """
    Llama a esto desde tu archivo principal (app.py o factory).
    Ejemplo:
       from config.mongodb import init_app, mongo
       app = Flask(__name__)
       init_app(app)
    """
    # Configura la URI en Flask
    app.config["MONGO_URI"] = MONGO_URI
    # Inicializa la extensión
    mongo.init_app(app)
