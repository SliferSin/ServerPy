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
        self.edat = j['Edat']
        self.sexe = j['Sexe']        

#Estructura per eliminar usuari
class DelUser(object):
    def __init__(self,j):
        self.DNI = j['DNI']

