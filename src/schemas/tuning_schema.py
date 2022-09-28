
from main import ma


class TuningSchema(ma.Schema):
    class Meta:
        feilds = ("tuning_id", "name", "notes")


tuning_schema = TuningSchema()
#multiple
tuning_schema = TuningSchema(many=True)