from enum import Enum, unique


@unique
class RequestMethod(str, Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


@unique
class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


@unique
class OrderStatus(str, Enum):
    NEW = "new"
    PROCESSING = "processing"
    OPEN = "open"
    FILLED = "filled"
    CANCELED = "canceled"
    REJECTED = "rejected"
    FAILED = "failed"
