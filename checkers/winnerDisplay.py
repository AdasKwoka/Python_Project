import pygame
from .constants import WHITE, BIGFONT, WIDTH, HEIGHT


class WinnerDisplay:
    def __init__(self, text, win):
        self.color = WHITE
        self.text = BIGFONT.render(text, True, self.color)
        self.win = win
        self.draw()

    def draw(self):
        self.win.blit(self.text, (400, HEIGHT - 60))
