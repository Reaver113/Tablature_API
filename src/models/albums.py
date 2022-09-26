from main import db

class Album(db.Model):
    #define table name in DB
    __tablename__= "albums"
    #set columns
    album_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    release = db.Column(db.Date(), nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"), nullable = False)
