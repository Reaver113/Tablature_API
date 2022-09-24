from main import db

class Tuning(db.Model):
    #define table name in DB
    __tablename__= "tunings"
    #set columns
    tuning_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable = False)
    notes = db.Column(db.String(), nullable = False)