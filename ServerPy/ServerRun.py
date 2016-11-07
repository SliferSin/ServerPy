from flask import Flask
import UserAPI
import SensorAPI
import DadesAPI

app = Flask(__name__)

if __name__ == "__main__":   
    app.run(host='localhost', port='155')