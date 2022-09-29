
from main import ma
from marshmallow import fields


class TuningSchema(ma.Schema):
    class Meta:
        feilds = ("tuning_id", "name", "song", "notes")
        tabs = fields.List(fields.Nested("TabSchema", only = ("song",)))


tuning_schema = TuningSchema()
#multiple
tuning_schema = TuningSchema(many=True)