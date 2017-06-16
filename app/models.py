game_board = {'x1': '', 'x2': '', 'x3': '', 'x4': '', 'x5': '', 'x6': '', 'x7': '', 'x8': '', 'x9': ''}

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
