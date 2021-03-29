import pygame
from player import Player
from network import Network
import pickle

width = 602
height = 602
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, p1, p2):
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0, 0, 0), (0, 201), (602, 201), 1)
    pygame.draw.line(win, (0, 0, 0), (0, 402), (602, 402), 1)
    pygame.draw.line(win, (0, 0, 0), (201, 0), (201, 602), 1)
    pygame.draw.line(win, (0, 0, 0), (402, 0), (402, 602), 1)
    for i in p1.moves:
        p1.draw(i, win)
    for i in p2.moves:
        p2.draw(i, win)
    pygame.display.update()


def get_coord(tup):
    return tup*201 + 100


def main():
    run = True
    circle_turn = True
    cross_turn = False
    n = Network()
    p1 = n.getP()
    pos = (1, 1)
    while run:
        p2 = n.send(p1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = get_coord(pygame.mouse.get_pos())
        if pos not in p1.moves and pos not in p2.moves:
            p1.moves.append(pos)
            circle_turn = not circle_turn
            cross_turn = not cross_turn

        redrawWindow(win, p1, p2)


main()
