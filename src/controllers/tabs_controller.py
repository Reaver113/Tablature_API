from flask import Blueprint, jsonify, request
from main import db
from models.tabs import Tab
from schemas.tab_schema import tab_schema, tabs_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

tabs = Blueprint("tabs", __name__, url_prefix="/tabs")

# Query all artists
@tabs.route("/", methods =["GET"])
def get_tabs():
    tabs_list = Tab.query.all()
    result = tabs_schema.dump(tabs_list)
    return jsonify(result)