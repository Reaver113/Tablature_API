from flask import Blueprint, jsonify, request
from main import db
from models.tabs import Tab
from schemas.tab_schema import tab_schema, tabs_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date
from marshmallow.exceptions import ValidationError

tabs = Blueprint("tabs", __name__, url_prefix="/tabs")

# Get all Tabs
@tabs.route("/", methods =["GET"])
def get_tabs():
    # QUERY SEARCHS
        #search by artist_id
    if request.args:
        if request.args.get("artist_id"):
            filtered_tabs_list = Tab.query.filter_by(artist_id = request.args.get("artist_id"))
            result = tabs_schema.dump(filtered_tabs_list)
            return jsonify(result)
            #search by album_id
        elif request.args.get("album_id"):
            filtered_tabs_list = Tab.query.filter_by(album_id = request.args.get("album_id"))
            result = tabs_schema.dump(filtered_tabs_list)
            return jsonify(result)
            #search by instrument_id
        elif request.args.get("instrument_id"):
            filtered_tabs_list = Tab.query.filter_by(instrument_id = request.args.get("instrument_id"))
            result = tabs_schema.dump(filtered_tabs_list)
            return jsonify(result)
            #search by tuning_id
        elif request.args.get("tuning_id"):
            filtered_tabs_list = Tab.query.filter_by(tuning_id = request.args.get("tuning_id"))
            result = tabs_schema.dump(filtered_tabs_list)
            return jsonify(result)
            #catch invalid searchs
        else: 
            return {"Error":"Invalid search parameters"}
    else:
        tabs_list = Tab.query.all()
        result = tabs_schema.dump(tabs_list)
        return jsonify(result)



@tabs.route("/<int:id>", methods =["GET"])
def get_tab(id):
    tabs = Tab.query.get(id)
    if not tabs:
        return{"Error": "Tab not found"}, 404
    result = tab_schema.dump(tabs)
    return jsonify(result)



# GET tab by its ID
@tabs.route("/", methods=["POST"])
@jwt_required()
def new_tab():
    if not "Moderator" in get_jwt_identity():
        if not "Uploader" in get_jwt_identity():
            return {"Error": "You do not have the credentials to complete this action"}, 401


    tab_fields = tab_schema.load(request.json)
    tab = Tab(
        artist_id = tab_fields["artist_id"],
        album_id = tab_fields["album_id"],
        song = tab_fields["song"], 
        instrument_id = tab_fields["instrument_id"],
        tuning_id = tab_fields["tuning_id"],
        user_id = get_jwt_identity().partition("-")[0],
        uploaded_date = date.today()

    )
    db.session.add(tab)
    db.session.commit()
    return jsonify(tab_schema.dump(tab)), 201


# Delete a Tab by its ID
@tabs.route("/<int:id>", methods = ["DELETE"])
@jwt_required()
def delete_tab(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}, 401
    tab = Tab.query.get(id)
    if not tab:
        return{"Error": "Tab not found"}, 404
    db.session.delete(tab)
    db.session.commit()
    return {"Message": "Tab removed successfully"}, 202


# Change information of a tab by its ID
@tabs.route("/<int:id>", methods = ["PUT"])
@jwt_required()
def update_tab(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}, 401
    tab = Tab.query.get(id)
    if not tab:
        return{"Error": "Tab not found"}, 404
    tab_fields = tab_schema.load(request.json)
    tab.artist = tab_fields["artist"]
    tab.album = tab_fields["album"]
    tab.song = tab_fields["song"]
    db.session.commit()
    return jsonify(tab_schema.dump(tab)), 201

# Error handeling
@tabs.errorhandler(ValidationError)
def tab_validation_error(error):
    return error.messages, 400