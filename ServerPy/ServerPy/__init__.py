from flask import Flask
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

import ServerPy.Views.DadesAPI
import ServerPy.Views.SensorAPI
import ServerPy.Views.UserAPI
import DBClass