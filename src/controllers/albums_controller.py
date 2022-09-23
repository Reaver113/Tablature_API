from flask import Blueprint, jsonify, request
from main import db
from models.albums import Album
from schemas.album_schema import album_schema, albums_schema

albums = Blueprint("albums", __name__, url_prefix="/albums")

@albums.route("/", methods =["GET"])
def get_albums():
    #Query all albums
    albums_list = Album.query.all()
    result = albums_schema.dump(albums_list)
    return jsonify(result)


@albums.route("/<int:id>", methods =["GET"])
def get_album(id):
    #Query an album by id
    album = Album.query.get(id)
    result = album_schema.dump(album)
    return jsonify(result)

@albums.route("/", methods=["POST"])
def new_album():
    album_fields = album_schema.load(request.json)
    album = Album(
        name = album_fields["name"],
        release = album_fields["release"]
    )
    db.session.add(album)
    db.session.commit()
    return jsonify(album_schema.dump(album))