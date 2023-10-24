from alien import Alien
import pygame
from position2d import Position2D

"""
Alien that sticks to your cursor. Updates when draw() is called. draw() functionality is replaced with draw_here()
"""

class CursorAlien(Alien):
    def draw(self):
        try:
            self.position = Position2D(*pygame.mouse.get_pos())
            super().draw()
        except TypeError:
            super().draw()

    def draw_here(self):
        super().draw()