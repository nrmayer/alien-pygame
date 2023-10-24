import pygame
from position2d import Position2D

"""
Defines alien base class. Has position represented by Position2D class, a name, and an image.
draw() draws at current x,y position. draw_at() updates x,y positions and then calls draw()
"""

class Alien:
    def __init__(self, screen: pygame.Surface, name: str, image: pygame.Surface, 
                 x: int = 0, y: int = 0, pos2d: Position2D = None):
        
        self.screen = screen
        if pos2d == None:
            self.position = Position2D(x, y)
        else:
            self.position = pos2d
        self.name = name
        self.image = image
        self.size = Position2D(self.image.get_width(), self.image.get_height())
    
    def __repr__(self):
        return f"Alien {self.name}, {self.position}"

    # draws at current x,y Position2D coordinates
    def draw(self):
        self.screen.blit(self.image, (self.position.x, self.position.y))

        font = pygame.font.SysFont('arial', 25)
        text = font.render(f'This is {self.name}', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (self.position.x + textRect.width/2, self.position.y + textRect.height/2)
        self.screen.blit(text, textRect)

    # Draws at specified coordinates
    def draw_pos(self, x: int = 0, y: int = 0, pos2d: Position2D = None):
        if pos2d != None:
            x = pos2d.x
            y = pos2d.y
        self.position.x = x
        self.position.y = y
        self.draw()