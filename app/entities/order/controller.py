from flask import jsonify

from app.rest_lib.controller import Controller

from .service import OrderService
from .schema import PageSchema, OrderSchema, OrderChartSchema


class OrderController(Controller):
    service: OrderService

    def __init__(self, service=OrderService()):
        super().__init__(service=service)

    def get(self):
        orders, pages = self.service.get_page(
            page=PageSchema().load(self.args)
        )
        return jsonify(
            data=OrderSchema(many=True, exclude=('cost', )).dump(orders),
            meta={'pages': pages}
        )


class OrderChartController(Controller):
    service: OrderService

    def __init__(self, service=OrderService()):
        super().__init__(service=service)

    def get(self):
        chart, total = self.service.get_chart_data()
        return jsonify(
            data=OrderChartSchema(many=True).dump(chart),
            meta={'total': total}
        )
