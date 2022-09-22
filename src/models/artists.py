from main import db

class Artist(db.Model):
    #define table name in DB
    __tablename__= "artists"
    #set columns
    artist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    genre = db.Column(db.String())
    albums = db.Column(db.Integer) #foriegn key

