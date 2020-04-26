from flask import Flask

from webapp.db import db
from webapp.dashboard.views import blueprint as dashboard_blueprint
from webapp.case.views import blueprint as case_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    app.register_blueprint(case_blueprint)
    app.register_blueprint(dashboard_blueprint)

    return app
