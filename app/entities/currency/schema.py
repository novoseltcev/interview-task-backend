from marshmallow import Schema, fields, EXCLUDE, post_load, pre_load
from stringcase import snakecase


class CurrencySchema(Schema):
    class Meta:
        unknown = EXCLUDE

    num_code = fields.Integer()
    char_code = fields.String()
    nominal = fields.Integer()
    name = fields.String()
    value = fields.String()

    @pre_load
    def to_snakecase(self, data, **kwargs):
        return {snakecase(key): value for key, value in data.items()}

    @post_load
    def calculate_exchange_rate(self, data, **kwargs):
        data['value'] = float(data['value'].replace(',', '.'))
        return data
