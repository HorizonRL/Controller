from dataclasses import dataclass

@dataclass
class Point:
    x : float
    y : float

    def to_tuple(self) -> tuple:
        return (self.x, self.y)

    def to_int_tuple(self) -> tuple:
        return (int(self.x), int(self.y))
    
    def rescale(self, value: float):
        self.x *= value
        self.y *= value
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
