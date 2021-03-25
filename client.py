import pygame
from player import Player
from network import Network

width = 602
height = 602
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, p1, p2):
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0,0,0), (0,201), (602,201), 1)
    pygame.draw.line(win, (0,0,0), (0,402), (602,402), 1)
    pygame.draw.line(win, (0,0,0), (201,0), (201,602), 1)
    pygame.draw.line(win, (0,0,0), (402,0), (402,602), 1)
    p1.draw(win, symbol, coord)
    p2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 20, 20, (0, 0, 255))
    p2 = Player(50, 50, 20, 20, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)


main()

