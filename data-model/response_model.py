from pydantic import BaseModel
from shared_services.schema.documents import Dispatch
from enum import Enum

class CaseInsensitiveEnum(Enum):
    """Enum overriden to support case insensitive keys"""
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value == value.upper():
                return member