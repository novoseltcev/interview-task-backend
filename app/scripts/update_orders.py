from app import create_app
from app.adapters.google_spreadsheet import GoogleSpreadsheetsAdapter
from app.entities.order.service import OrderService


def main():
    app = create_app()
    adapter = GoogleSpreadsheetsAdapter(access_key=app.config.get('GOOGLE_API_KEY'))
    OrderService().replace(
        rows=adapter.get_data(
            id=app.config.get('GOOGLE_SPREADSHEET_ID'),
            range='A:D'
        )
    )


if __name__ == '__main__':
    main()
