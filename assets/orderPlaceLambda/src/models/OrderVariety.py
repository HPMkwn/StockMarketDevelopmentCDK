from enum import Enum
from MetaEnum import _MetaEnum


class OrderVariety(Enum, metaclass=_MetaEnum):
    VARIETY_AMO = 'VARIETY_AMO'
    VARIETY_REGULAR = 'VARIETY_REGULAR'


    