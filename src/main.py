from flask import Flask

def create_app():
    #Create flask app object
    app = Flask(__name__)
    app.config.from_object("config.app_config")

    return app