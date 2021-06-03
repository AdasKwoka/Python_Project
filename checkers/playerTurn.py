import pygame
from .constants import WHITE, BIGFONT, WIDTH, HEIGHT


class PlayerTurn:
    def __init__(self, text, win):
        self.color = WHITE
        self.text = BIGFONT.render(text, True, self.color)
        self.win = win
        self.draw()

    def draw(self):
        self.win.blit(self.text, (40, HEIGHT - 60))
