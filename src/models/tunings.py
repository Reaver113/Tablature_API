from main import db

class Tuning(db.Model):
    #define table name in DB
    __tablname__="tunings"
    #set columns
    tuning_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    notes = db.Column(db.String())