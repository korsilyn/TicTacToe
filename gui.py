# Main GUI file

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
	game_param = [['','',''],['','',''],['','',''], 1, mode, ''] # game matrix, move, mode, result of logic check
	while True:
		event, values = game.read()
		if event in (gui.WIN_CLOSED, 'Exit'):
			game.close()
			mainmenu()
		if event in ('m00'):
			print("test")
			game_param = logic.move(0, 0, game_param) # current pos and game_param matrix
			if game_param[5] != '':
				game['m00'].update(game_param[5])
				game_param[5] = ''
		if event in ('m01'):
			game_param = logic.move(0, 1, game_param)
			if game_param[5] != '':
				game['m01'].update(game_param[5])
				game_param[5] = ''
		if event in ('m02'):
			game_param = logic.move(0, 2, game_param)
			if game_param[5] != '':
				game['m02'].update(game_param[5])
				game_param[5] = ''
		if event in ('m10'):
			game_param = logic.move(1, 0, game_param)
			if game_param[5] != '':
				game['m10'].update(game_param[5])
				game_param[5] = ''
		if event in ('m11'):
			game_param = logic.move(1, 1, game_param)
			if game_param[5] != '':
				game['m11'].update(game_param[5])
				game_param[5] = ''
		if event in ('m12'):
			game_param = logic.move(1, 2, game_param)
			if game_param[5] != '':
				game['m12'].update(game_param[5])
				game_param[5] = ''
		if event in ('m20'):
			game_param = logic.move(2, 0, game_param)
			if game_param[5] != '':
				game['m20'].update(game_param[5])
				game_param[5] = ''
		if event in ('m21'):
			game_param = logic.move(2, 1, game_param)
			if game_param[5] != '':
				game['m21'].update(game_param[5])
				game_param[5] = ''
		if event in ('m22'):
			game_param = logic.move(2, 2, game_param)
			if game_param[5] != '':
				game['m22'].update(game_param[5])
				game_param[5] = ''

def settings():
	pass