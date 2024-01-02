import sys
from PyQt6.QtWidgets import QApplication
from scr.game.game import Game

from scr.game.startwindow import StartWindow


# tähän tiedostoon teen jotakin, ainakin testailen koodia ilman, että teen sille omaa testiä



def init_game(name, width, length):

    game = Game()
    game.set_player(name)
    game.set_random_map(width, length)
    start_game(game)

def start_game(game):
    global app
    app = QApplication(sys.argv)
    game.set_gui(50)

    sys.exit(app.exec())

def main():


    global app
    app = QApplication(sys.argv)
    start_window = StartWindow()

    sys.exit(app.exec())


if __name__ =='__main__':
    main()