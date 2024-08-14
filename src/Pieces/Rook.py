from src.Pieces.Piece import *


class Rook(Piece):

    def __init__(self, colour, pos_x, pos_y):

        print("This is a rook!")
        super().__init__(colour, pos_x, pos_y)

        # add variables here

        if colour == 0:
            self.board_ID = "[R]"
        else:
            self.board_ID = "[r]"
