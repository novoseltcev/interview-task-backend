from xml.etree import ElementTree

import requests

from app.entities.currency.schema import CurrencySchema


class CBRuAdapter:
    """Адаптер обращения к gRPS ЦБ РФ"""

    api_template = 'https://www.cbr.ru/scripts/{script_name}'

    def get_usd_currency(self):
        """Возвращает данные по доллару"""
        response = requests.get(self.api_template.format(script_name='XML_daily.asp'))
        xml_root = ElementTree.fromstring(response.content)
        for child in xml_root:
            if child.attrib['ID'] == 'R01235':
                return CurrencySchema().load({el.tag: el.text for el in child.iter()})
        raise ValueError
