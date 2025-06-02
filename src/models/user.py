from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.password_hash = user_data['password_hash']
        self.active = user_data.get('active', True)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

