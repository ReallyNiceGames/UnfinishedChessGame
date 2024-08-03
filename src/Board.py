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

        y = 0
        for x in range(self.max_pawns):
            self.white_pieces.append(Pawn(0))
            self.board_layout[1][0 + y] = "[P]"
            self.black_pieces.append(Pawn(1))
            self.board_layout[6][0 + y] = "[p]"
            y += 1

        for x in range(self.max_knights):
            self.white_pieces.append(Knight(0))
            if self.board_layout[0][1] != "[H]":
                self.board_layout[0][1] = "[H]"
            else:
                self.board_layout[0][6] = "[H]"

            self.black_pieces.append(Knight(1))
            if self.board_layout[7][1] != "[h]":
                self.board_layout[7][1] = "[h]"
            else:
                self.board_layout[7][6] = "[h]"

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

        if self.turn == 0:
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

    def take_turn(self):

        print("Deciding who's turn it is...")

        if self.turn == 0:
            print("It's white's turn!")
            self.turn = 1
        else:
            print("It's black's turn!")
            self.turn = 0

        self.update_board()

    def flip_board(self):

        print("Rotating the board 180 degrees...")

        # Flips the board perspective by 180 degrees

    def start_game(self):

        #print("Starting game...")

        #self.white_pieces[0].move_piece()
        #print(self.white_pieces[0].get_pos_x())

        #print(self.white_pieces[0].colour)
        #print(self.black_pieces[0].colour)

        while True:
            user_input = input("Who's turn is it? Input: ")
            #os.system('clear')
            self.take_turn()
            if user_input == "exit":
                break

        # while game is going, loop

        return 0
