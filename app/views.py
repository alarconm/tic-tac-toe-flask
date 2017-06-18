from flask import render_template, request
from app import app
from app import models



@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title="Tic-Tac-Toe",
                           x1=models.game_board['x1'],
                           x2=models.game_board['x2'],
                           x3=models.game_board['x3'],
                           x4=models.game_board['x4'],
                           x5=models.game_board['x5'],
                           x6=models.game_board['x6'],
                           x7=models.game_board['x7'],
                           x8=models.game_board['x8'],
                           x9=models.game_board['x9'])


@app.route('/game/move')
def game():

    player = models.player_select()

    models.game_board[request.args.get('move')] = player
    models.moves_made += 1
    player = models.player_select()



    return render_template('game.html', title='Tic-Tac-Toe',
                           x1=models.game_board['x1'],
                           x2=models.game_board['x2'],
                           x3=models.game_board['x3'],
                           x4=models.game_board['x4'],
                           x5=models.game_board['x5'],
                           x6=models.game_board['x6'],
                           x7=models.game_board['x7'],
                           x8=models.game_board['x8'],
                           x9=models.game_board['x9'], current_player=player)

    