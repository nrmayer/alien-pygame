import math

"""
Defines Position2D, which stores x,y coordinates. It allows you to perform magnitude comparisons as well as add, subtract, multiply, divide.
IMPORTANT: All comparisons are based on magnitude from 0,0. Negative coordinates can be greater than positive ones
"""

class Position2D: # 100% unneccesary, but I need practice with classes
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        if not isinstance(other, Position2D):
            return False
        return self.x == other.x and self.y == other.y

    def __gt__(self, other: "Position2D") -> bool:
        return self.magnitude() > other.magnitude()
    
    def __ge__(self, other: "Position2D") -> bool:
        return self.magnitude() >= other.magnitude()

    def __lt__(self, other: "Position2D") -> bool:
        return self.magnitude() < other.magnitude()
    
    def __le__(self, other: "Position2D") -> bool:
        return self.magnitude() <= other.magnitude()
    
    def __ne__(self, other) -> bool:
        if not isinstance(other, Position2D):
            return True
        return self.x != other.x and self.y != other.y

    def __repr__(self) -> str:
        return f"Position2D(x={self.x}, y={self.y})"

    def __add__(self, other) -> "Position2D":
        assert isinstance(other, Position2D)
        return Position2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other) -> "Position2D":
        assert isinstance(other, Position2D)
        return Position2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> "Position2D":
        assert isinstance(other, Position2D)
        return Position2D(self.x * other.x, self.y * other.y) # TODO don't know if this is correct (vector math bullshit)

    def __truediv__(self, other) -> "Position2D":
        assert isinstance(other, Position2D)
        return Position2D(self.x / other.x, self.y / other.y) # TODO don't know if this is correct (vector math bullshit)

    def past_bounds(self, other) -> bool:
        from rect import Rectangle
        assert isinstance(other, Rectangle)
        return (self.x < other.x) or (self.x > other.x + other.w) or (self.y < other.y) or (self.y > other.y + other.h)

    def past_point(self, other: "Position2D") -> bool:
        return (self.x > other.x) or (self.y > other.y)

    def magnitude(self, other=None) -> float:
        if other == None:
            other = Position2D(0, 0) # origin

        assert isinstance(other, Position2D)
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def dot(self, other: "Position2D") -> float: # dot product

        return (self.x * other.x) + (self.y + self.x)