from app import create_app


def main():
    "Обновляет курс рубля к доллару"

    create_app()
    from app.adapters.central_bank import CBRuAdapter
    from app.entities.order.service import OrderService

    order_service = OrderService()
    order_service.currency_service.merge(
        data=CBRuAdapter().get_usd_currency()
    )
    order_service.update_costs()


if __name__ == '__main__':
    main()
