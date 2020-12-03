import pygame
import random


def draw_chess_bar(s, n):
    pygame.init()
    size = width, height = s, s
    if n % 2 == 0:
        color = 'white'
        flag = 0
    else:
        color = 'black'
        flag = 1
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Шахматная клетка')
    w = h = s // n
    sz = s // n
    for column in range(n):
        for row in range(n):
            screen.fill(color, pygame.Rect(column * sz, row * sz, sz, sz))
            if color == 'white':
                color = 'black'
            else:
                color = 'white'
        if flag == 0:
            if color == 'white':
                color = 'black'
            else:
                color = 'white'


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
    print('Введите номер задания  (Крест - 1, Прямоугольник - 2, Шахматная доска - 3, Мишень - 4)')
    which_function = input()

    if which_function == '1':
        draw_kross()

    if which_function == '2':
        print('Введите размеры окна (ширина высота)')
        s = input().split()
        wi, he = s[0], s[1]
        draw_rectangle(int(wi), int(he))
    if which_function == '3':
        print('Введите размеры сторону квадратного окна и количесвто клеток в строке')
        s = input().split()
        s, n = int(s[0]), int(s[1])
        draw_chess_bar(s, n)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
