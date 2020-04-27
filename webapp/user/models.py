from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(32), nullable=False)
    nick = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    role = db.Column(db.Integer, index=True)
    superuser = db.Column(db.Integer)
    foto = db.Column(db.String(64))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'

    def __repr__(self):
        return "<Пользователь: {}, ID: {}>".format(self.login, self.id)
