from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist
from schemas.artist_schema import artist_schema, artists_schema

artists = Blueprint("artists", __name__, url_prefix="/artists")

@artists.route("/", methods =["GET"])
def get_artists():
    #Query all artists
    artists_list = Artist.query.all()
    result = artists_schema.dump(artists_list)
    return jsonify(result)



@artists.route("/<int:id>", methods =["GET"])
def get_artist(id):
    #Query an artist by id
    artist = Artist.query.get(id)
    result = artist_schema.dump(artist)
    return jsonify(result)


@artists.route("/", methods=["POST"])
def new_artist():
    artist_fields = artist_schema.load(request.json)
    artist = Artist(
        name = artist_fields["name"],
        genre = artist_fields["genre"],
        # ALBUMS TO BE ADDED
    )
    db.session.add(artist)
    db.session.commit()
    return jsonify(artist_schema.dump(artist))