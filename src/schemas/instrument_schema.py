from main import ma
from marshmallow import fields

class InstrumentSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["instrument_id", "name", "strings"]
        load_only = ["instrument_id"]
    tabs = fields.List(fields.Nested("TabSchema", only = ("song",)))


#single schema
instrument_schema = InstrumentSchema()
#multiple
instrument_schema = InstrumentSchema(many=True)
