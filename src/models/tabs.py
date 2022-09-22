from main import db

class Tab(db.Model):
    #define table name in DB
    __tablname__="tabs"
    #set columns
    tab_id = db.Column(db.Integer, primary_key = True)
    artist = db.Column(db.Integer) #foriegn key
    song = db.Column(db.String())
    type = db.Column(db.Integer()) #foriegn key
    tuning = db.Column(db.Integer) #foriegn key
    uploaded = db.Column(db.Integer) #foriegn key
