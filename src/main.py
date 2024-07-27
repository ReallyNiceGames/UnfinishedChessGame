from Board import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    new_board = Board()

    game_state = 1
    while game_state == 1:

        game_state = new_board.start_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
