from main import ma
from marshmallow import fields
from schemas.tab_schema import TabSchema

class AlbumSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artist", "artist_id", "album_id", "name", "release", "tabs", "tab_id"]
        load_only = ["album_id", "artist_id",]
    artist = fields.Nested("ArtistSchema", only = ("name",))
    tabs = fields.List(fields.Nested(TabSchema, only = ("song",)))


#single schema
album_schema = AlbumSchema()
#multiple
albums_schema = AlbumSchema(many=True)
