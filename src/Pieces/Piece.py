class Piece:

    def __init__(self, colour):
        #print("The piece superclass has been called!")
        # add variables

        if colour == 0:
            self.colour = "White"
        else:
            self.colour = "Black"
        self.pos_x = 0
        self.pos_y = 0

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def move_piece(self):
        print("Moving piece...")

    def take_piece(self):
        print("Taking piece...")
        # finds the piece on the selected tile and removes it from play

