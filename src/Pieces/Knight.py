from src.Pieces.Piece import *


class Knight(Piece):

    def __init__(self, colour):

        print("This is a knight!")
        super().__init__(colour)

        # add variables here

        if colour == 0:
            self.board_ID = "[H]"
        else:
            self.board_ID = "[h]"

