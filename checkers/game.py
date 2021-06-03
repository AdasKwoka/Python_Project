import pygame
from checkers.board import Board
from checkers.reset import ResetBtn
from checkers.playerTurn import PlayerTurn
from .constants import WHITE, BLACK, GREEN, SQUARE_SIZE, WHITE_TURN, BLACK_TURN


class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.resetBtn = ResetBtn(self.win)
        self.txtTurn = PlayerTurn(self.txt, self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.txt = BLACK_TURN
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if(self.selected):
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        print(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True, (row, col)

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            kings = self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False, (), None, None
        return True, (row, col), skipped, kings

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE +
                               SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = []
        if self.turn == WHITE:
            self.turn = BLACK
            self.txt = BLACK_TURN
        else:
            self.turn = WHITE
            self.txt = WHITE_TURN
