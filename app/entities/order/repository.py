from datetime import date
from typing import Iterable, Sequence

import sqlalchemy as sa
from flask_sqlalchemy import Pagination

from app.config import config
from app.db import db
from app.rest_lib.repository import Repository

from app.config import config
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
