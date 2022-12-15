from app import db, select
from app.repository.userRepository import User
import json

def insertUser(userName, email, password, is_adm):
    insert = User(nome = userName, email = email, password = password, is_adm = is_adm)
    db.session.add(insert)
    db.session.commit()   
    
def getUserByEmailPass(email, password):
    getUser = User.query.filter_by(email = email, password = password).first()    
    return getUser 

def getUser():
    user = db.session.query(User.nome, User.email, User.is_adm).all()
    return user

        
        
