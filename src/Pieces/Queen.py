from src.Pieces.Piece import *


class Queen(Piece):

    def __init__(self, colour):

        print("This is a queen!")
        super().__init__(colour)

        # add variables here

        if colour == 0:
            self.board_ID = "[Q]"
        else:
            self.board_ID = "[q]"
