from Board import *


if __name__ == '__main__':

    new_board = Board()

    game_state = 1
    while game_state == 1:

        game_state = new_board.start_game()
