from classic.http_api import App
from classic.http_auth import Authenticator

from order_service.adapters.orders_api import auth
from order_service.application import services


def create_app(
    is_dev_mode: bool,
    orders: services.OrderService,
) -> App:
    authenticator = Authenticator(app_groups=auth.ALL_GROUPS)

    if is_dev_mode:
        authenticator.set_strategies(auth.dummy_strategy)
    else:
        authenticator.set_strategies(auth.jwt_strategy)

    app = App(prefix='/api')

    return app
