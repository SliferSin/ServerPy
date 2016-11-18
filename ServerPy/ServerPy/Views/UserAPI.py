import sqlite3
import json
import DBClass
from flask import Flask,request,Response
from ServerPy import app 

@app.route("/User/Add", methods = ['POST']) #Afegir fila
def AddUser(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:
        if request.headers['Content-Type'] == 'application/json':
            usuario = request.json
            u = DBClass.User(usuario)
            c.execute("INSERT INTO Usuari VALUES (?,?,?,?,?)",[u.DNI,u.name,u.lastname,u.age,u.gender])
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

@app.route('/User/GetInfo',methods = ['GET']) #Consultar usuari
def GetUser():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:
        if request.headers['Content-Type'] == 'application/json':
            uDNI = request.args.get('DNI')
            c.execute("SELECT u.DNI,u.Nom,u.Cognom,u.Edat,d.X,d.Y,d.Z,d.data,d.ID_Sensor FROM Usuari u, Dades d WHERE u.DNI = ?",[uDNI])
            info_usuari = c.fetchone()
            info = DBClass.GetUser(info_usuari)
            resp = info.Send()            
        
    except sqlite3.Error as e:
        print("Error:",e.args[0])
    
    conn.close()
    return resp