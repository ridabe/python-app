from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# login_manager = LoginManager(app)


from app.controller import indexController, userController
