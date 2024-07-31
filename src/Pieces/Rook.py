from src.Pieces.Piece import *


class Rook(Piece):

    def __init__(self, colour):

        print("This is a rook!")
        super().__init__(colour)

        # add variables here

        if colour == 0:
            self.board_ID = "[R]"
        else:
            self.board_ID = "[r]"
