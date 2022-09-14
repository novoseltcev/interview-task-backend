from typing import Iterable

import requests


class GoogleSpreadsheetsAdapter:
    api_template = 'https://sheets.googleapis.com/{version}/spreadsheets/{suffix}'

    def __init__(self, access_key: str, version: str = 'v4'):
        self.key = access_key
        self.version = version

    def get_data(self, id: str, range: str) -> Iterable[Iterable[str]]:
        suffix = f'{id}/values/{range}/?key={self.key}'
        vals = requests.get(self.api_template.format(version=self.version, suffix=suffix)).json()['values'][1:]
        return (('-'.join(cell.split('.')[::-1]) if i == 3 else cell for i, cell in enumerate(row)) for row in vals)
