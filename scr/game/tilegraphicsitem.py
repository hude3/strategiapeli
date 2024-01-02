
from PyQt6.QtCore import QRectF
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsRectItem, QPushButton
from PyQt6.QtGui import QColor







class TileGraphicsItem(QGraphicsRectItem):


    def __init__(self, tile, tile_size):
        super().__init__(QRectF(0,0,tile_size,tile_size))
        self.tile = tile
        self.tile_size = tile_size
        self.location = self.tile.location
        x = self.location[0]
        y = self.location[1]
        self.setPos(x * tile_size, y * tile_size)



    def mousePressEvent(self, *args, **kwargs):
        if self.tile.map.moving_unit != None:
            self.tile.map.set_tile_to_move_to(self.tile)
        else:
            if self.tile.map.game.gui.unit_panel != None:
                self.tile.map.game.gui.unit_panel.hide()
                self.tile.map.game.gui.unit_panel = None
                self.tile.map.attacking_unit = None
            elif self.tile.map.game.gui.city_panel != None:
                self.tile.map.game.gui.city_panel.hide()
                self.tile.map.game.gui.city_panel = None
            elif self.tile.map.game.gui.panel2 != None:
                self.tile.map.game.gui.panel2.hide()
                self.tile.map.game.gui.panel2 = None




