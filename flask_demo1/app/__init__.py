from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID


import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view('login')
oid = OpenID(app,os.path.join(basedir,'tmp'))


from app import views,models