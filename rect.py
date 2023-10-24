from position2d import Position2D

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
    
    def get_corner(self) -> Position2D:
        return Position2D(self.x, self.y)
    
    def get_outer_bounds(self) -> Position2D:
        return Position2D(self.x + self.w, self.y + self.h)