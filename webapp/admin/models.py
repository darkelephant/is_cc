# from webapp.db import db
from flask_login import current_user
from flask_admin import AdminIndexView
from flask import redirect, flash
from flask_admin.contrib.sqla import ModelView
# from flask_security import UserMixin, RoleMixin



class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.login == 'admin':
                return True

    def inaccessible_callback(self, name, **kwargs):
        # return redirect(url_for(dashboard.dashboard_index))
        flash('Эта страница только для администратора')
        return redirect('/')


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.set_password()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class UserModelView(BaseModelView, ModelView):
    pass


"""
# Flask-Security

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User2(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    # username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean(120))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(255))
"""