# Logic lib
import numpy as np

def move(a, b, game_param):
	# collecting args from game_param
	board = []
	for i in range(3):
		board.append(game_param[i])
	move = game_param[3]
	mode = game_param[4]
	result = game_param[5]

	if board[a][b] == '':
		if move == 1:
			board[a][b] = 1
			result = 'X'
			if mode == 'pvp':
				move = 2
		elif mode == 'pvp':
			board[a][b] = 2
			move = 1
			result = 'O'

	for i in range(3):
		game_param[i] = board[i]
	game_param[3] = move
	game_param[5] = result

	return game_param
