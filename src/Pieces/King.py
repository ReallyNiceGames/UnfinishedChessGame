from src.Pieces.Piece import *


class King(Piece):

    def __init__(self, colour):

        print("This is a king!")
        super().__init__(colour)

        # add variables here

        if colour == 0:
            self.board_ID = "[K]"
        else:
            self.board_ID = "[k]"
