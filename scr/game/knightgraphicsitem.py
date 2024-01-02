from PyQt6.QtGui import QBrush, QColor, QPainter, QPen, QPainterPath
from PyQt6.QtWidgets import QGraphicsItem, QGraphicsRectItem
from PyQt6.QtCore import QRectF, QLineF, QPointF
from scr.game.unitgraphicsitem import UnitGraphicsItem

class KnightGraphicsItem(UnitGraphicsItem):
    def __init__(self, unit, tile_size):
        super().__init__(unit, tile_size)

        self.width = tile_size * 0.5
        self.height = tile_size * 0.8

        # määritetään muuttujat hevosen eri osille
        self.body_width = 0.6 * tile_size
        self.body_height = 0.8 * tile_size
        self.head_size = 0.4 * tile_size
        self.leg_width = 0.1 * tile_size
        self.leg_height = 0.5 * tile_size
        self.ear_size = 0.2 * tile_size
        self.head_offset = 0.3 * tile_size



        # määritetään harmaa harjusväri ja hevosen väri pelaajan mukaan
        self.brush = QBrush(QColor(128, 128, 128))
        self.color = QBrush(unit.player.color)

        self.UpdateLocation()



    def boundingRect(self):
        return self.shape().boundingRect()


    def shape(self):
        path = QPainterPath()
        path.addRect(0, 0, self.tile_size, self.tile_size)
        return path


    def paint(self, painter, option, widget):
        # piirretään vartalo
        painter.setBrush(self.color)
        painter.setPen(QPen(QColor(0, 0, 0), 2))
        painter.drawEllipse((self.tile_size - self.body_width) / 2,self.tile_size - self.body_height, self.body_width, self.body_height)

        # piirrä miekan kahva
        handle_width = self.width // 5
        handle_height = self.height // 3
        handle_x = (self.width - handle_width) // 2
        handle_y = self.height - handle_height
        handle_rect = QRectF(handle_x, handle_y, handle_width, handle_height)
        painter.setBrush(QBrush(QColor(100, 100, 100)))  # tummanharmaa
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




