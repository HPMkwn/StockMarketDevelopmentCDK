from enum import Enum
from MetaEnum import _MetaEnum


class TrnsactionType(Enum, metaclass=_MetaEnum):
    BUY = 'BUY'
    SELL = 'SELL'

