from src.Pieces.Piece import *


class Pawn(Piece):
    def __init__(self, colour):
        print("This is a pawn!")
        super().__init__(colour)

        # add variables

        if colour == 0:
            self.board_ID = "[P]"
        else:
            self.board_ID = "[p]"


    def promote_piece(self):
        print("Promoting piece...")
        # allow promotion when this piece reaches the opposite end of the board
