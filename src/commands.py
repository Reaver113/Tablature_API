from flask import Blueprint
from main import db, bcrypt
from models.albums import Album
from models.artists import Artist
from models.instruments import Instrument
from models.tunings import Tuning
from models.tabs import Tab
from models.users import Username
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
    db.session.commit()
    print("artists created")


    #Seed albums

    album1 = Album(
        name = "Periphery II",
        release = date(day = 29, month = 6, year = 2012),
        artist = artist1
    )
    album2 = Album(
        name = "Periphery III",
        release = date(day = 22, month = 7, year = 2016),
        artist = artist1
    )
    album3 = Album(
        name = "Periphery IV",
        release = date(day = 5, month = 4, year = 2019),
        artist = artist1
    )
    album4 = Album(
        name = "The Worst",
        release = date(day = 21, month = 7, year = 2017),
        artist = artist2
    )
    album5 = Album(
        name = "New Levels New Devils",
        release = date(day = 12, month = 10, year = 2018),
        artist = artist2
    )
    
    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.add(album4)
    db.session.add(album5)
    db.session.commit()
    print("albums created")

    #Seed tunings
    tuning1 = Tuning(
        name = "E Standard",
        notes = "E,A,D,G,B,E"
    )
    tuning2 = Tuning(
        name = "Drop D",
        notes = "D,A,D,G,B,E"
    )
    tuning3 = Tuning(
        name = "Drop C",
        notes = "C,G,C,F,A,D"
    )
    db.session.add(tuning1)
    db.session.add(tuning2)
    db.session.add(tuning3)
    db.session.commit()
    print("tunings created")

    #Seed instruments
    instruments1 = Instrument(
        name = "Guitar",
        strings = "6"
    )
    instruments2 = Instrument(
        name = "Bass",
        strings = "4"
    )
    instruments3 = Instrument(
        name = "Guitar",
        strings = "7"
    )
    instruments4 = Instrument(
        name = "Guitar",
        strings = "8"
    )
    db.session.add(instruments1)
    db.session.add(instruments2)
    db.session.add(instruments3)
    db.session.add(instruments4)
    db.session.commit()
    print("instruments created")

    #Seed Users
    user1 = Username(
        username = "Reaver113",
        email = "test@gmail.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8"),
        role = "Standard"
    )
    user2 = Username(
        username= "Tabmin",
        email = "tabmin@gmail.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8"),
        role = "Moderator"
        )
    user3 = Username(
        username = "Andy",
        email = "andy@gmail.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8"),
        role = "Uploader"
    )
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
    print("Users created")

    #seed tabs
    tab1 = Tab(
        artist = artist1,
        album = album1,
        song = "Froggin Bullfish",
        instrument = instruments2,
        tuning = tuning3,
        uploaded_by = user3,
        uploaded_date = date.today()
    )
    tab2 = Tab(
        artist = artist1,
        album = album1,
        song = "Scarlet",
        instrument = instruments1,
        tuning = tuning3,
        uploaded_by = user3,
        uploaded_date = date.today()
    )
    tab3 = Tab(
        artist = artist1,
        album = album2,
        song = "The way the news goes",
        instrument = instruments3,
        tuning = tuning1,
        uploaded_by = user3,
        uploaded_date = date.today()
    )
    tab4 = Tab(
        artist = artist2,
        album = album5,
        song = "G.O.A.T",
        instrument = instruments1,
        tuning = tuning1,
        uploaded_by = user3,
        uploaded_date = date.today()
    )
    tab5 = Tab(
        artist = artist2,
        album = album5,
        song = "Yass (ft. Chon)",
        instrument = instruments1,
        tuning = tuning1,
        uploaded_by = user2,
        uploaded_date = date.today()
    )
    tab6 = Tab(
        artist = artist2,
        album = album5,
        song = "So Strange (ft. Cuco)",
        instrument = instruments1,
        tuning = tuning1,
        uploaded_by = user2,
        uploaded_date = date.today()
    )
    tab7 = Tab(
        artist = artist2,
        album = album4,
        song = "The Worst",
        instrument = instruments1,
        tuning = tuning1,
        uploaded_by = user2,
        uploaded_date = date.today()
    )
    tab8 = Tab(
        artist = artist2,
        album = album4,
        song = "Icronic",
        instrument = instruments1,
        tuning = tuning1,
        uploaded_by = user2,
        uploaded_date = date.today()
    )
    
    
    db.session.add(tab1)
    db.session.add(tab2)
    db.session.add(tab3)
    db.session.add(tab4)
    db.session.add(tab5)
    db.session.add(tab6)
    db.session.add(tab7)
    db.session.add(tab8)



    
    #commit to db
    db.session.commit()
    print("tabs created")
    print("Tables Seeded")