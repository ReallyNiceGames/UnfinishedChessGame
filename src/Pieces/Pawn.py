from src.Pieces.Piece import *


class Pawn(Piece):
    def __init__(self, colour, pos_x, pos_y):
        print("This is a pawn!")
        super().__init__(colour, pos_x, pos_y)

        # add variables

        if colour == 0:
            self.board_ID = "[P]"
        else:
            self.board_ID = "[p]"


    def promote_piece(self):
        print("Promoting piece...")
        # allow promotion when this piece reaches the opposite end of the board
