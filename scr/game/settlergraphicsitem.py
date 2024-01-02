from PyQt6.QtGui import QBrush, QColor, QPen
from PyQt6.QtCore import QRectF, Qt

from scr.game.unitgraphicsitem import UnitGraphicsItem


class SettlerGraphicsItem(UnitGraphicsItem):
    def __init__(self, unit, tile_size):
        super().__init__(unit, tile_size)



        self.pen = QPen(QColor(0, 0, 0))
        self.brush = QBrush(QColor(self.player.color))
        self.UpdateLocation()

    def boundingRect(self):
        return QRectF(0, 0, self.tile_size, self.tile_size)

    def paint(self, painter, option, widget):
        # Draw a square for the tile
        pen = QPen(QColor(0,0,0), 2, Qt.PenStyle.SolidLine)
        brush = QBrush(QColor(200, 200, 200, 255), Qt.BrushStyle.SolidPattern)
        painter.setPen(pen)
        painter.setBrush(brush)
        #painter.drawRect(self.boundingRect())

        # Draw the flag inside the square
        pen = QPen(QColor(0,0,0), 2, Qt.PenStyle.SolidLine)
        brush = QBrush(self.player.color, Qt.BrushStyle.SolidPattern)
        painter.setPen(pen)
        painter.setBrush(brush)
        flag_width = self.tile_size / 1.5
        flag_height = self.tile_size / 3
        flag_x = self.tile_size / 2 - flag_width / 2
        flag_y = flag_height / 5
        painter.drawRect(flag_x, flag_y, flag_width, flag_height)

        pole_x = self.tile_size / 2 - flag_width / 2
        pole_y = flag_height / 5
        pole_width = self.tile_size / 20
        pole_height = self.tile_size - flag_height / 5
        painter.drawRect(pole_x, pole_y, pole_width, pole_height)




    def mousePressEvent(self, *args, **kwargs):
        if self.unit.player.game.map.attacking_unit == None and self.unit.player == self.player.game.player:
            gui = self.unit.player.game.gui
            gui.settler_options_side_panel(self.unit)
            self.unit.unit_pressed = True
        elif self.unit.player.game.map.attacking_unit == None:
            pass
        else:
            self.unit.player.game.map.attacking_unit.attack(self.unit)