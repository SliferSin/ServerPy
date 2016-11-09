import sqlite3
import json
import DBClass
from flask import Flask
from flask import request

app = Flask(__name__)

################
## API USUARI ##
################
@app.route("/User/Add", methods = ['POST']) #Afegir fila
def AddUser(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:
        if request.headers['Content-Type'] == 'application/json':
            usuario = request.json
            u = DBClass.User(usuario)
            c.execute("INSERT INTO Usuari VALUES (?,?,?,?,?)",[u.DNI,u.name,u.lastname,u.edat,u.sexe])
            conn.commit()    
    except sqlite3.Error as e:
        print("Error: ",e.args[0])

    conn.close()    
    return "Fila insertada"

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

################
## API SENSOR ##
################
@app.route("/Sensor/Add", methods = ['POST']) #Afegir fila
def AddSensor(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    
    try:   
        if request.headers['Content-Type'] == 'application/json':
            sens = request.json
            #s = Sensor(sens)
            s = DBClass.Sensor(sens)           
            c.execute("INSERT INTO Sensor VALUES (?,?,?)",[s.ID,s.ID_Propietari,s.ID_Usuari])
            conn.commit()    

    except sqlite3.Error as e:
        print("Error:",e.args[0])

    conn.close()    
    return "Fila insertada"

@app.route("/Sensor/Del", methods = ['DELETE']) #Elimina el Sensor
def DelSensor():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:
        if request.headers['Content-Type'] == 'application/json':
            sens = request.json
            s = DBClass.Sensor(sens)        
            c.execute("DELETE FROM Sensor WHERE ID = ?",[s.ID])
            conn.commit()    
    except sqlite3.Error as e:
        print("Error:",e.args[0])

    conn.close()    
    return "Fila eliminada"

#Canviar ID_USUARI
@app.route("/Sensor/Update",methods = ['PUT'])
def UpdateUsuari():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    try:
        if request.headers['Content-Type'] == 'application/json':
            sens = request.json
            s = DBClass.Sensor(sens)        
            print(s.ID)
            c.execute("UPDATE Sensor SET ID_Usuari = ? WHERE ID = ?",[s.ID_Usuari,s.ID])
            conn.commit()    
    except sqlite3.Error as e:
        print("Error:",e.args[0])

    conn.close()    
    return "200"

###############
## API DADES ##
###############
       
@app.route("/Dades/Add/", methods = ['POST']) #Afegir fila
def AddDades(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
    
    try:   
        if request.headers['Content-Type'] == 'application/json':
            data = request.json
            d = DBClass.Dades(data)
            c.execute("INSERT INTO Dades VALUES (?,?,?,?,?)",[d.ID_Sensor,d.Data,d.X,d.Y,d.Z])
            conn.commit()    

    except sqlite3.Error as e:
        print("Error:",e.args[0])

    conn.close()    
    return "Entrada insertada"

@app.route("/Dades/Del/", methods = ['DELETE']) #Eliminar fila
def DelDades():
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()

    try:   
        if request.headers['Content-Type'] == 'application/json':
            data = request.json
            d = DBClass.DelDades(data)

            c.execute("SELECT ID FROM Sensor WHERE Id_Usuari = ?",[d.ID_Usuari])
            ID_Sensor = c.fetchone()

            #Arreglar fecha para que sea s?lo del dia
            #c.execute("DELETE FROM Dades WHERE ID_Sensor = ? AND Data BETWEEN ? AND ? ",[ID_Sensor, d.Data,])
            conn.commit()    

    except sqlite3.Error as e:
        print("Error:",e.args[0])

    conn.close()    
    return "Entrada eliminada"

if __name__ == "__main__":   
    app.run(host='localhost', port='155')