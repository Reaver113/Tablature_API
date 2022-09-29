from flask import Blueprint, jsonify, request
from main import db
from models.tabs import Tab
from schemas.tab_schema import tab_schema, tabs_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date

tabs = Blueprint("tabs", __name__, url_prefix="/tabs")

@tabs.route("/", methods =["GET"])
def get_tabs():
    tabs_list = Tab.query.all()
    result = tabs_schema.dump(tabs_list)
    return jsonify(result)


@tabs.route("/<int:id>", methods =["GET"])
def get_tab(id):
    tabs = Tab.query.get(id)
    if not tabs:
        return{"Error": "Tab not found"}
    result = tab_schema.dump(tabs)
    return jsonify(result)




@tabs.route("/", methods=["POST"])
@jwt_required()
def new_tab():
    print(get_jwt_identity())
    if not "Moderator" in get_jwt_identity():
        if not "Uploader" in get_jwt_identity():
            return {"Error": "You do not have the credentials to complete this action"}


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
    return jsonify(tab_schema.dump(tab))


@tabs.route("/<int:id>", methods = ["DELETE"])
@jwt_required()
def delete_tab(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}
    tab = Tab.query.get(id)
    if not tab:
        return{"Error": "Tab not found"}
    db.session.delete(tab)
    db.session.commit()
    return {"Message": "Tab removed successfully"}



@tabs.route("/<int:id>", methods = ["PUT"])
@jwt_required()
def update_tab(id):
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}
    tab = Tab.query.get(id)
    if not tab:
        return{"Error": "Tab not found"}
    tab_fields = tab_schema.load(request.json)
    tab.artist = tab_fields["artist"]
    tab.album = tab_fields["album"]
    tab.song = tab_fields["song"]
    db.session.commit()
    return jsonify(tab_schema.dump(tab))