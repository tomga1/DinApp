from flask import Blueprint
from services.ingresos_services import crear_ingresos_services

ingresos = Blueprint('ingresos', __name__)

@ingresos.route('/', methods=['GET'])
def get_ingresos():
    return 'Get all todos'

@ingresos.route('/<id>', methods=['GET'])
def get_ingresos_id(id):
    return 'Get all todos by id'

@ingresos.route('/', methods=['POST'])
def create_ingresos():
    return crear_ingresos_services()

@ingresos.route('/<id>', methods=['PUT'])
def update_todo(id):
    return 'Update ingresos'

@ingresos.route('/<id>', methods=['DELETE'])
def delete_ingresos(id):
    return 'Delete ingreso by id'


