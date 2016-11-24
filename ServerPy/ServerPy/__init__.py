from flask import Flask,redirect,url_for
import os

app = Flask(__name__)

#Secret Key necesitada pel objecte session
app.secret_key = os.urandom(24)

import ServerPy.Views.DadesAPI
import ServerPy.Views.SensorAPI
import ServerPy.Views.UserAPI
import ServerPy.Login
import ServerPy.Templates
import DBClass