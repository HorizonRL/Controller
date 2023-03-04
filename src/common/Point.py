from dataclasses import dataclass

@dataclass
class Point:
    x : float
    y : float

    def to_tuple(self) -> tuple:
        return (self.x, self.y)
