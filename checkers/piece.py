import pygame
from .constants import WHITE, BLACK, SQUARE_SIZE, CROWN


class Piece:
    PADDING = 15
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col+SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row+SQUARE_SIZE//2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        pygame.draw.circle(win, self.color, (self.x, self.y),
                           radius + self.BORDER)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() //
                     2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
