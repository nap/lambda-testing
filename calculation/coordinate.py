__author__: str = "Jean-Bernard Ratte - jean.bernard.ratte@unary.ca"

import math


class Coordinate:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = int(x)
        self.y: int = int(y)

    def calculate(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self) -> str:
        return f"Coordinate({self.x}, {self.y})"
