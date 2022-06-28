
import attr


@attr.dataclass
class Order:
    id: int
    order_id: int
    price_us: int
    date: str
    price_rub : float

