from enum import Enum


class Status(Enum):
    SUCCESS = 200
    NOT_FOUND = 400
    FAILURE = 500
    _504 = 5.04