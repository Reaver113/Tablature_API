from main import ma 

class ArtistSchema(ma.Schema):
    class Meta:
        fields = ["name", "genre", "albums"]


#single schema
artist_schema = ArtistSchema()
#multiple
artists_schema = ArtistSchema(many=True)
