from main import db

class Tab(db.Model):
    #define table name in DB
    __tablename__= "tabs"
    #set columns
    tab_id = db.Column(db.Integer, primary_key = True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.artist_id"), nullable = False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.album_id"), nullable = False)
    song = db.Column(db.String(), nullable = False)
    instrument_id = db.Column(db.Integer, db.ForeignKey("instruments.instrument_id"), nullable = False)
    tuning_id = db.Column(db.Integer, db.ForeignKey("tunings.tuning_id"), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
    uploaded_date = db.Column(db.Date(), nullable = False)