from typing import Iterable, Sequence

from app.rest_lib.service import Service
from .repository import OrderRepository, Order


class OrderService(Service):
    repository: OrderRepository

    def __init__(self, repository=OrderRepository()):
        super().__init__(repository)

    def replace(self, rows: Iterable[Iterable[str]]) -> None:
        self.repository.truncate()
        self.repository.insert(rows)
        self.repository.commit()

    def get_expired_deliveries(self) -> Sequence[Order]:
        return self.repository.get_all_expired_deliveries()
