import UserAPI
from datetime import datetime


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
        
        
@app.route("Dades/Add/", methods = ['POST']) #Afegir fila
def Add(): 
    conn = sqlite3.connect('IS.db')
    c = conn.cursor()
   
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        d = Dades(data)
        c.execute("INSERT INTO Dades VALUES (?,?,?,?,?)",[d.ID_Sensor,d.Data,d.X,d.Y,d.Z])
        conn.commit()    

    conn.close()    
    return "Entrada insertada"

@app.route("Dades/Del/", methods = ['DELETE'])
def Del():
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
