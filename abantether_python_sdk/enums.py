from enum import Enum, unique


@unique
class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


@unique
class Method(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
