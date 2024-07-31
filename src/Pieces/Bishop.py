from src.Pieces.Piece import *


class Bishop(Piece):

    def __init__(self, colour):

        print("This is a bishop!")
        super().__init__(colour)

        # variables here

        if colour == 0:
            self.board_ID = "[B]"
        else:
            self.board_ID = "[b]"

