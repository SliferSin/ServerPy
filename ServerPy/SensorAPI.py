import UserAPI
import sqlite3
import json
from flask import Flask
from flask import request

app = Flask(__name__)

class Sensor(object):
    def __init__(self, j):
        self.ID = j['ID']
        self.ID_Propietari = j['ID_Propietari']
        self.ID_Usuari = j['ID_Usuari']
        
@app.route("/Sensor/Add", methods = ['POST']) #Afegir fila
def Add(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        sens = request.json
        s = Sensor(sens)
        c.execute("INSERT INTO Sensor VALUES (?,?,?)",[s.ID,s.ID_Propietari,s.ID_Usuari])
        conn.commit()    

    conn.close()    
    return "Fila insertada"

#Eliminar sensor
@app.route("Sensor/Del", methods = ['DELETE'])
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