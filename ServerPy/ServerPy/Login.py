import sqlite3
import DBClass
from flask import Flask,request,Response,session
from ServerPy import app 

@app.route("/login", methods = ['GET','POST']) #Loggin or Register
def Login():
     if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        loguser = DBClass.LogUser(username,password)
        try:
            if loguser.VerifyLogin(): #Hacer función que compruebe que es correcta la relación user-pass
                session['username'] = username

     else : #Registrar usuario
        session['username'] = request.arg.get('username')
        
