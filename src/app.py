# app.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv

from config.mongodb import init_app, mongo
from routes.ingresos import ingresos


load_dotenv()

app = Flask(__name__)
init_app(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-db')
def test_db():
    try:
        mongo.db.test_collection.insert_one({"mensaje": "conexión exitosa"})
        return "✅ Conexión a MongoDB exitosa"
    except Exception as e:
        return f"❌ Error conectando a MongoDB: {str(e)}", 500

app.register_blueprint(ingresos, url_prefix='/ingresos')

if __name__ == '__main__':
    app.run(debug=True)
