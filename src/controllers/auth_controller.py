from datetime import timedelta
from flask import Blueprint, jsonify, request
from main import db, bcrypt, jwt
from flask_jwt_extended import create_access_token
from models.users import Username
from schemas.user_schema import username_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def register_user():
    #get user details from request
    user_fields = username_schema.load(request.json)

    #check if email is in db
    email = Username.query.filter_by(email=user_fields["email"]).first()
    if email:
        return {"Error": "Email already exists"}

    #check if username is in db
    user = Username.query.filter_by(username=user_fields["username"]).first()
    if user:
        return {"Error": "User already exists"}

    #create user object
    user = Username(
        username = user_fields["username"],
        email = user_fields["email"],
        password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8"),
        role = user_fields["role"]
    )

    #add user to db
    db.session.add(user)
    db.session.commit()

    #GENERATE ACCES TOKEN TO IDENTITY AND SET EXPIERY 
    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))

    return {"username": user.username, "token": token}