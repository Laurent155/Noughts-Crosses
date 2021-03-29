import pygame


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.moves = []

    def draw(self, coord, win):
        coord = coord * 201 + 100
        if self.symbol == "circle":
            pygame.draw.circle(win, (0, 0, 0), coord, 1, 1)
        else:
            pygame.draw.line(win, (0, 0, 0), (coord[0] - 20, coord[1] - 20), (coord[0] + 20, coord[1] + 20), 1)
            pygame.draw.line(win, (0, 0, 0), (coord[0] + 20, coord[1] - 20), (coord[0] - 20, coord[1] + 20), 1)
