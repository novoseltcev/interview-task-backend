from marshmallow import fields, Schema, EXCLUDE, post_load, pre_dump
from marshmallow.validate import Range


class PageSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    page = fields.Integer(required=False, load_only=True, load_default=1, validate=Range(min=1))

    @post_load
    def unpack(self, data, **kwargs):
        return data['page']


class OrderSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.String()
    num_order = fields.String()
    cost = fields.String()
    delivery_date = fields.String()
    rubble_cost = fields.String()


class OrderChartSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    x = fields.Date(required=True, dump_only=True)
    y = fields.Float(required=True, dump_only=True)

    @pre_dump
    def parse(self, data, **kwargs):
        return dict(x=data[0], y=data[1])
