
from enum import Enum

class BaseEnum(Enum):
    @classmethod
    def keys(cls):
        return [k.name for k in cls]

    @classmethod
    def values(cls):
        return [k.value for k in cls]

    @classmethod
    def items(cls):
        return [(k.value, k.name) for k in cls]


class ProgressChoiceEnum(BaseEnum): 
    Pending = "Pending"
    InProgress = "In Progress"
    Cancelled = "Cancelled"
    Completed = "Completed"
    Delayed   = "Delayed"
    
   