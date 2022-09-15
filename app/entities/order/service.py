from typing import Iterable, Sequence, NamedTuple

from app.entities.currency.service import CurrencyService
from app.rest_lib.service import Service
from .repository import OrderRepository, Page, Order


class Chart(NamedTuple):
    groups: list[tuple[Order.delivery_date, Order.rubble_cost]]
    total: float


class OrderService(Service):
    repository: OrderRepository

    def __init__(self, repository=OrderRepository()):
        super().__init__(repository)
        self.currency_service = CurrencyService()

    def get_page(self, page: int) -> Page[Order]:
        return self.repository.get_rubble_page(page=page)

    def get_chart_data(self) -> Chart:
        groups = self.repository.get_sum_by_date_with_total()
        return Chart(groups=groups[:-1], total=groups[-1][-1])

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
