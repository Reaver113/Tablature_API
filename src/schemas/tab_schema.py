from main import ma
from marshmallow import fields
from schemas.user_schema import UsernameSchema
from schemas.tuning_schema import TuningSchema
from schemas.instrument_schema import InstrumentSchema

class TabSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["song", "uploaded_by", "tuning", "instrument", "uploaded_date", "artist", "album",]
        load_only = ["tab_id",]
    artist = fields.Nested("ArtistSchema", only = ("name",))
    album = fields.Nested("AlbumSchema", only = ("name",))
    instrument = fields.Nested(InstrumentSchema, only = ("name",))
    tuning = fields.Nested(TuningSchema, only = ("name", "notes",))
    uploaded_by = fields.Nested(UsernameSchema, only = ("username",))

#single schema
tab_schema = TabSchema()
#multiple
tabs_schema = TabSchema(many=True)