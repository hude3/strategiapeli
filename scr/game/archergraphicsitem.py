from PyQt6.QtGui import QColor, QBrush, QPen, QPainter, QPolygonF, QPainterPath
from PyQt6.QtWidgets import QGraphicsItem
from PyQt6.QtCore import QPointF
from scr.game.unitgraphicsitem import UnitGraphicsItem

class ArcherGraphicsItem(UnitGraphicsItem):
    def __init__(self, unit, tile_size):
        super().__init__(unit, tile_size)

        self.color = self.unit.player.color
        self.width = 2
        self.points = [QPointF(tile_size * 0.5, tile_size * 0.75),QPointF(tile_size * 0.5, tile_size * 0.25),QPointF(tile_size * 0.25, tile_size * 0.25),QPointF(tile_size * 0.5, tile_size * 0),QPointF(tile_size * 0.75, tile_size * 0.25),QPointF(tile_size * 0.5, tile_size * 0.25),QPointF(tile_size * 0.5, tile_size * 0.75),QPointF(tile_size * 0.4, tile_size * 0.9),QPointF(tile_size * 0.5, tile_size * 0.75),QPointF(tile_size * 0.6, tile_size * 0.9)]
        self.UpdateLocation()

    def boundingRect(self):
        return self.shape().boundingRect()

    def shape(self):
        path = QPainterPath()
        path.addRect(0, 0, self.tile_size, self.tile_size)
        return path

    def paint(self, painter, option, widget):
        path = QPainterPath()  # Luo uuden QPainterPath-olion

        # Lisää pisteet polulle
        path.moveTo(self.points[0])
        for point in self.points[1:]:
            path.lineTo(point)

        # Piirrä polku halutulla värillä
        painter.setPen(QPen(self.color, 2))
        painter.drawPath(path)




