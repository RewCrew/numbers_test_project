from kombu import Connection
from sqlalchemy import create_engine

from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext

from order_service.adapters import orders_api, database, message_bus
from order_service.application import services


class Settings:
    db = database.Settings()
    orders_api = orders_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    order_repo = database.repositories.OrdersRepo(context=context)


class PublisherMessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Application:
    orders = services.OrderService(
        order_repo=DB.order_repo, publisher=PublisherMessageBus.publisher
    )
    is_dev_mode = Settings.orders_api.IS_DEV_MODE


class ConsumerMessageBus:
    consumer = message_bus.create_consumer(
        PublisherMessageBus.connection, Application.orders
    )

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(PublisherMessageBus.connection)


class Aspects:
    services.join_points.join(DB.context)
    orders_api.join_points.join(PublisherMessageBus.publisher, DB.context)


app = orders_api.create_app(
    orders=Application.orders, is_dev_mode=Application.is_dev_mode
)

if __name__ == "__main__":
    from wsgiref import simple_server

    with simple_server.make_server('', 8000, app=app) as server:
        server.serve_forever()
