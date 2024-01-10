from enum import Enum
from models.MetaEnum import _MetaEnum

class Exchange(Enum,metaclass=_MetaEnum):
    NSE = 'NSE'
    BSE = 'BSE'
    NFO = 'NFO'

     




    