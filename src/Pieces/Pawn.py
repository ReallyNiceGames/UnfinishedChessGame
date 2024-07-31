from src.Pieces.Piece import *


class Pawn(Piece):
    def __init__(self):
        print("This is a pawn!")

        # add variables

        self.board_ID = "[P]"

    def promote_piece(self):
        print("Promoting piece...")
        # allow promotion when this piece reaches the opposite end of the board
