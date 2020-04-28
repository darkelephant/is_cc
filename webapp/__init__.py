from flask import Flask
from flask_login import LoginManager, current_user, login_required

from webapp.db import db
from webapp.case.views import blueprint as case_blueprint
from webapp.dashboard.views import blueprint as dashboard_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.user.models import User


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(case_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(user_blueprint)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
