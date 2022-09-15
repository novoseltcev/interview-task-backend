from typing import Mapping, Any, NamedTuple

from app.rest_lib.repository import Repository
from .model import Currency


class PK(NamedTuple):
    num_code: int


class CurrencyRepository(Repository):
    def __init__(self) -> None:
        super().__init__(model=Currency)

    def get_by_pk(self, pk: PK) -> Currency:
        return self.pk_query(pk=pk).first()

    def create(self, entity: Currency) -> None:
        self.session.add(entity)
        self.session.commit()

    def update(self, pk: PK, data: Mapping[str, Any]) -> None:
        self.pk_query(pk=pk).update(data)
        self.session.commit()

    def get_by_char_code(self, char_code: str) -> Currency:
        return self.query().filter(Currency.char_code == char_code).first()

