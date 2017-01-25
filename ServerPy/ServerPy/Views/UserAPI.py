import sqlite3
import json
import DBClass
from flask import Flask,request,Response,redirect,url_for,render_template,send_file
from ServerPy import app 
from datetime import datetime


@app.route("/User/AddUser", methods = ['POST']) #Afegir fila
def AddUser(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()    
    try:          
        usuario = request.json                                   
        u = DBClass.User(usuario)                 
        c.execute("INSERT INTO Usuari VALUES (?,?,?,?,?,?)",[u.DNI,u.name,u.lastname,u.age,u.password,u.gender])
        conn.commit()    
    except sqlite3.Error as e:        
        print("Error: ",e.args[0])

    conn.close()
    data = {
                "DNI":u.DNI
    }
    js = json.dumps(data)
    resp = Response(js,status=200, mimetype='application/json')    
    return resp    

@app.route("/User/Del",methods = ['DELETE']) #Eliminar fila
def DelUser():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:
        if request.headers['Content-Type'] == 'application/json':
            usuario = request.json
            u = DBClass.DelUser(usuario) 
            c.execute("DELETE FROM Usuari WHERE DNI = ?",[u.DNI])
        conn.commit()
    except sqlite3.Error as e:
        print("Error:",e.args[0])
    conn.close()        
    return "Fila eliminada"

#localhost:155/User/GetInfo?DNI=1234
@app.route('/User/GetInfo',methods = ['GET']) #Consultar usuari
def GetUser():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:        
        uDNI = request.args.get('DNI')        
        c.execute("SELECT u.DNI,u.Nom,u.Cognom,u.Edat,d.ID_Sensor FROM Usuari u, Dades d,Sensor s WHERE u.DNI = ?",[uDNI])
        info_usuari = c.fetchone()
        info = DBClass.GetUser(info_usuari)
        resp = info.Send()            
        
    except sqlite3.Error as e:
        print("Error:",e.args[0])
    
    conn.close()
    return resp

#localhost:155/User/GetFile?DNI=1234
@app.route('/User/GetFile',methods = ['GET']) #Obtenir fitxer per lectura en octave
def GetFile():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()        
    try:
        uDNI = request.args.get('DNI')            
        startDate = request.args.get('Data')
        endDate = request.args.get('Data2')  
        
        sql = "SELECT u.DNI,u.Nom,u.Cognom,u.Edat,d.ID_Sensor FROM Usuari u, Dades d WHERE u.DNI = ? and d.Data between ? and ?"
        
        c.execute(sql,[uDNI,startDate,endDate])
        info_usuari = c.fetchone()
        info = DBClass.GetUser(info_usuari)
        
        info.CreateFile(startDate,endDate)       
        
    except sqlite3.Error as e:
        print("Error:",e.args[0])
    
    conn.close()
    return render_template("DownloadFile.html")

@app.route('/file')
def File():
    return render_template('UserDetail.html')

#Descarregar el fitxer de dades
@app.route('/download/dades.txt')
def download():        
    return send_file("./download/dades.txt")