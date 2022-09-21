from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    #Create flask app object
    app = Flask(__name__)
    app.config.from_object("config.app_config")

    db = SQLAlchemy(app)

    return app