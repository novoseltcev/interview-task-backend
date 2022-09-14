from app import create_app
from app.adapters.central_bank import CBRuAdapter
from app.entities.currency.service import CurrencyService


def main():
    create_app()
    usd_currency = CBRuAdapter().get_usd_currency()
    CurrencyService().merge(data=usd_currency)


if __name__ == '__main__':
    main()
