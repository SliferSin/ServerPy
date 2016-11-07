import UserAPI
import sqlite3
import json
import DBClass
from flask import Flask
from flask import request

app = Flask(__name__)

#Eliminar sensor
@app.route("/Sensor/Del", methods = ['DELETE'])
def Del():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        sens = request.json
        s = Sensor(sens)        
        c.execute("DELETE FROM Sensor WHERE ID = ?",[s.ID])
        conn.commit()    

    conn.close()    
    return "Fila insertada"