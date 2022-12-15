from app import app, render_template, request, db, sha256, login_manager, jsonify, redirect, url_for, flash, login_user, UserMixin,logout_user, login_required
from app.service.userService import postUserService, getUserByEmailPassService, getAllUserService
import json

@app.route('/get-user')
def GetAllUser():    
    return render_template('base.html')

@app.route("/cadastrar", methods=["GET","POST"])
def cadastrar():    
    nome = request.form['userName']
    email = request.form['email']
    pwd = request.form['pwd']
    pwd = sha256(pwd.encode())
    pwd = pwd.hexdigest()
    
    postUserService(nome, email, pwd)   
    
    flash(f'Usuario {nome} cadastrado com sucesso!!') 
    return render_template('auth/login.html')

    
@app.route("/logar", methods=["GET","POST"])
def logar():
   
        email = request.form['email']
        pwd = request.form['pwd']
        pwd = sha256(pwd.encode())
        pwd = pwd.hexdigest()
        
        user = getUserByEmailPassService(email, pwd)        
        
        if user and user.password == pwd:
            login_user(user)            
            return redirect(url_for('project'))                 
            
        else : 
            flash('Login Invalido!')
            return render_template('auth/login.html') 
        
@app.route('/alluser')
@login_required 
def allUser():
    response = getAllUserService()
    return render_template("interno/list_user.html", user=response)  

    
@app.route('/logout')
def logout():
    logout_user()
    flash('Você esta deslogado!')
    return render_template('auth/login.html')
    