from main import ma
from marshmallow import fields
from schemas.artist_schema import ArtistSchema

class AlbumSchema(ma.Schema):
    class Meta:
        fields = ["name", "release", "artist_id", "artist"]
        load_only = ["artist_id"]
    artist = fields.Nested(ArtistSchema)


#single schema
album_schema = AlbumSchema()
#multiple
albums_schema = AlbumSchema(many=True)
