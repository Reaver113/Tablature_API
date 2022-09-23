from main import ma 

class AlbumSchema(ma.Schema):
    class Meta:
        fields = ["name", "release"]


#single schema
album_schema = AlbumSchema()
#multiple
albums_schema = AlbumSchema(many=True)
