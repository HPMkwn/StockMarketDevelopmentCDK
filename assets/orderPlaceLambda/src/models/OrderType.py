from enum import Enum
from MetaEnum import _MetaEnum


class OrderType(Enum, metaclass=_MetaEnum):
    ORDER_TYPE_LIMIT = "ORDER_TYPE_LIMIT"
    ORDER_TYPE_MARKET = "ORDER_TYPE_MARKET"
    ORDER_TYPE_SL = "ORDER_TYPE_SL"
    ORDER_TYPE_SLM = "ORDER_TYPE_SLM"

