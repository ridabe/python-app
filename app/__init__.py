from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

# app.config['APPNAME'] = config.APPNAME



# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:algo#2023@44.197.13.55/algoritmum'

login_manager = LoginManager(app)

from app.controller import userController
