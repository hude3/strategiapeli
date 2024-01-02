from PyQt6.QtCore import QRectF, QLineF, QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen
from PyQt6.QtWidgets import QGraphicsItem
from scr.game.unitgraphicsitem import UnitGraphicsItem

class SwordManGraphicsItem(UnitGraphicsItem):
    def __init__(self,unit, tile_size):
        super().__init__(unit, tile_size)
        self.width = tile_size
        self.height = tile_size

        self.UpdateLocation()

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(QColor(0,0,0), 2))


        # piirrä miekan kahva
        handle_width = self.width // 5
        handle_height = self.height // 3
        handle_x = (self.width - handle_width) // 2
        handle_y = self.height - handle_height
        handle_rect = QRectF(handle_x, handle_y, handle_width, handle_height)
        painter.setBrush(QBrush(QColor(100,100,100)))   # tummanharmaa
        painter.drawRect(handle_rect)

        # piirrä miekan terä
        blade_width = self.width // 4
        blade_height = self.height * 2 // 3
        blade_x = (self.width - blade_width) // 2
        blade_y = handle_y - blade_height
        blade_rect = QRectF(blade_x, blade_y, blade_width, blade_height)
        painter.setBrush(QBrush(self.unit.player.color))
        painter.drawRect(blade_rect)



        # piirrä miekan väistin (se poikittainen osa tupen kahvan yläpuolella
        guard_line = QLineF(QPointF(blade_x - handle_width, blade_y + blade_height), QPointF(blade_x + blade_width + handle_width, blade_y + blade_height))
        painter.drawLine(guard_line)



