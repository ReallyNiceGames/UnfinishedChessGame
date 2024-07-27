from Pieces import Knight, Pawn, Rook, Queen, King, Bishop


class Board:

    def __init__(self):
        print("Hello world!")
        # add variables

        self.maxPawns = 8
        self.maxKnights = 2
        self.maxBishops = 2
        self.maxRooks = 2
        self.maxQueens = 1
        self.maxKings = 1

        self.white_pieces = []
        self.black_pieces = []

        self.reset_board()

    def reset_board(self):
        print("Resetting board...")
        # resets the board to default state and placements

        self.white_pieces.clear()
        self.black_pieces.clear()

        for x in range(self.maxPawns):
            self.white_pieces.append(Pawn)
            self.black_pieces.append(Pawn)

        for x in range(self.maxKnights):
            self.white_pieces.append(Knight)
            self.black_pieces.append(Knight)

        for x in range(self.maxBishops):
            self.white_pieces.append(Bishop)
            self.black_pieces.append(Bishop)

        for x in range(self.maxRooks):
            self.white_pieces.append(Rook)
            self.black_pieces.append(Rook)

        for x in range(self.maxKings):
            self.white_pieces.append(King)
            self.black_pieces.append(King)

        for x in range(self.maxQueens):
            self.white_pieces.append(Queen)
            self.black_pieces.append(Queen)

        print("There is", len(self.white_pieces), "white pieces in the list.")
        print("There is", len(self.black_pieces), "black pieces in the list.")

    def start_game(self):

        print("Starting game...")

        # while game is going, loop

        return 0
