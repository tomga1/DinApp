from flask import Blueprint
from services.auth_services.auth_services import login_services, register_services 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    return login_services()


@auth.route('/register', methods=['POST'])
def register():
    return register_services()