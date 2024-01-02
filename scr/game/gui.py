from PyQt6 import QtWidgets

from PyQt6.QtWidgets import QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QColor, QAction, QIcon

from scr.tiles.water import Water
from scr.tiles.plains import Plains
from scr.tiles.mountain import Mountain
from scr.tiles.forest import Forest
from scr.tiles.hills import Hills
from scr.game.game_saver import GameSaver




# alotan jo GUI:n tekemisen, koska haluan saada itselleni visualisoinnin, mitä tapahtuu


class GUI(QtWidgets.QMainWindow):


    def __init__(self, map, tile_size):
        super().__init__()

        self.unit_items_list = []
        self.city_items_list = []



        self.main_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.main_widget)
        self.horizontal = QtWidgets.QHBoxLayout()

        self.centralWidget().setLayout(self.horizontal)
        self.map = map
        self.game = self.map.game
        self.tile_size = int(tile_size)
        self.map_width = int(self.map.get_width())
        self.map_length = int(self.map.get_length())
        self.statusBar().setStatusTip('Statusbar')

        self.init_buttons()

        self.add_menubar()      # lisää menubarin


        self.unit_panel = None
        self.city_panel = None


        self.init_window()
        self.init_side_panel()
        self.add_map_tile_items()
        self.add_city_items()
        self.add_unit_items()



    def init_window(self):
        self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle('Strategy Game')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, self.map_width * self.tile_size, self.map_length * self.tile_size)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)


    def init_side_panel(self):                      # lisää main viewin oikealle puolelle paneelin

        self.side_widget = QtWidgets.QWidget()
        self.side_panel = QtWidgets.QVBoxLayout()
        self.money_label = QLabel(f'Money amount: {self.game.player.money:d}')
        self.event_list = QtWidgets.QListWidget()

        self.side_panel.addWidget(self.event_list)
        self.side_panel.addWidget(self.money_label)
        self.side_panel.addWidget(self.next_button)
        self.side_widget.setLayout(self.side_panel)
        self.horizontal.addWidget(self.side_widget)



    def show_unit_options_side_panel(self, unit):
        if self.unit_panel == None and self.city_panel == None:
            self.unit = unit
            self.unit_panel = QtWidgets.QWidget()
            self.unit_layout = QtWidgets.QVBoxLayout()

            if self.unit.has_attacked == False:
                self.attack_button.setText('Attack')
                self.unit_layout.addWidget(self.attack_button)
            else:
                self.attack_button.setText('Cannot attack')
            if self.unit.has_moved == False:
                self.move_button.setText('Move to')
                self.unit_layout.addWidget(self.move_button)
            else:
                self.move_button.setText('Cannot move')
                self.unit_layout.addWidget(self.move_button)
            self.unit_panel.setLayout(self.unit_layout)
            self.side_panel.addWidget(self.unit_panel)

    def settler_options_side_panel(self, settler):
        if self.unit_panel == None and self.city_panel == None:
            self.unit = settler
            self.unit_panel = QtWidgets.QWidget()
            self.unit_layout = QtWidgets.QVBoxLayout()

            self.unit_layout.addWidget(self.settle_button)
            if self.unit.has_moved == False:
                self.move_button.setText('Move to')
                self.unit_layout.addWidget(self.move_button)
            else:
                self.move_button.setText('Cannot move')
                self.unit_layout.addWidget(self.move_button)
            self.unit_panel.setLayout(self.unit_layout)
            self.side_panel.addWidget(self.unit_panel)


    def city_options_side_panel(self, city):
        if self.unit_panel == None and self.city_panel == None:
            self.city = city
            self.city_panel = QtWidgets.QWidget()
            self.panel_layout = QtWidgets.QVBoxLayout()

            self.panel_layout.addWidget(self.build_unit_button)

            self.city_panel.setLayout(self.panel_layout)
            self.side_panel.addWidget(self.city_panel)

    def build_units_panel(self):
        self.panel2 = QtWidgets.QWidget()
        self.panel2_layout = QtWidgets.QVBoxLayout()

        self.panel2_layout.addWidget(self.swordsman_button)
        self.panel2_layout.addWidget(self.archer_button)
        self.panel2_layout.addWidget(self.knight_button)
        self.panel2_layout.addWidget(self.settler_button)

        self.panel2.setLayout(self.panel2_layout)
        self.side_panel.addWidget(self.panel2)




    def init_buttons(self):
        self.attack_button = QPushButton("Attack")
        self.attack_button.clicked.connect(self.attack_button_clicked)

        self.move_button = QPushButton("Move to")
        self.move_button.clicked.connect(self.move_button_clicked)

        self.next_button = QPushButton(f"Next turn / Turn number {self.game.turn_counter:d}")
        self.next_button.clicked.connect(self.next_turn_clicked)
        self.next_button.setShortcut('Space')

        self.settle_button = QPushButton('Settle a city')
        self.settle_button.clicked.connect(self.settle_button_clicked)

        self.build_unit_button = QPushButton('Build an unit')
        self.build_unit_button.clicked.connect(self.build_unit_button_clicked)

        self.archer_button = QPushButton('Build an Archer / 2 coins')
        self.archer_button.clicked.connect(self.archer_button_clicked)


        self.knight_button = QPushButton('Build a Knight / 3 coins')
        self.knight_button.clicked.connect(self.knight_button_clicked)

        self.swordsman_button = QPushButton('Build a Swordsman / 2 coins')
        self.swordsman_button.clicked.connect(self.swordsman_button_clicked)

        self.settler_button = QPushButton('Build a Settler / 5 coins')
        self.settler_button.clicked.connect(self.settler_button_clicked)






    # seuraavat koodit käsittelevät kun nappeja painellaan

    def move_button_clicked(self):
        if self.move_button.text() == 'Move to':
            self.move_button.setText('Click where to move')
            self.game.map.set_moving_unit(self.unit)
        elif self.move_button.text() == 'Cannot move':
            pass
        else:
            self.move_button.setText('Move to')
            self.game.map.set_moving_unit(None)

    def next_turn_clicked(self):
        self.game.next_turn()
        self.move_button.setText('Move to')
        self.attack_button.setText('Attack')
        self.next_button.setText(f"Next turn / Turn number {self.game.turn_counter:d}")
        self.money_label.setText(f'Money amount: {self.game.player.money:d}')



    def settle_button_clicked(self):
        self.unit.build_city()
        self.add_city_items()
        self.update_city_positions()
        if self.unit_panel != None:
            self.unit_panel.hide()
            self.unit_panel = None


    def attack_button_clicked(self):
        if self.attack_button.text() == 'Attack':
            self.attack_button.setText('Click what unit to attack')
            self.game.map.set_attacking_unit(self.unit)
        elif self.attack_button.text() == 'Cannot attack':
            pass
        else:
            self.attack_button.setText('Attack')
            self.game.map.set_attacking_unit(None)



    # seuraavat koodit koskevat hahmojen luomista kaupungissa
    def build_unit_button_clicked(self):
        self.city_panel.hide()
        self.city_panel = None
        self.build_units_panel()


    def swordsman_button_clicked(self):
        self.game.build_unit('sw',self.city)
        self.add_unit_items()
        self.panel2.hide()

    def archer_button_clicked(self):
        self.game.build_unit('ar', self.city)
        self.add_unit_items()
        self.panel2.hide()

    def knight_button_clicked(self):
        self.game.build_unit('kn', self.city)
        self.add_unit_items()
        self.panel2.hide()

    def settler_button_clicked(self):
        self.game.build_unit('se', self.city)
        self.add_unit_items()
        self.panel2.hide()










    def add_menubar(self):      # otin harjoitusesimerkeistä
        save_game = QAction(QIcon(None), 'Save', self)
        save_game.triggered.connect(self.save_game)
        menubar = self.menuBar()  # luodaan menu bar -olio
        file_menu = menubar.addMenu('&File')  # lisätään menubariin yllä luodut toiminnot

        file_menu.addAction(save_game)



    def save_game(self):
        filename, ok = QtWidgets.QInputDialog.getText(self, 'File name', 'Enter the name of the save file')
        if ok:
            saver = GameSaver()
            saver.save_game(self.game, filename)


    def add_map_tile_items(self):

        map_width = self.map.get_width()
        map_length = self.map.get_length()
        for x in range(map_width):
            for y in range(map_length):
                tile = self.map.get_tile(x,y)
                r = tile.color[0]
                g = tile.color[1]
                b = tile.color[2]

                tile_graphics_item = tile.make_tile_graphics_item(self.tile_size)

                if type(tile) == type(Water(x,y)):
                    tile_graphics_item.setBrush(QColor(r,g,b))           # sininen
                    tile_graphics_item.setToolTip('Water')
                elif type(tile) == type(Hills(x,y)):
                    tile_graphics_item.setBrush(QColor(r,g,b))      # harmaa
                    tile_graphics_item.setToolTip('Hills')
                elif type(tile) == type(Forest(x,y)):
                    tile_graphics_item.setBrush(QColor(r,g,b))        # tummanvihreä
                    tile_graphics_item.setToolTip('Forest')
                elif type(tile) == type(Plains(x,y)):
                    tile_graphics_item.setBrush(QColor(r,g,b))       # vaaleanvihreä
                    tile_graphics_item.setToolTip('Plains')
                elif type(tile) == type(Mountain(x,y)):
                    tile_graphics_item.setBrush(QColor(r,g,b))            # tummanharmaa
                    tile_graphics_item.setToolTip('Mountain')

                self.scene.addItem(tile_graphics_item)



    def add_unit_items(self):

        for i in range(len(self.game.player.units_list)):
            unit = self.game.player.units_list[i]
            if unit.graphicsitem == None:
                graphicsitem = unit.paint_unit_graphics_item(self.tile_size)
                self.unit_items_list.append(graphicsitem)
                self.scene.addItem(graphicsitem)

        for i in range(len(self.game.AI.units_list)):
            unit = self.game.AI.units_list[i]
            if unit.graphicsitem == None:
                graphicsitem = unit.paint_unit_graphics_item(self.tile_size)
                self.unit_items_list.append(graphicsitem)
                self.scene.addItem(graphicsitem)

    def add_city_items(self):
        for i in range(len(self.game.player.cities_list)):
            city = self.game.player.cities_list[i]

            graphicsitem = city.paint_graphics_item(self.tile_size)
            self.city_items_list.append(graphicsitem)

            self.scene.addItem(graphicsitem)

        for i in range(len(self.game.AI.cities_list)):
            city = self.game.AI.cities_list[i]

            graphicsitem = city.paint_graphics_item(self.tile_size)
            self.city_items_list.append(graphicsitem)

            self.scene.addItem(graphicsitem)


    def update_unit_positions(self):
        for i in range(len(self.unit_items_list)):
            self.unit_items_list[i].UpdateLocation()


    def update_city_positions(self):
        for i in range(len(self.city_items_list)):
            self.city_items_list[i].UpdateLocation()

    def event_happens(self, message):
        self.event_list.addItem(message)



class WinnerWindow(QtWidgets.QWidget):

    def __init__(self, winning_player_name, turns):
        super().__init__()
        self.setWindowTitle('Winner winner chicken dinner!')
        self.layout = QtWidgets.QHBoxLayout()
        self.label = QLabel(f'Congrats on the win {winning_player_name:s}. You won the opponent in {turns:d} turns')
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setGeometry(300,300,200,200)
        self.show()

