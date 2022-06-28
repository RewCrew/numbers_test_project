import click

from order_service.composites import order_loader


def create_cli(MessageBus):

    @click.group()
    def cli():
        pass

    @cli.command()
    def get_orders():
        orders = order_loader.get_order()
        return orders

    @cli.command()
    def consumer():
        MessageBus.declare_scheme()
        MessageBus.consumer.run()

    return cli
