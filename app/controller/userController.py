from app import app, render_template, request, db
from app.models.user import insertUser


@app.route('/get-user')
def GetAllUser():    
    return render_template('base.html')

@app.route("/cadastrar", methods=["GET","POST"])
def cadastrar():    
    nome = request.form['userName']
    email = request.form['email']
    pwd = request.form['pwd']
    
    insert = insertUser(nome, email, pwd)   
    
    return render_template('auth/login.html', response=nome)