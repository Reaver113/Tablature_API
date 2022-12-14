from main import db

class Instrument(db.Model):
    #define table name in DB
    __tablename__= "instruments"
    #set columns
    instrument_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable = False)
    strings = db.Column(db.Integer, nullable = False)
    tabs = db.relationship(
        "Tab",
        backref = "instrument"
    )