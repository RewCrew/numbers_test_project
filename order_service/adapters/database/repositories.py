from typing import  Optional

from sqlalchemy import or_, select

from classic.components import component
from classic.sql_storage import BaseRepository

from order_service.application import interfaces
from order_service.application.dataclasses import Order


@component
class OrdersRepo(BaseRepository, interfaces.OrderRepo):

    def add(self, order: Order):
        self.session.add(order)
        self.session.flush()
        self.session.refresh(order)
        return order

    def get_by_id(self, id_: int) -> Optional[Order]:
        query = select(Order).where(Order.order_id == id_)
        return self.session.execute(query).scalars().one_or_none()



    def get_or_create(self, order: Order) -> Order:
        if order.order_id is None:
            self.add(order)
        else:
            new_order = self.get_by_id(order.order_id)
            if new_order is None:
                self.add(order)
            else:
                if order == new_order:
                    order = new_order
                else:
                    new_order.date, new_order.id, new_order.price_rub, new_order.price_us = order.date, order.id, order.price_rub, order.price_us
                    self.session.add(new_order)
                    self.session.commit()
        return order



    def get_all(self):
        orders = self.session.query(Order).order_by(Order.order_id).all()
        return orders

    def delete(self, id:int):
        self.session.query(Order).filter(Order.order_id == id).delete()
        self.session.commit()



