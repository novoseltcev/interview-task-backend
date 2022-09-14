from app import create_app


def main():
    """При наличии заказов с просроченными сроками доставки отправляет уведомление в чат-бота Telegram"""
    create_app()
    from app.adapters.telegram_bot import TelegramBotAdapter
    from app.entities.order.service import OrderService
    from app.config import config

    orders = OrderService().get_expired_deliveries()
    if len(orders) > 0:
        table_prefix = '\n\t'
        table_header = table_prefix + '№ заказа  |  Срок доставки' + \
                       table_prefix + '—————|———————'

        def create_row(order) -> str:
            divider = 2 * ' ' + '|' + 3 * ' '
            return 2 * ' ' + str(order.num_order) + divider + str(order.delivery_date)

        table_body = table_prefix + table_prefix.join(create_row(order=order) for order in orders)
        table = table_header + table_body

        TelegramBotAdapter().send_message(
            chat_id=config.TG_CHAT_ID,
            message=f'По {len(orders)} заказ{"у" if len(orders) == 1 else "ам"} задерживается доставка: {table}',
            is_quite=False
        )


if __name__ == '__main__':
    main()
