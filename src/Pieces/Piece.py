class Piece:

    def __init__(self, colour, pos_x, pos_y):
        #print("The piece superclass has been called!")
        # add variables

        if colour == 0:
            self.colour = "White"
        else:
            self.colour = "Black"
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def set_pos(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_piece(self, move):
        print("Moving piece...")

    def take_piece(self):
        print("Taking piece...")
        # finds the piece on the selected tile and removes it from play

