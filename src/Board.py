from Pieces.Pawn import *
from Pieces.Knight import *
from Pieces.Bishop import *
from Pieces.Rook import *
from Pieces.Queen import *
from Pieces.King import *


class Board:

    def __init__(self):
        print("Board instance created!")
        # add variables

        self.max_pawns = 8
        self.max_knights = 2
        self.max_bishops = 2
        self.max_rooks = 2
        self.max_queens = 1
        self.max_kings = 1

        self.turn = 0

        self.white_pieces = []
        self.black_pieces = []
        self.board_layout = []

        self.default_layout = [["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                              ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]]

        self.reset_board()


    def reset_board(self):
        print("Resetting board...")
        # resets the board to default state and placements

        self.white_pieces.clear()
        self.black_pieces.clear()
        self.board_layout = self.default_layout

        for x in range(self.max_pawns):
            self.white_pieces.append(Pawn())
            self.black_pieces.append(Pawn())

        for x in range(self.max_knights):
            self.white_pieces.append(Knight())
            self.black_pieces.append(Knight())

        for x in range(self.max_bishops):
            self.white_pieces.append(Bishop())
            self.black_pieces.append(Bishop())

        for x in range(self.max_rooks):
            self.white_pieces.append(Rook())
            self.black_pieces.append(Rook())

        for x in range(self.max_kings):
            self.white_pieces.append(King())
            self.black_pieces.append(King())

        for x in range(self.max_queens):
            self.white_pieces.append(Queen())
            self.black_pieces.append(Queen())

        print("There is", len(self.white_pieces), "white pieces in the list.")
        print("There is", len(self.black_pieces), "black pieces in the list.")



        for x in range(len(self.board_layout)):
            for y in range(len(self.board_layout[x])):
                print(self.board_layout[x][y], end="")
            print()

        #self.update_board()

    def update_board(self):

        print("Updating board layout...")

    def take_turn(self):

        print("Deciding who's turn it is...")

        if self.turn == 0:
            print("It's white's turn!")
            self.turn = 1
        else:
            print("It's black's turn!")
            self.turn = 0

    def start_game(self):

        print("Starting game...")

        self.white_pieces[0].move_piece()
        #print(self.white_pieces[0].pos_x)

        # while game is going, loop

        return 0
