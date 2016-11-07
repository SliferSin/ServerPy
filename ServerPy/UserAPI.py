import sqlite3
import json
import DBClass
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/User/Add", methods = ['POST']) #Afegir fila
def Add(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        usuario = request.json
        u = DBClass.User(usuario)
        c.execute("INSERT INTO Usuari VALUES (?,?,?,?,?)",[u.DNI,u.name,u.lastname,u.edat,u.sexe])
        conn.commit()    

    conn.close()    
    return "Fila insertada"

@app.route("/Del",methods = ['DELETE']) #Eliminar fila
def Delete():
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

@app.route("/Sensor/Add", methods = ['POST']) #Afegir fila
def AddSensor(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        sens = request.json
        #s = Sensor(sens)
        s = DBClass.Sensor(sens)
        c.execute("INSERT INTO Sensor VALUES (?,?,?)",[s.ID,s.ID_Propietari,s.ID_Usuari])
        conn.commit()    

    conn.close()    
    return "Fila insertada"


if __name__ == "__main__":   
    app.run(host='localhost', port='155')