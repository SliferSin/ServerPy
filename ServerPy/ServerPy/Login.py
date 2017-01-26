import sqlite3
import DBClass
from flask import Flask,request,Response,session,redirect,url_for,render_template
from ServerPy import app 

#localhost:155/login?username="loquesea"&password="loquesea"
@app.route("/login", methods = ['GET','POST']) #Login or Register
def Login():     
     if request.method == 'GET': #Probar con request.form
        username = request.args.get('username')
        password = request.args.get('password')
        
        loguser = DBClass.LogUser(username,password)
        
        if loguser.VerifyLogin(): 
            session['username'] = username
            return redirect(url_for('index'))
        else:           
            return "Registrat com " + username + "<br>"

     else : #Registrar usuario            
        return redirect(url_for('Register'))        
        
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

@app.route('/register')
def Register():       
    return render_template('Register.html')

@app.route('/')
def Enviar():
    print("redirecting")
    return redirect(url_for('Connect'))

@app.route('/index')
def index():
    return render_template('log.html')
    