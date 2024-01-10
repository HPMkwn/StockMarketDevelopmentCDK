from enum import Enum
from models.MetaEnum import _MetaEnum

class PriceType(Enum,metaclass=_MetaEnum):
    upper_circuit_limit = 'upper_circuit_limit'
    lower_circuit_limit = 'lower_circuit_limit'
    MARKET = 'MARKET'
    LIMIT = 'LIMIT'

     