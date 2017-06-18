game_board = {'x1': 'X', 'x2': 'X', 'x3': 'X', 'x4': 'X', 'x5': 'X', 'x6': 'X', 'x7': 'X', 'x8': 'X', 'x9': 'X'}
moves_made = 0


def game(position, player):
    '''Takes in key/value pair, then updates the game board'''

    game_board[position] = player

def player_select():
    if moves_made % 2 == 0:
        return 'A'
    return 'B'
