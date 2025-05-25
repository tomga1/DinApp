from flask import Blueprint
from services.ingresos_services.ingesos_services import crear_ingresos_services, get_all_ingresos, get_ingreso_xid , update_ingreso_id , delete_ingreso_id

ingresos = Blueprint('ingresos', __name__)

@ingresos.route('/get_all_ingresos', methods=['GET'])
def get_ingresos():
    return get_all_ingresos()

@ingresos.route('/get_ingreso_xid/<id>', methods=['GET'])
def get_ingresos_id(id):
    return get_ingreso_xid(id)

@ingresos.route('/', methods=['POST'])
def create_ingresos():
    return crear_ingresos_services()

@ingresos.route('/update_ingreso/<id>', methods=['PUT'])
def update_todo(id):
    return update_ingreso_id(id)

@ingresos.route('/delete_ingreso_id/<id>', methods=['DELETE'])
def delete_ingresos(id):
    return delete_ingreso_id(id)


