import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("La variable MONGO_URI no está definida en el .env")

mongo = PyMongo()

def init_app(app):
    """
    Llama a esto desde tu archivo principal (app.py o factory).
    Ejemplo:
       from config.mongodb import init_app, mongo
       app = Flask(__name__)
       init_app(app)
    """
    app.config["MONGO_URI"] = MONGO_URI
    mongo.init_app(app)
