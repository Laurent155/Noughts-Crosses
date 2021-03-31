import pygame
from player import Player
from network import Network
import pickle
from game import Game

width = 602
height = 602
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win, game):
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0, 0, 0), (0, 201), (602, 201), 1)
    pygame.draw.line(win, (0, 0, 0), (0, 402), (602, 402), 1)
    pygame.draw.line(win, (0, 0, 0), (201, 0), (201, 602), 1)
    pygame.draw.line(win, (0, 0, 0), (402, 0), (402, 602), 1)
    for i in game.p1moves:
        if i != (100, 100):
            game.draw(i, win, symbol)
    for i in game.p2moves:
        if i != (100, 100):
            game.draw(i, win, symbol)
    pygame.display.update()


def get_coord(tup):
    return tup[0] // 201, tup[1] // 201
def swap_turn(game):
    if game.turn == "circle":
        game.turn = "cross"
    else:
        game.turn = "circle"

def main():
    run = True
    n = Network()
    p1, game = n.getP()
    pos = (100, 100)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if game.turn == p1.symbol:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = get_coord(pygame.mouse.get_pos())
                    swap_turn(game)
        if pos not in game.p1moves and pos not in game.p2moves:
            game.p1moves.append(pos)
        game = n.send(game)
        redrawWindow(win, game)


main()
