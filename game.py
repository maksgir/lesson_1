import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (100, 255, 100), (10, 10), (310, 310), width=1)
    pygame.draw.rect(screen, (255,100,100), (10,10,300,300), width=3)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
