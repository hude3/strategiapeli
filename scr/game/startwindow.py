from PyQt6 import QtWidgets
from scr.game.game import Game
from PyQt6.QtWidgets import QPushButton, QLabel
from scr.game.game_init import GameInit
from scr.game.game_errors import CorruptedConfigureFileError

class StartWindow(QtWidgets.QWidget):               # aloitusikkuna pelille

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome to STRAT')
        self.init_buttons()
        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.addWidget(self.new_match_button)
        self.layout1.addWidget(self.continue_match_button)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.layout1)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def init_buttons(self):
        self.new_match_button = QPushButton('Start a new match')
        self.new_match_button.clicked.connect(self.new_match_button_clicked)

        self.continue_match_button = QPushButton('Continue a match')
        self.continue_match_button.clicked.connect(self.continue_match_button_clicked)




    def new_match_button_clicked(self):
        name, ok = QtWidgets.QInputDialog.getText(self,'Name', 'Enter your name')

        if ok:
            width, ok = QtWidgets.QInputDialog.getText(self,'Width', 'Enter map width')
            try:
                if ok and int(width) <= 0:
                    ok = False
                    self.incorrect_label = QLabel('Incorrect width')
                    self.layout.addWidget(self.incorrect_label)
                    self.show()
            except ValueError:
                ok = False
                self.incorrect_label = QLabel('Incorrect width')
                self.layout.addWidget(self.incorrect_label)
                self.show()

            if ok:
                length, ok = QtWidgets.QInputDialog.getText(self, 'Length', 'Enter map length')
                try:
                    if ok and int(length) <= 0:
                        ok = False
                        self.incorrect_label = QLabel('Incorrect length')
                        self.layout.addWidget(self.incorrect_label)
                        self.show()
                except ValueError:
                    ok = False
                    self.incorrect_label = QLabel('Incorrect length')
                    self.layout.addWidget(self.incorrect_label)
                    self.show()
                if ok:
                    try:
                        game = Game()
                        game.set_player(name)
                        game.set_random_map(int(width), int(length))
                        game.set_gui(50)
                        self.close()
                    except CorruptedConfigureFileError:
                        self.configlabel = QLabel('Configure file corrupted')
                        self.layout.addWidget(self.configlabel)
                        self.show()





    def continue_match_button_clicked(self):
        filename, ok = QtWidgets.QInputDialog.getText(self,'File name', 'Enter the name of the save file')
        if ok:
            try:
                save_file = open(filename, 'r')
                init = GameInit()
                game = init.load_game(save_file)
                if not game:
                    self.corruptlabel = QLabel('Save file corrupted')
                    self.layout.addWidget(self.corruptlabel)
                    self.show()


                else:
                    save_file.close()
                    game.set_gui(50)
                    self.close()

            except OSError:
                self.corruptlabel = QLabel('Wrong file name')
                self.layout.addWidget(self.corruptlabel)
                self.show()


