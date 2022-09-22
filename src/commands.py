from flask import Blueprint
from main import db
from models.albums import Album
from models.artists import Artist
from models.instruments import Instrument
from models.tunings import Tuning
from models.tabs import Tab

db_commands = Blueprint("db", __name__)

#Command makes SQLAlchemy create all tables for all models in physical DB
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables Created")


#Command makes SQLAlchemy drop all tables
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables Dropped")