from abc import ABC, abstractmethod
from typing import TypeVar, Iterable, NamedTuple

from .repository import Repository

T = TypeVar('T')


class Page(NamedTuple):
    items: Iterable[T]
    pages: int


class Service:
    def __init__(self, repository: Repository | None):
        self.repository = repository


class AbstractAuthService(ABC, Service):
    @property
    @abstractmethod
    def user(self):
        pass
