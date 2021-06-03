import pygame

WIDTH, HEIGHT = 800, 900
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (65, 105, 225)
GRAY = (200, 200, 200)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))

pygame.font.init()
SMALLFONT = pygame.font.SysFont("assets/Roboto/Roboto-Black.ttf", 25)

WHITE_TURN = "Tura gracza bialego"
BLACK_TURN = "Tura gracza czarnego"
BIGFONT = pygame.font.SysFont("assets/Roboto/Roboto-Black.ttf", 35)
