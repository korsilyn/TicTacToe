def check(a, b, mode, mv, matrix):
	if matrix[a][b] == 0:
		return move(a, b, mode, mv)

def move(a, b, mode):
	mv = 1
	if mv == 1:
		matrix[a][b] = 1
		mv = 2
		return 1
	elif mode == 'pvp':
		matrix[a][b] = 2
		mv = 1
		return 2
#	else:
#		ai.diff.move()