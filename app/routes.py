from flask import Flask

from app.entities.order.controller import OrderController, OrderChartController


def register_routes(app: Flask):
    api_prefix = ''

    orders_view = OrderController.as_view('orders')
    app.add_url_rule(api_prefix + '/orders', view_func=orders_view, methods=['GET'])

    chart_view = OrderChartController.as_view('chart')
    app.add_url_rule(api_prefix + '/orders/chart', view_func=chart_view, methods=['GET'])
