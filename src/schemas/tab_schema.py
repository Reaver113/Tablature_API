from main import ma
from marshmallow import fields
from schemas.user_schema import UsernameSchema
from schemas.tuning_schema import TuningSchema

class TabSchema(ma.Schema):
    class Meta:
        odered = True
        fields = ["artist", "album", "tuning", "instrument", "song", "uploaded_by", "uploaded_date"]
        load_only = ["tab_id",]
    artist = fields.Nested("ArtistSchema", only = ("name",))
    album = fields.Nested("AlbumSchema", only = ("name",))
    tuning = fields.List(fields.Nested(TuningSchema, only = ("name",)))
    uploaded_by = fields.List(fields.Nested(UsernameSchema, only = ("name",)))

#single schema
tab_schema = TabSchema()
#multiple
tabs_schema = TabSchema(many=True)