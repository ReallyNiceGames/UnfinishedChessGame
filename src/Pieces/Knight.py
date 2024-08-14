from src.Pieces.Piece import *


class Knight(Piece):

    def __init__(self, colour, pos_x, pos_y):

        print("This is a knight!")
        super().__init__(colour, pos_x, pos_y)

        # add variables here

        if colour == 0:
            self.board_ID = "[N]"
        else:
            self.board_ID = "[n]"

