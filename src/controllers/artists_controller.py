from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist
from schemas.artist_schema import artist_schema, artists_schema

artists = Blueprint("artists", __name__, url_prefix="/artists")

# Query all artists
@artists.route("/", methods =["GET"])
def get_artists():
    artists_list = Artist.query.all()
    result = artists_schema.dump(artists_list)
    return jsonify(result)


# Query an Artist by id
@artists.route("/<int:id>", methods =["GET"])
def get_artist(id):
    artist = Artist.query.get(id)
    if not artist:
        return{"Error": "Artist not found"}
    result = artist_schema.dump(artist)
    return jsonify(result)

# Post and Artist
@artists.route("/", methods=["POST"])
def new_artist():
    artist_fields = artist_schema.load(request.json)
    artist = Artist(
        name = artist_fields["name"],
        genre = artist_fields["genre"],
        # ALBUMS TO BE ADDED WITH FORIEGN KEY
    )
    db.session.add(artist)
    db.session.commit()
    return jsonify(artist_schema.dump(artist))

# Delete an Artist
@artists.route("/<int:id>", methods = ["DELETE"])
def delete_artist(id):
    artist = Artist.query.get(id)
    if not artist:
        return{"Error": "Artist not found"}
    db.session.delete(artist)
    db.session.commit()
    return {"Message": "Artist deleted successfully"}


# Update an artist
@artists.route("/<int:id>", methods = ["PUT"])
def update_artist(id):
    artist = Artist.query.get(id)
    if not artist:
        return{"Error": "Artist not found"}
    artist_fields = artist_schema.load(request.json)
    artist.name = artist_fields["name"]
    artist.genre = artist_fields["genre"]
    db.session.commit()
    return jsonify(artist_schema.dump(artist))