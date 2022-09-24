from typing import Container
from main import ma
from marshmallow.validate import Length, OneOf, Email

class UsernameSchema(ma.Schema):
    class Meta:
        feilds = ("username", "email", "password", "role")

    username = ma.String(validate=Length(min=3))
    password = ma.String(validate=Length(min=8))
    email = ma.String(validate=Email())
    role = ma.String(validate=OneOf(choices=("Standard", "Uploader", "Moderator")))


username_schema = UsernameSchema()

usernames_schema = UsernameSchema(many=True)