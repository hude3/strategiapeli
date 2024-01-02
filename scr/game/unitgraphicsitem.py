from PyQt6.QtWidgets import QGraphicsItem
from PyQt6.QtGui import QBrush

class UnitGraphicsItem(QGraphicsItem):



    def __init__(self, unit, tile_size):
        super().__init__()
        self.unit = unit
        self.tile_size = tile_size
        self.player = unit.player
        self.coordinates = unit.coordinates
        if self.unit.health_points != None:
            self.setToolTip(f'{self.unit.name:s} belonging to {self.unit.player.name:s} / hp: {self.unit.health_points:d}')
        else:
            self.setToolTip(f'{self.unit.name:s} belonging to {self.unit.player.name:s} {str(id(self.unit)):s}')






    def UpdateLocation(self):
        self.coordinates = self.unit.coordinates
        self.setPos(self.coordinates[0] * self.tile_size, self.coordinates[1] * self.tile_size)


    def remove_from_scene(self):
        if self.scene() is not None:
            self.setVisible(False)
            self.scene().removeItem(self)


    def mousePressEvent(self, *args, **kwargs):             # kun painat unittia, sivuun tulee paneeli mitä voit tehdä sillä
        if self.unit.player.game.map.attacking_unit == None and self.unit.player == self.player.game.player:
            gui = self.unit.player.game.gui
            gui.show_unit_options_side_panel(self.unit)
            self.unit.unit_pressed = True
        elif self.unit.player.game.map.attacking_unit == None:
            pass
        else:
            self.unit.player.game.map.set_defending_unit(self.unit)