from app import create_app


def main():
    "Обновляет курс рубля к доллару"

    create_app()
    from app.adapters.central_bank import CBRuAdapter
    from app.entities.currency.service import CurrencyService

    CurrencyService().merge(
        data=CBRuAdapter().get_usd_currency()
    )


if __name__ == '__main__':
    main()
