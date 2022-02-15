# Logic lib

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
			board[a][b] = 'X'
			result = 'X'
			if mode == 'pvp':
				move = 2
		elif mode == 'pvp':
			board[a][b] = 'O'
			move = 1
			result = 'O'

	for i in range(3):
		game_param[i] = board[i]
	game_param[3] = move
	game_param[5] = result
	game_param[6] = isWinner(board, 'X', 'O')

	return game_param

# generating every possible win combo
# later i can create games >3x3
def win_indexes(n):
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]

# getting board and decorator (decorator customize in settings)
def isWinner(board, firstPlayer, secondPlayer):
    n = len(board)
    for indexes in win_indexes(n):
        if all(board[r][c] == firstPlayer for r, c in indexes):
            return True
    for indexes in win_indexes(n):
        if all(board[r][c] == secondPlayer for r, c in indexes):
            return True
    return False
