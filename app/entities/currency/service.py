from typing import MutableMapping, Any

from app.rest_lib.service import Service
from .repository import CurrencyRepository, PK, Currency


class CurrencyService(Service):
    repository: CurrencyRepository

    def __init__(self, repository=CurrencyRepository()):
        super().__init__(repository)

    def merge(self, data: MutableMapping[str, Any]) -> None:
        pk = PK(num_code=data['num_code'])
        if not self.repository.get_by_pk(pk=pk):
            return self.repository.create(Currency(**data))
        del data['num_code']
        return self.repository.update(pk, data)


