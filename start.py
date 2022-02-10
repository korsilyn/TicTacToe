import PySimpleGUI as gui
import gui as game
import settings

layout = [[gui.T('TicTacToe by KrakeN000')],
[gui.T('v4.0.0 prealpha 1')]]
window = gui.Window('TicTacToe', layout, location=(0,0), size=(1000,1000))
window.read(timeout='1000')
window.close()
game.mainmenu()
