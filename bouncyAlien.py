from alien import Alien
import pygame
from position2d import Position2D

"""
Alien that bounces around. Calling draw() will run a bounce step. draw() functionality is replaced with draw_here()
"""

class BouncyAlien(Alien):
    def __init__(self, screen: pygame.Surface, name: str, image: pygame.Surface, 
                 x: int = 0, y: int = 0, pos2d: Position2D = None, velocity=1, xBounds=700, yBounds=500):
        super().__init__(screen, name, image, x=x, y=y, pos2d=pos2d)

        self.velocity = Position2D(velocity, velocity) # using like a vector2
        self.bounds = Position2D(xBounds, yBounds)

    def draw(self):
        if self.position.x > self.bounds.x - self.size.x or self.position.x < 0:
            self.velocity.x = -(self.velocity.x)
        if self.position.y > self.bounds.y - self.size.y or self.position.y < 0:
            self.velocity.y = -(self.velocity.y)
        self.position += Position2D(self.velocity.x, self.velocity.y)
        super().draw()

    def draw_here(self):
        super().draw()
