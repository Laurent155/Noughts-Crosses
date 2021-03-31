class Game:
    def __init__(self, turn):
        self.turn = turn
        self.p1moves = []
        self.p2moves = []
   
    def draw(self, coord, win, symbol):
        coord = coord[0] * 201 + 100, coord[1] * 201 + 100
        if symbol == "circle":
            pygame.draw.circle(win, (0, 0, 0), coord, 20, 5)
        else:
            pygame.draw.line(win, (0, 0, 0), (coord[0] - 20, coord[1] - 20), (coord[0] + 20, coord[1] + 20), 5)
            pygame.draw.line(win, (0, 0, 0), (coord[0] + 20, coord[1] - 20), (coord[0] - 20, coord[1] + 20), 5)  
