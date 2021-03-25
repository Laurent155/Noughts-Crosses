import pygame
class Player():
  def __init__(self, symbol, win):
    self.symbol = symbol
    self.win = win
    self.moves = []
    
  def draw(self, coord):
    pygame.draw.circle(self.win, (0,0,0), coord, 1, 1)
    
  
    
 
