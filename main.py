import pygame
from alien import Alien
from bouncyAlien import BouncyAlien
from cursorAlien import CursorAlien
from position2d import Position2D
from rect import Rectangle

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
screenRect = Rectangle(0, 0, *size)
pygame.display.set_caption("pain")

clock = pygame.time.Clock()
fps = 60

alienImage = pygame.image.load("joe.jpg")


aliens = []
aliens.append(BouncyAlien(screen, "Bob", alienImage, x=0, y=0, velocity=1))
aliens.append(CursorAlien(screen, "Joe", alienImage, pos2d=Position2D(0, 0)))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)


    screen.fill((255, 255, 255))

    alien: Alien
    for alien in aliens:
        alien.draw()


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()