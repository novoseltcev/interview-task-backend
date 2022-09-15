from typing import Iterable, Sequence

from app.entities.currency.service import CurrencyService
from app.rest_lib.service import Service
from .repository import OrderRepository, Order


class OrderService(Service):
    repository: OrderRepository

    def __init__(self, repository=OrderRepository()):
        super().__init__(repository)
        self.currency_service = CurrencyService()

    def update_costs(self) -> None:
        self.repository.update_rubble_costs(
            rate=self.currency_service.get_by_name('USD').exchange_rate()
        )
        self.repository.commit()

    def replace(self, rows: Iterable[Sequence[str]]) -> None:
        currency = self.currency_service.get_by_name('USD')

        self.repository.truncate()
        self.repository.insert(
            ((*row, float(row[2]) * currency.exchange_rate()) for row in rows)
        )
        self.repository.commit()

    def get_expired_deliveries(self) -> Sequence[Order]:
        return self.repository.get_all_expired_deliveries()
