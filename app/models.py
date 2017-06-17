game_board = {'x1': 'X', 'x2': 'X', 'x3': 'X', 'x4': 'X', 'x5': 'X', 'x6': 'X', 'x7': 'X', 'x8': 'X', 'x9': 'X'}

def game(position, player):
    '''Takes in key/value pair, then updates the game board'''

    game_board[position] = player


def players_toggle(current_player):
    '''Pass in which player just finished their move as either 'A' or 'B'
    return the next player'''

    if current_player == 'A':
        return 'B'
    else:
        return 'A'
