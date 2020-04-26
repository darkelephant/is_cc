from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'base_app.db')
SECRET_KEY = 'TOP_SECRET_KEY'
REMEMBER_COOKIE_DURATION = timedelta(days=1)

SQLALCHEMY_TRACK_MODIFICATIONS = False

VERSION = '0.0.1'
