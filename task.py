import pygame
import random


def draw_kross():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Крест')
    pygame.draw.line(screen, pygame.Color(255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, pygame.Color(255, 255, 255), (width, 0), (0, height), 5)


def draw_rectangle(w, h):
    pygame.init()
    size = width, height = w, h
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Прямоугольник')
    screen.fill((0, 0, 0))
    screen.fill((255, 0, 0), pygame.Rect(1, 1, w - 2, h - 2))


if __name__ == '__main__':
    print('Введите название задания  (Крест, Прямоугольник, Шахматная доска, Мишень)')
    which_function = input()

    if which_function == 'Крест':
        draw_kross()
    if which_function == 'Прямоугольник':
        s = input().split()
        wi, he = s[0], s[1]
        draw_rectangle(int(wi), int(he))
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
