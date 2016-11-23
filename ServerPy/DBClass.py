import json
import sqlite3
from flask import Response

##############
###        ###
###  DADES ###
###        ###
##############
#Estructura per afegir les dades
class Dades(object):
    def __init__(self, j):
        self.Data = j['Data']
        self.ID_Sensor = j['ID_Sensor']        
        self.X = j['X']
        self.Y = j['Y']
        self.Z = j['Z']
    
#Estructura per eliminar a partir del sensor
class DelDades(object):
    def __init__(self, j):
        self.ID_Usuari = j['ID_Usuari']
        self.Data = j['Data']

###############
###         ###
###  SENSOR ###
###         ###
###############
class Sensor(object):
    def __init__(self, j):
        self.ID = j['ID']
        self.ID_Propietari = j['ID_Propietari']
        self.ID_Usuari = j['ID_Usuari']


###############
###         ###
###  USUARI ###
###         ###
###############
#Estructura per afegir usuari
class User(object):
    def __init__(self, j):
        self.DNI = j['DNI']
        self.name = j['Name']
        self.lastname = j['LastName']
        self.age = j['Age']
        self.gender = j['Gender']        

#Estructura per eliminar usuari
class DelUser(object):
    def __init__(self,j):
        self.DNI = j['DNI']

#Estructura per obtenir dades mitjançant un DNI

class GetUser(object):
    def __init__(self, j):
        self.DNI = j[0]
        self.name = j[1]
        self.lastname = j[2]
        self.age = j[3]
        self.x = j[4]
        self.y = j[5]
        self.z = j[6]
        self.data = j[7]
        self.ID_Sensor = j[8]

#Metode Send per retornar la informació en format JSON    
    def Send(self):
        data = {
            "DNI": self.DNI,
            "Name": self.name,
            "LastName": self.lastname,
            "Age":self.age,
            "X":self.x,
            "Y":self.y,
            "Z":self.z,
            "Data":self.data,
            "ID_Sensor":self.ID_Sensor        
        }
        js = json.dumps(data)
        resp = Response(js,status=200, mimetype='application/json')    
        return resp

class LogUser(object):
    def __init__(self,name,password):
        self.name = name    
        self.password = password

    def VerifyLogin(self):
        conn = sqlite3.connect('IS.db')
        c = conn.cursor()
        try:
            c.execute("SELECT name FROM Usuari WHERE password = ?",[self.password])
            conn.commit()    
            nameDB = c.fethone()
        except sqlite3.Error as e:
            print("Error: ",e.args[0])
        
        conn.close()

        if nameDB == self.name:
                return True
        else: 
                return False

        
        