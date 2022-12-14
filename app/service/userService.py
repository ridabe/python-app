from app import app
from app.models.user import getUserByEmailPass,insertUser, getUser

def postUserService(nome, email, pwd, is_adm=False):
    insert = insertUser(nome, email, pwd, is_adm)
    
    return insert
    
def getUserByEmailPassService(email, pwd):
    user = getUserByEmailPass(email, pwd) 
    
    return user

def getAllUserService():
    allUser = getUser()    
    return allUser