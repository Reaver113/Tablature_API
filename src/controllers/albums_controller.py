from flask import Blueprint, jsonify, request
from main import db
from models.albums import Album
from schemas.album_schema import album_schema, albums_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

albums = Blueprint("albums", __name__, url_prefix="/albums")
# Query all albums
@albums.route("/", methods =["GET"])
def get_albums():
    albums_list = Album.query.all()
    result = albums_schema.dump(albums_list)
    return jsonify(result)

# Query an album by id
@albums.route("/<int:id>", methods =["GET"])
def get_album(id):
    album = Album.query.get(id)
    if not album:
        return{"Error": "Album not found"}
    result = album_schema.dump(album)
    return jsonify(result)


# Post an album
@albums.route("/", methods=["POST"])
@jwt_required()
def new_album():
    print(get_jwt_identity())
    if not "Moderator" in get_jwt_identity():
        if not "Uploader" in get_jwt_identity():
            return {"Error": "You do not have the credentials to complete this action"}


    album_fields = album_schema.load(request.json)
    album = Album(
        name = album_fields["name"],
        release = album_fields["release"]
    )
    db.session.add(album)
    db.session.commit()
    return jsonify(album_schema.dump(album))

# Delete an album
@albums.route("/<int:id>", methods = ["DELETE"])
@jwt_required()
def delete_album(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}
    album = Album.query.get(id)
    if not album:
        return{"Error": "Album not found"}
    db.session.delete(album)
    db.session.commit()
    return {"Message": "Album removed successfully"}


# Update an album
@albums.route("/<int:id>", methods = ["PUT"])
@jwt_required()
def update_album(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}
    album = Album.query.get(id)
    if not album:
        return{"Error": "Album not found"}
    album_fields = album_schema.load(request.json)
    album.name = album_fields["name"]
    album.genre = album_fields["release"]
    db.session.commit()
    return jsonify(album_schema.dump(album))