from flask import Blueprint
from main import db
from models.albums import Album
from models.artists import Artist
from models.instruments import Instrument
from models.tunings import Tuning
from models.tabs import Tab
from datetime import date

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


@db_commands.cli.command("seed")
def seed_db():
    #Seed artists
    artist1 = Artist(
        name = "Periphery",
        genre = "Metalcore"
    )
    artist2 = Artist(
        name = "Polyipha",
        genre = "Math Rock"
    )
    db.session.add(artist1)
    db.session.add(artist2)


    #Seed albums

    album1 = Album(
        name = "Periphery II",
        release = date(day = 29, month = 6, year = 2012)
    )
    album2 = Album(
        name = "Periphery III",
        release = date(day = 22, month = 7, year = 2016)
    )
    album3 = Album(
        name = "Periphery IV",
        release = date(day = 5, month = 4, year = 2019)
    )
    album4 = Album(
        name = "The Worst",
        release = date(day = 21, month = 7, year = 2017)
    )
    album5 = Album(
        name = "New Levels New Devils",
        release = date(day = 12, month = 10, year = 2018)
    )
    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.add(album5)
    db.session.commit()
    print("Tables Seeded")