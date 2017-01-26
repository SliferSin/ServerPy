import ServerPy.Views.UserAPI
import sqlite3
import json
import DBClass
import paramiko,os #Control SSH
from ServerPy import app 
from flask import Flask,request


@app.route("/Sensor/Connect")#Realitza una connexió per SSH a la raspberry per moure l'arxiu
def Connect():
    ssh_server = "192.168.0.10"
    ssh_port = 22
    ssh_usuari = "pi"
    ssh_password = "raspberry"
    comanda = "scp "+ssh_usuari+"@"+ssh_server+":/home/pi/projecte/dades2.txt ./ServerPy/download/Entrades3.txt"
    
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ssh_server,ssh_port,ssh_usuari,ssh_password)

    ssh_client.exec_command(comanda)

    ssh_client.close()
    redirect(url_for('AddDades'))        
        

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