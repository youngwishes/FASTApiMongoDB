from enum import Enum


class FormTypes(str, Enum):
    TEXT = "TEXT"
    DATE = "DATE"
    EMAIL = "EMAIL"
    PHONE = "PHONE"
