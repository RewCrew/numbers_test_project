from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from order_service.application import services

from .scheme import broker_scheme


def create_consumer(
    connection: Connection, orders: services.OrderService
) -> KombuConsumer:
    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        orders.add_order,
        'Queue',
    )

    return consumer
