new_game_board = {'x1': 'X', 'x2': 'X', 'x3': 'X', 'x4': 'X', 'x5': 'X', 'x6': 'X', 'x7': 'X', 'x8': 'X', 'x9': 'X'}
game_board = {'x1': 'X', 'x2': 'X', 'x3': 'X', 'x4': 'X', 'x5': 'X', 'x6': 'X', 'x7': 'X', 'x8': 'X', 'x9': 'X'}
moves_made = 1


def player_select():
    if moves_made % 2 == 0:
        return 'A'
    return 'B'


def winner():
    if game_board['x1'] == 'A' and game_board['x2'] == 'A' and game_board['x3'] == 'A':
        return 'winner'

    if game_board['x4'] == 'A' and game_board['x5'] == 'A' and game_board['x6'] == 'A':
        return 'winner'

    if game_board['x7'] == 'A' and game_board['x8'] == 'A' and game_board['x9'] == 'A':
        return 'winner'

    if game_board['x1'] == 'A' and game_board['x4'] == 'A' and game_board['x7'] == 'A':
        return 'winner'

    if game_board['x2'] == 'A' and game_board['x5'] == 'A' and game_board['x8'] == 'A':
        return 'winner'

    if game_board['x3'] == 'A' and game_board['x6'] == 'A' and game_board['x9'] == 'A':
        return 'winner'

    if game_board['x1'] == 'A' and game_board['x5'] == 'A' and game_board['x9'] == 'A':
        return 'winner'

    if game_board['x7'] == 'A' and game_board['x5'] == 'A' and game_board['x3'] == 'A':
        return 'winner'

    if game_board['x1'] == 'B' and game_board['x2'] == 'B' and game_board['x3'] == 'B':
        return 'winner'

    if game_board['x4'] == 'B' and game_board['x5'] == 'B' and game_board['x6'] == 'B':
        return 'winner'

    if game_board['x7'] == 'B' and game_board['x8'] == 'B' and game_board['x9'] == 'B':
        return 'winner'

    if game_board['x1'] == 'B' and game_board['x4'] == 'B' and game_board['x7'] == 'B':
        return 'winner'

    if game_board['x2'] == 'B' and game_board['x5'] == 'B' and game_board['x8'] == 'B':
        return 'winner'

    if game_board['x3'] == 'B' and game_board['x6'] == 'B' and game_board['x9'] == 'B':
        return 'winner'

    if game_board['x1'] == 'B' and game_board['x5'] == 'B' and game_board['x9'] == 'B':
        return 'winner'

    if game_board['x7'] == 'B' and game_board['x5'] == 'B' and game_board['x3'] == 'B':
        return 'winner'