from src.Pieces.Piece import *


class Bishop(Piece):

    def __init__(self, colour, pos_x, pos_y):

        print("This is a bishop!")
        super().__init__(colour, pos_x, pos_y)

        # variables here

        if colour == 0:
            self.board_ID = "[B]"
        else:
            self.board_ID = "[b]"

