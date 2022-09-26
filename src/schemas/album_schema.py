from main import ma
from marshmallow import fields

class AlbumSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["album_id", "name", "release", "artist"]
        load_only = ["album_id"]
    artist = fields.Nested("ArtistSchema", only = ("name",))


#single schema
album_schema = AlbumSchema()
#multiple
albums_schema = AlbumSchema(many=True)
