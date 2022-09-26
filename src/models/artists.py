from main import db

class Artist(db.Model):
    #define table name in DB
    __tablename__= "artists"
    #set columns
    artist_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)
    genre = db.Column(db.String(), nullable = False)
    album_id = db.relationship(
        "Album",
        backref = "artist"
    )

