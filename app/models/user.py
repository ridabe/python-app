from sqlalchemy import create_engine
from . import config
from app import db
from app import app


class User():
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password      
        
    def GetAllUser():
        conn= db.engine(config.SQLALCHEMY_DATABASE_URI)
        users = conn.execute('select * from user')
        return users
    
    def __repr__(self):
        return '<User %r>' % self.name
        
        
