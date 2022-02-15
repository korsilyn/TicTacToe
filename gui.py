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
            [gui.Button(key='board00'), gui.Button(key='board01'), gui.Button(key='board02')],
            [gui.Button(key='board10'), gui.Button(key='board11'), gui.Button(key='board12')],
            [gui.Button(key='board20'), gui.Button(key='board21'), gui.Button(key='board22')],
            [gui.Exit()]]
	game = gui.Window('TicTacToe', layout, location=(0,0), size=(1000,1000))
	# Start
	game_param = [['','',''],['','',''],['','',''], 1, mode, '', 0] # game matrix, move, mode, result of logic check, winner
	while True:
		event, values = game.read()
		if event in (gui.WIN_CLOSED, 'Exit'):
			game.close()
			mainmenu()
		if event in ('board00'):
			game_param = logic.move(0, 0, game_param) # current pos and game_param matrix
			if game_param[5] != '':
				game['board00'].update(game_param[5])
				game_param[5] = ''
		if event in ('board01'):
			game_param = logic.move(0, 1, game_param)
			if game_param[5] != '':
				game['board01'].update(game_param[5])
				game_param[5] = ''
		if event in ('board02'):
			game_param = logic.move(0, 2, game_param)
			if game_param[5] != '':
				game['board02'].update(game_param[5])
				game_param[5] = ''
		if event in ('board10'):
			game_param = logic.move(1, 0, game_param)
			if game_param[5] != '':
				game['board10'].update(game_param[5])
				game_param[5] = ''
		if event in ('board11'):
			game_param = logic.move(1, 1, game_param)
			if game_param[5] != '':
				game['board11'].update(game_param[5])
				game_param[5] = ''
		if event in ('board12'):
			game_param = logic.move(1, 2, game_param)
			if game_param[5] != '':
				game['board12'].update(game_param[5])
				game_param[5] = ''
		if event in ('board20'):
			game_param = logic.move(2, 0, game_param)
			if game_param[5] != '':
				game['board20'].update(game_param[5])
				game_param[5] = ''
		if event in ('board21'):
			game_param = logic.move(2, 1, game_param)
			if game_param[5] != '':
				game['board21'].update(game_param[5])
				game_param[5] = ''
		if event in ('board22'):
			game_param = logic.move(2, 2, game_param)
			if game_param[5] != '':
				game['board22'].update(game_param[5])
				game_param[5] = ''
		if game_param[6] > 0:
			game['move'].update('We have a winner!')

def settings():
	pass
