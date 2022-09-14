from typing import Iterable

from app.rest_lib.repository import Repository

from app.config import config
from .model import Order


class OrderRepository(Repository):
    def __init__(self, page_length: int = config.PAGE_LENGTH):
        super().__init__(model=Order)
        self.page_length = page_length

    def commit(self):
        self.session.commit()

    def truncate(self):
        self.session.execute(statement=f'TRUNCATE TABLE "{self.model.__tablename__}"')

    def insert(self, rows: Iterable[Iterable[str]]):
        statement = f'INSERT INTO "{self.model.__tablename__}" VALUES {self._compile_rows_to_values(rows=rows)}'
        self.session.execute(statement=statement)

    @staticmethod
    def _compile_rows_to_values(rows: Iterable[Iterable[str]]):
        return str(tuple(tuple(row) for row in rows))[1:-1]
