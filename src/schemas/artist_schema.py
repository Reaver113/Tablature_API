from main import ma
from marshmallow import fields
from schemas.album_schema import AlbumSchema


class ArtistSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["artist_id", "name", "genre", "albums"]
        load_only = ["artist_id"]
    albums = fields.List(fields.Nested(AlbumSchema, only = ("name", "release",)))


#single schema
artist_schema = ArtistSchema()
#multiple
artists_schema = ArtistSchema(many=True)
