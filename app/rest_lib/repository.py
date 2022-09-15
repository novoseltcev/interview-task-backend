from __future__ import annotations
from typing import Callable, NamedTuple, Any, Type, Iterable

from sqlalchemy import text
from sqlalchemy.orm import Session, Query, InstrumentedAttribute as Column
from sqlalchemy.ext.declarative import AbstractConcreteBase
from app.db import session

Model = Type[AbstractConcreteBase]


class Repository:
    """Абстрактный репозиторий - слой обращения к БД и ORM"""

    class PK(NamedTuple):
        ...

    def __init__(self, model: Model, filters: dict[str, Callable] = None):
        self._model = model
        self._filters = filters

    @property
    def session(self) -> Session:
        return session

    @property
    def model(self) -> Model:
        return self._model

    def pk_query(self, pk: PK, model: Model = None) -> Any:
        return self.query(model).filter_by(**pk._asdict())

    def query(self, model: Model = None, columns: Iterable[Column] = None) -> Query:
        result = self.session.query(model if model else self.model)
        if columns:
            result = self.session.query(*columns)
        Query.custom_filters = lambda query, *params, **kwargs: self.__custom_filters(query, *params, **kwargs)
        Query.custom_order_by = lambda query, *params, **kwargs: self.__custom_orders(query, *params, **kwargs)
        return result

    def __custom_filters(self, query: Query, filters: list) -> Query:
        result = query
        for key in filters:
            result = result.filter(self._filters[key]())
        return result

    @staticmethod
    def __custom_orders(query: Query, sort_by: str, reversed: bool) -> Query:
        prefix = 'DESC' if reversed else 'ASC'
        return query.order_by(text(sort_by + ' ' + prefix))
