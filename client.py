import pygame
from player import Player
from network import Network
from server import currentPlayer

width = 602
height = 602
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = currentPlayer


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, p1, p2):
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0, 0, 0), (0, 201), (602, 201), 1)
    pygame.draw.line(win, (0, 0, 0), (0, 402), (602, 402), 1)
    pygame.draw.line(win, (0, 0, 0), (201, 0), (201, 602), 1)
    pygame.draw.line(win, (0, 0, 0), (402, 0), (402, 602), 1)
    for i in p1.moves:
        p1.draw(win, i)
    for i in p2.moves:
        p2.draw(win, i)
    pygame.display.update()


def get_coord(pos):
    return pos[0] // 201, pos[1] // 201


def main():
    run = True
    circle_turn = True
    cross_turn = False
    n = Network()
    if clientNumber == 1:
        p1 = Player("circle", win)
        p2 = Player("cross", win)
    else:
        p1 = Player("cross", win)
        p2 = Player("circle", win)

    while run:
        # p2Pos = read_pos(n.send(make_pos(p1.moves[-1])))
        # p2.x = p2Pos[0]
        # p2.y = p2Pos[1]
        # p2.update()

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
