from enum import Enum
from MetaEnum import _MetaEnum

class PriceType(Enum,metaclass=_MetaEnum):
    UPPER_CERCUIT = 'UPPER_CERCUIT'
    LOWER_CERCUIT = 'LOWER_CERCUIT'
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'

     