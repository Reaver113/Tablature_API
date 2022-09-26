from main import ma
from marshmallow import fields


class ArtistSchema(ma.Schema):
    class Meta:
        fields = ["name", "genre", "album_id", "albums"]
        load_only = ["album_id"]



#single schema
artist_schema = ArtistSchema()
#multiple
artists_schema = ArtistSchema(many=True)
