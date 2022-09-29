from main import ma
from marshmallow import fields
from schemas.user_schema import UsernameSchema
from schemas.tuning_schema import TuningSchema

class TabSchema(ma.Schema):
    class Meta:
        odered = True
        fields = ["song","uploaded_by", "uploaded_date", "artist", "album",]
        load_only = ["tab_id",]
    artist = fields.Nested("ArtistSchema", only = ("name",))
    album = fields.Nested("AlbumSchema", only = ("name",))
    #tuning = fields.Nested(TuningSchema, only = ("notes",))
    uploaded_by = fields.Nested(UsernameSchema, only = ("username",))

#single schema
tab_schema = TabSchema()
#multiple
tabs_schema = TabSchema(many=True)