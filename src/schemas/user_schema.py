from main import ma
from marshmallow.validate import Length 

class UsernameSchema(ma.Schema):
    class Meta:
        feilds = ("username", "email", "password", "role")

    password = ma.String(validate=Length(min=8))

username_schema = UsernameSchema()

usernames_schema = UsernameSchema(many=True)