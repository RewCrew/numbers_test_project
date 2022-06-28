from abc import ABC, abstractmethod

from .dataclasses import Order


class OrderRepo(ABC):

    @abstractmethod
    def add(self, order: Order):
        pass

    @abstractmethod
    def get_or_create(self, order: Order):
        pass

    @abstractmethod
    def get_by_id(self, id_: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, id:int):
        pass



