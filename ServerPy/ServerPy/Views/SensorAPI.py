import ServerPy.Views.UserAPI
import sqlite3
import json
import DBClass
from ServerPy import app 
from flask import Flask,request

#Eliminar sensor
@app.route("/Sensor/Del", methods = ['DELETE'])
def DelSensor():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        sens = request.json
        s = Sensor(sens)        
        c.execute("DELETE FROM Sensor WHERE ID = ?",[s.ID])
        conn.commit()    

    conn.close()    
    return "Fila eliminada"