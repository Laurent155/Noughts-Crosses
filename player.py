import pygame


class Player():
    def __init__(self, symbol, win):
        self.symbol = symbol
        self.win = win
        self.moves = []

    def draw(self, coord):
        coord = coord * 201 + 100
        if self.symbol == "circle":
            pygame.draw.circle(self.win, (0, 0, 0), coord, 1, 1)
        else:
            pygame.draw.line(self.win, (0, 0, 0), (coord[0] - 20, coord[1] - 20), (coord[0] + 20, coord[1] + 20), 1)
            pygame.draw.line(self.win, (0, 0, 0), (coord[0] + 20, coord[1] - 20), (coord[0] - 20, coord[1] + 20), 1)
