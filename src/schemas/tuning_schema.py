
from main import ma
from marshmallow import fields


class TuningSchema(ma.Schema):
    class Meta:
        fields = ("tuning_id", "name", "notes", "song")
        load_only = ("tuning_id")
    tabs = fields.List(fields.Nested("TabSchema", only = ("song",)))


tuning_schema = TuningSchema()
#multiple
tuning_schema = TuningSchema(many=True)