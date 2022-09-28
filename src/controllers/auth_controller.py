from datetime import timedelta
from flask import Blueprint, jsonify, request
from main import db, bcrypt, jwt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.users import Username
from schemas.user_schema import username_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
@jwt_required()
def register_user():
    if not "Moderator" in get_jwt_identity():
        return {"Error": "You do not have the credentials to complete this action"}
    #get user details from request
    user_fields = username_schema.load(request.json)

    #check if email is in db
    email = Username.query.filter_by(email=user_fields["email"]).first()
    if email:
        return {"Error": "Email already exists"}

    #check if username is in db
    user = Username.query.filter_by(username=user_fields["username"]).first()
    if user:
        return {"Error": "Username already exists"}

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

# Login Process
@auth.route("/login", methods = ["POST"])
def login_user():

    
    # Get username and password from request
    user_fields = username_schema.load(request.json)

    # Check username exists and password is valid
    user = Username.query.filter_by(username=user_fields["username"]).first()
    if not user:
        return {"Error": "Username not found"}
    if not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return {"Error": "Password not found"}

        # If credentials are valid generate token and return to user based on role
    elif user.role == "Moderator":
        token = create_access_token(identity=str(user.user_id) + ("-Moderator"), expires_delta=timedelta(days=1))
        return {"username": user.username, "role": user.role, "token": token, "message": "You are now logged in as a Moderator"}
    elif user.role == "Uploader":
        token = create_access_token(identity=str(user.user_id) + ("-Uploader"), expires_delta=timedelta(days=1))
        return {"username": user.username, "role": user.role, "token": token, "message": "You are now logged in as an Uploader"}
    elif user.role == "Standard":
        token = create_access_token(identity=str(user.user_id) + ("-Standard"), expires_delta=timedelta(days=1))
        return {"username": user.username, "role": user.role, "token": token, "message": "You are now logged in as a standard user"}


