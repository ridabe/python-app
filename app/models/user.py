from app import db
from app.repository.userRepository import User

def insertUser(userName, email, password):
    insert = User(nome = userName, email = email, password= password)
    db.session.add(insert)
    db.session.commit()
        
        
