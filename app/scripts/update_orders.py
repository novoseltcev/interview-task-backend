from app import create_app


def main():
    """Синхронизация заказов в БД с сервисом "Google Таблица" """
    create_app()
    from app.adapters.google_spreadsheet import GoogleSpreadsheetsAdapter
    from app.entities.order.service import OrderService
    from app.config import config

    OrderService().replace(
        rows=GoogleSpreadsheetsAdapter().get_data(
            id=config.GOOGLE_SPREADSHEET_ID,
            range='A:D'
        )
    )


if __name__ == '__main__':
    main()
