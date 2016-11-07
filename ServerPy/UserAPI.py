import sqlite3
import json
from flask import Flask
from flask import request

app = Flask(__name__)

#Estructura per afegir usuari
class User(object):
    def __init__(self, j):
        self.DNI = j['DNI']
        self.name = j['Name']
        self.lastname = j['LastName']
        self.edat = j['Edat']
        self.sexe = j['Sexe']        

#Estructura per eliminar usuari
class DelUser(object):
    def __init__(self,j):
        self.DNI = j['DNI']

@app.route("/User/Add", methods = ['POST']) #Afegir fila
def Add(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        usuario = request.json
        u = User(usuario)
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
            u = DelUser(usuario) 
            c.execute("DELETE FROM Usuari WHERE DNI = ?",[u.DNI])
        conn.commit()
    except sqlite3.Error as e:
        print("Error:",e.args[0])
    conn.close()        
    return "Fila eliminada"

if __name__ == "__main__":   
    app.run(host='localhost', port='155')