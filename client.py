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
        if i != (100, 100):
            p1.draw(i, win)
    for i in p2.moves:
        if i != (100, 100):
            p2.draw(i, win)
    pygame.display.update()


def get_coord(tup):
    return tup[0] // 201, tup[1] // 201




def main():
    run = True
    n = Network()
    p1 = n.getP()
    pos = (100, 100)

    while run:
        p2 = n.send(p1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if p1.turn and event.type == pygame.MOUSEBUTTONDOWN:
                pos = get_coord(pygame.mouse.get_pos())
                p1.turn = not p1.turn
        if pos not in p1.moves and pos not in p2.moves:
            p1.moves.append(pos)


        redrawWindow(win, p1, p2)


main()
