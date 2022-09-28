from main import db
from datetime import date

class Tab(db.Model):
    #define table name in DB
    __tablename__= "tabs"
    #set columns
    tab_id = db.Column(db.Integer, primary_key = True)
    artist = db.Column(db.Integer, db.ForeignKey("artists.artist_id"), nullable = False)
    album = db.Column(db.Integer, db.ForeignKey("albums.album_id"), nullable = False)
    song = db.Column(db.String(), nullable = False)
    instrument = db.Column(db.Integer, db.ForeignKey("instruments.instrument_id"), nullable = False)
    tuning = db.Column(db.Integer, db.ForeignKey("tunings.tuning_id"), nullable = False)
    uploaded_by = db.Column(db.Integer, nullable = False)
    uploaded_date = db.Column(db.Date(), nullable = False)
