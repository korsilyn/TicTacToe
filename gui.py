import tkinter #maybe useless
import PySimpleGUI as gui
import settings, logic
            
def mainmenu():
	layout = [[gui.Button('PvP', key=('pvp'))],
	[gui.Button('PvE', key=('pve'))],
	[gui.Button('Settings', key=('settings'))],
	[gui.Exit()]]
	menu = gui.Window('TicTacToe', layout, location=(0,0), size=(1000,1000))
	while True:
		event, values = menu.read()
		if event in (gui.WIN_CLOSED, 'Exit'):
			menu.close()
		if event in ('pvp'):
			menu.close()
			game('pvp')
		if event in ('pve'):
			menu.close()
			game('pve')
			
def game(mode):
	layout = [[gui.T('Move by: ', key='move')],
            [gui.Button(key='m00'), gui.Button(key='m01'), gui.Button(key='m02')],
            [gui.Button(key='m10'), gui.Button(key='m11'), gui.Button(key='m12')],
            [gui.Button(key='m20'), gui.Button(key='m21'), gui.Button(key='m22')],
            [gui.Exit()]]
	game = gui.Window('TicTacToe', layout, location=(0,0), size=(1000,1000))
	# Start
	move = 1
	matrix = [[0,0,0],[0,0,0],[0,0,0]]
	while True:
		event, values = game.read()
		if event in (gui.WIN_CLOSED, 'Exit'):
			game.close()
			mainmenu()
		if event in ('m00'):
			if matrix[0][0] == 0
				if move == 1:
					game['m00'].update('X')
					matrix[0][0] = 1
					if mode == 'pvp':
						move = 2
#				else:
#					a, b = ai.difficulty.move(matrix)
#					matrix[a][b] = 2
#					tmp = m+a+b (strings) and than change elem
				elif mode == 'pvp':
					game['m00'].update('O')
					matrix[0][0] = 2
					move = 1
		if event in ('m01'):
			logic.check(0, 1, mode)
			if move == 1:
				game['m01'].update('X')
			elif move == 2:
				game['m01'].update('O')
		if event in ('m02'):
			logic.check(0, 2, mode)
			if move == 1:
				game['m02'].update('X')
			elif move == 2:
				game['m02'].update('O')
		if event in ('m10'):
			logic.check(1, 0, mode)
			if move == 1:
				game['m10'].update('X')
			elif move == 2:
				game['m10'].update('O')
		if event in ('m11'):
			logic.check(1, 1, mode)
			if move == 1:
				game['m11'].update('X')
			elif move == 2:
				game['m11'].update('O')
		if event in ('m12'):
			logic.check(1, 2, mode)
			if move == 1:
				game['m12'].update('X')
			elif move == 2:
				game['m12'].update('O')
		if event in ('m20'):
			logic.check(2, 0, mode)
			if move == 1:
				game['m20'].update('X')
			elif move == 2:
				game['m20'].update('O')
		if event in ('m21'):
			logic.check(2, 1, mode)
			if move == 1:
				game['m21'].update('X')
			elif move == 2:
				game['m21'].update('O')
		if event in ('m22'):
			logic.check(2, 2, mode)
			if move == 1:
				game['m22'].update('X')
			elif move == 2:
				game['m22'].update('O')

def settings():
	pass