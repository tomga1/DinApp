from flask import Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from limiter import limiter
from services.auth_services.auth_services import login_services, register_services 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    return login_services()


@auth.route('/register', methods=['POST'])
def register():
    return register_services()