__author__: str = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"
from enum import Enum


class EventType(Enum):
    NOOP = "noop"
    FAKE = "fake"
    PERSIST = "persist"

    def lower(self) -> str:
        return self.value.lower()
