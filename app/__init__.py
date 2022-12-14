from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_login import current_user, LoginManager, logout_user, login_required, UserMixin
from flask_login import login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from hashlib import sha256


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


from app.controller import indexController, userController
