from src.Pieces.Piece import *


class King(Piece):

    def __init__(self, colour, pos_x, pos_y):

        print("This is a king!")
        super().__init__(colour, pos_x, pos_y)

        # add variables here

        if colour == 0:
            self.board_ID = "[K]"
        else:
            self.board_ID = "[k]"

        self.in_check = False

    def set_check(self, in_check):
        self.in_check = in_check

    def get_check(self):
        return self.in_check
