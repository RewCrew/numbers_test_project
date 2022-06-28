from sqlalchemy.orm import registry

from order_service.application import dataclasses

from . import tables

mapper = registry()

mapper.map_imperatively(dataclasses.Order, tables.orders)

