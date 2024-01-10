from enum import Enum
from models.MetaEnum import _MetaEnum


class TrnsactionType(Enum, metaclass=_MetaEnum):
    BUY = 'BUY'
    SELL = 'SELL'

