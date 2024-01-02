from scr.game.player import Player
from PyQt6.QtGui import QColor

class Aiplayer(Player):                         # en oikeastaan enää tiedä miksi tein tämän uutena oliona, mutta antaa nyt olla


    def __init__(self, name, money):
        super().__init__(name, money)
        self.name = 'AI'
        self.color = QColor(0, 100, 255)
        self.set_game