import ServerPy.Views.UserAPI
import sqlite3
import json
import DBClass
from ServerPy import app 
from flask import Flask,request
from datetime import datetime
       
@app.route("/Dades/Add/", methods = ['POST']) #Afegir fila
def AddDades(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        d = Dades(data)
        c.execute("INSERT INTO Dades VALUES (?,?,?,?,?)",[d.ID_Sensor,d.Data,d.X,d.Y,d.Z])
        conn.commit()    

    conn.close()    
    return "Entrada insertada"

@app.route("/Dades/Del/", methods = ['DELETE'])
def DelDades():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        d = DelDades(data)

        c.execute("SELECT ID FROM Sensor WHERE Id_Usuari = ?",[d.ID_Usuari])
        ID_Sensor = c.fetchone()

        #Arreglar fecha para que sea s?lo del dia
        #c.execute("DELETE FROM Dades WHERE ID_Sensor = ? AND Data BETWEEN ? AND ? ",[ID_Sensor, d.Data,])
        conn.commit()    

    conn.close()    
    return "Entrada eliminada"
