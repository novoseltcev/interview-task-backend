from typing import MutableMapping, Any

from app.errors import NoSuchEntityError
from app.rest_lib.service import Service
from .repository import CurrencyRepository, PK, Currency


class CurrencyService(Service):
    repository: CurrencyRepository

    def __init__(self, repository=CurrencyRepository()):
        super().__init__(repository)

    def get_by_name(self, name: str) -> Currency:
        entity = self.repository.get_by_char_code(char_code=name)
        if not entity:
            raise NoSuchEntityError()
        return entity

    def merge(self, data: MutableMapping[str, Any]) -> None:
        pk = PK(num_code=data['num_code'])
        if not self.repository.get_by_pk(pk=pk):
            return self.repository.create(Currency(**data))

        del data['num_code']
        self.repository.update(pk, data)
