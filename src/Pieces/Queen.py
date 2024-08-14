from src.Pieces.Piece import *


class Queen(Piece):

    def __init__(self, colour, pos_x, pos_y):

        print("This is a queen!")
        super().__init__(colour, pos_x, pos_y)

        # add variables here

        if colour == 0:
            self.board_ID = "[Q]"
        else:
            self.board_ID = "[q]"
