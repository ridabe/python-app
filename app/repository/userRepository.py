from app import db, login_manager, login_user, UserMixin

@login_manager.user_loader
def load_user(user_id):
        return User.query.filter_by(id=user_id).first()
    
class User(UserMixin, db.Model):        
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(80), unique=False, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(120), unique=True, nullable=False)
        is_adm= db.Column(db.Boolean, default=False)
        
        def __init__(self, nome, email, password, is_adm):
            self.nome = nome
            self.email = email
            self.password = password
            self.is_adm = is_adm
    

        def __repr__(self):
            return '<User %r>' % self.id