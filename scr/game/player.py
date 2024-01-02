from PyQt6.QtGui import QColor



class Player:                       # pelaajaolio



    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cities_list = []
        self.units_list = []
        self.color = QColor(255, 0, 0)



    def set_game(self,game):
        self.game = game

    def set_color(self, tuple):
        self.color = QColor(tuple[0], tuple[1], tuple[2])