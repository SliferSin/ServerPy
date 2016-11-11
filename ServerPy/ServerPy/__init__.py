from flask import Flask

app = Flask(__name__)

import ServerPy.Views.DadesAPI
import ServerPy.Views.SensorAPI
import ServerPy.Views.UserAPI
import DBClass