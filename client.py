import pygame
from network import Network
from game import Game, Turn

width = 602
height = 602
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def redrawWindow(win, game, symbol):
    win.fill((255, 255, 255))
    if game.winner == 'neither':

        pygame.draw.line(win, (0, 0, 0), (0, 201), (602, 201), 1)
        pygame.draw.line(win, (0, 0, 0), (0, 402), (602, 402), 1)
        pygame.draw.line(win, (0, 0, 0), (201, 0), (201, 602), 1)
        pygame.draw.line(win, (0, 0, 0), (402, 0), (402, 602), 1)
        for i in game.p1moves:
            if i != (100, 100):
                game.draw(i, win, 'circle')
        for i in game.p2moves:
            if i != (100, 100):
                game.draw(i, win, 'cross')
    elif game.winner == 'circle':
        if symbol == 'circle':
            textsurface = myfont.render('You win!', False, (0, 0, 0))
        else:
            textsurface = myfont.render('You lose!', False, (0, 0, 0))
        win.blit(textsurface, (260, 270))
    elif game.winner == 'cross':
        if symbol == 'cross':
            textsurface = myfont.render('You win!', False, (0, 0, 0))
        else:
            textsurface = myfont.render('You lose!', False, (0, 0, 0))
        win.blit(textsurface, (260, 270))
    if game.tie == 'yes':
        textsurface = myfont.render('Draw!', False, (0, 0, 0))
        win.blit(textsurface, (270, 270))

    pygame.display.update()


def get_coord(tup):
    return tup[0] // 201, tup[1] // 201


def main():
    run = True
    n = Network()
    symb = n.getP()
    print(symb)
    pos = (100, 100)
    game = Game('circle')
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = get_coord(pygame.mouse.get_pos())
                game = n.send(Turn(symb, pos))
                pos = (100, 100)
        game = n.send(Turn(symb, pos))
        redrawWindow(win, game, symb)


main()
