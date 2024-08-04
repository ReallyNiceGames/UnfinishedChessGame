from Pieces.Pawn import *
from Pieces.Knight import *
from Pieces.Bishop import *
from Pieces.Rook import *
from Pieces.Queen import *
from Pieces.King import *
import os


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

        self.white_turn = True

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
            self.white_pieces.append(Pawn(0))
            self.board_layout[1][0 + x] = "[P]"
            self.black_pieces.append(Pawn(1))
            self.board_layout[6][0 + x] = "[p]"

        for x in range(self.max_knights):
            self.white_pieces.append(Knight(0))
            if self.board_layout[0][1] != "[N]":
                self.board_layout[0][1] = "[N]"
            else:
                self.board_layout[0][6] = "[N]"

            self.black_pieces.append(Knight(1))
            if self.board_layout[7][1] != "[n]":
                self.board_layout[7][1] = "[n]"
            else:
                self.board_layout[7][6] = "[n]"

        for x in range(self.max_bishops):
            self.white_pieces.append(Bishop(0))
            if self.board_layout[0][2] != "[B]":
                self.board_layout[0][2] = "[B]"
            else:
                self.board_layout[0][5] = "[B]"

            self.black_pieces.append(Bishop(1))
            if self.board_layout[7][2] != "[b]":
                self.board_layout[7][2] = "[b]"
            else:
                self.board_layout[7][5] = "[b]"

        for x in range(self.max_rooks):
            self.white_pieces.append(Rook(0))
            if self.board_layout[0][0] != "[R]":
                self.board_layout[0][0] = "[R]"
            else:
                self.board_layout[0][7] = "[R]"

            self.black_pieces.append(Rook(1))
            if self.board_layout[7][0] != "[r]":
                self.board_layout[7][0] = "[r]"
            else:
                self.board_layout[7][7] = "[r]"

        for x in range(self.max_kings):
            self.white_pieces.append(King(0))
            self.board_layout[0][4] = "[K]"

            self.black_pieces.append(King(1))
            self.board_layout[7][4] = "[k]"

        for x in range(self.max_queens):
            self.white_pieces.append(Queen(0))
            self.board_layout[0][3] = "[Q]"

            self.black_pieces.append(Queen(1))
            self.board_layout[7][3] = "[q]"

        print("There is", len(self.white_pieces), "white pieces in the list.")
        print("There is", len(self.black_pieces), "black pieces in the list.")

        self.update_board()

    def update_board(self):

        print("Updating board layout...")

        # re-displays the board

        if self.white_turn:
            print("Flipping to White PoV")
            for x in range(len(self.board_layout)):
                for y in range(len(self.board_layout[x])):
                    print(self.board_layout[(len(self.board_layout) - 1) - x][(len(self.board_layout) - 1) - y], end="")
                print()
        else:
            print("Flipping to Black PoV")
            for x in range(len(self.board_layout)):
                for y in range(len(self.board_layout[x])):
                    print(self.board_layout[x][y], end="")
                print()

    def change_turn(self):

        print("Deciding who's turn it is...")

        # swapping the turn
        self.white_turn = not self.white_turn

        if self.white_turn:
            print("It's white's turn!")
        else:
            print("It's black's turn!")

        self.update_board()

    def make_move(self, user_input):

        print("Moving based on input...")

        #inputs should be 4 letters/numbers, for example: b1c4

        #take the code, break it down, find the piece on the initial space and activate its move function
        #send the move function the 2 last bits of the code to determine where it goes (if possible)

    def start_game(self):

        # while game is going, loop
        while True:
            user_input = input("Please input a move. Input: ")

            if user_input == "exit":
                break
            elif user_input == "help":
                print("This is where help goes")
            else:
                self.make_move(user_input)

        return 0
