from order_service.adapters.cli import create_cli
from order_service.composites.app_api import ConsumerMessageBus

cli = create_cli(ConsumerMessageBus)
