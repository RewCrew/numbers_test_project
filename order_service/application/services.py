import datetime
from time import sleep

import gspread
from pycbrf import ExchangeRates
from datetime import datetime

from classic.app import DTO
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Message, Publisher


from . import interfaces
from .dataclasses import Order

join_points = PointCut()
join_point = join_points.join_point


class OrderInfo(DTO):
    id: str
    order_id: str
    price_us: str
    date: str
    price_rub: float





@component
class OrderService:
    order_repo: interfaces.OrderRepo
    publisher: Publisher

    @join_point
    def add_order(self, data:dict):
        order_info = OrderInfo(**data)
        new_order = order_info.create_obj(Order)
        order = self.order_repo.get_or_create(new_order)
        self.order_repo.add(order)



    @join_point
    def get_orders(self, info):
        gc = gspread.service_account_from_dict(info)
        sh = gc.open("test")
        worksheet = sh.worksheet('Лист1')
        list_of_dicts = worksheet.get_all_records()

        for i in list_of_dicts:
            date = datetime.strptime(i['срок поставки'], "%d.%m.%Y").strftime('%Y-%m-%d')
            i['стоимость в рублях'] = round(float(ExchangeRates(date)['USD'].value) * i['стоимость,$'], 2)
            sleep(0.1)
            order = {}
            order['id']=i['№']
            order['order_id']=i['заказ №']
            order['price_us']=i['стоимость,$']
            order['date']=i['срок поставки']
            order['price_rub']=i['стоимость в рублях']
            self.publisher.publish(
                Message('Exchange', {"data":order}))

        sleep(2)
        orders_in_db = list(self.order_repo.get_all())
        orders_in_db2=list([int(order.order_id) for order in orders_in_db])
        orders_in_google = list([order['заказ №'] for order in list_of_dicts])
        list_to_delete = list(set(orders_in_db2) - set(orders_in_google))
        for order_id in list_to_delete:
            self.order_repo.delete(order_id)

