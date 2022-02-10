import tkinter #maybe useless
import PySimpleGUI as gui
import settings
            
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
            [gui.Button(key='m11'), gui.Button(key='m12'), gui.Button(key='m13')],
            [gui.Button(key='m21'), gui.Button(key='m22'), gui.Button(key='m23')],
            [gui.Button(key='m31'), gui.Button(key='m32'), gui.Button(key='m33')],
            [gui.Exit()]]
	game = gui.Window('TicTacToe', layout, location=(0,0), size=(1000,1000))
	while True:
		event, values = game.read()
		if event in (gui.WIN_CLOSED, 'Exit'):
			game.close()
			mainmenu()

def settings():
	pass