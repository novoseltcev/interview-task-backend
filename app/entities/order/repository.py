from datetime import date
from typing import Iterable, Sequence

import sqlalchemy as sa
from flask_sqlalchemy import Pagination

from app.config import config
from app.db import db
from app.rest_lib.repository import Repository
from app.rest_lib.service import Page

from .model import Order


class OrderRepository(Repository):
    model: Order

    def __init__(self, page_length: int = config.PAGE_LENGTH):
        super().__init__(model=Order)
        self.page_length = page_length

    def commit(self):
        self.session.commit()

    def truncate(self):
        self.session.execute(statement='TRUNCATE TABLE ' + self.model.__tablename__)

    def insert(self, rows: Iterable[Iterable[str]]):
        self.session.execute(
            statement=(
                db.metadata.tables[self.model.__tablename__]
                .insert()
                .values(tuple(rows))
            )
        )

    def update_rubble_costs(self, rate: float):
        self.query().update(dict(rubble_cost=rate * Order.cost))

    def get_all_expired_deliveries(self) -> Sequence[Order]:
        return self.query().filter(self.model.delivery_date < date.today()).order_by(sa.desc(Order.delivery_date)).all()

    def get_rubble_page(self, page: int) -> Page[Order]:
        pagination: Pagination = (
            self.query(Order)
            .paginate(page, self.page_length, error_out=False)
        )
        return Page(items=pagination.items, pages=pagination.pages)

    def get_sum_by_date_with_total(self) -> list[tuple[Order.delivery_date, Order.rubble_cost]]:
        return (
            self.query(columns=(Order.delivery_date, sa.func.sum(Order.rubble_cost)))
            .group_by(sa.func.rollup(Order.delivery_date))
            .order_by(Order.delivery_date)
            .all()
        )
