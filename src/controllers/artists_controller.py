from flask import Blueprint, jsonify, request
from main import db
from models.artists import Artist
from schemas.artist_schema import artist_schema, artists_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError

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
        return{"Error": "Artist not found"}, 404
    result = artist_schema.dump(artist)
    return jsonify(result)

# Post an Artist
@artists.route("/", methods=["POST"])
@jwt_required()
def new_artist():
    if not "Moderator" in get_jwt_identity():
        if not "Uploader" in get_jwt_identity():
            return {"Error": "You do not have the credentials to complete this action"}, 401


    artist_fields = artist_schema.load(request.json)
    artist = Artist(
        name = artist_fields["name"],
        genre = artist_fields["genre"],
        # ALBUMS TO BE ADDED WITH FORIEGN KEY
    )
    db.session.add(artist)
    db.session.commit()
    return jsonify(artist_schema.dump(artist)), 201

# Delete an Artist
@artists.route("/<int:id>", methods = ["DELETE"])
@jwt_required()
def delete_artist(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}, 401
    artist = Artist.query.get(id)
    if not artist:
        return{"Error": "Artist not found"}, 404
    db.session.delete(artist)
    db.session.commit()
    return {"Message": "Artist deleted successfully"}, 202


# Update an artist
@artists.route("/<int:id>", methods = ["PUT"])
@jwt_required()
def update_artist(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}, 401
    artist = Artist.query.get(id)
    if not artist:
        return{"Error": "Artist not found"}, 404
    artist_fields = artist_schema.load(request.json)
    artist.name = artist_fields["name"]
    artist.genre = artist_fields["genre"]
    db.session.commit()
    return jsonify(artist_schema.dump(artist)), 201



@artists.errorhandler(ValidationError)
def artist_validation_error(error):
    return error.messages, 400