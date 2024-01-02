from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QColor, QBrush, QPen
from PyQt6.QtWidgets import QGraphicsItem

class CityGraphicsItem(QGraphicsItem):

    def __init__(self, city, tile_size):
        super().__init__()
        self.city = city
        self.tile_size = tile_size
        self.coordinates = self.city.coordinates
        self.setToolTip(f'City belonging to {self.city.player.name:s} / hp: {self.city.health_points:d}')
        self.UpdateLocation()

    def boundingRect(self):
        return QRectF(0, 0, self.tile_size, self.tile_size)

    def paint(self, painter, option, widget):
        # Draw a square for the tile
        pen = QPen(self.city.player.color, 2, Qt.PenStyle.DashLine)
        brush = QBrush(QColor(200, 200, 200, 255), Qt.BrushStyle.SolidPattern)
        painter.setPen(pen)

        painter.drawRect(-self.tile_size, -self.tile_size, 3* self.tile_size, 3*self.tile_size)

        # Draw the tower inside the square
        pen = QPen(QColor(0,0,0), 2, Qt.PenStyle.SolidLine)

        painter.setPen(pen)
        painter.setBrush(brush)
        tower_width = self.tile_size / 2
        tower_height = self.tile_size / 2
        tower_x = self.tile_size / 2 - tower_width / 2
        tower_y = self.tile_size / 2 - tower_height / 2
        painter.drawRect(tower_x, tower_y, tower_width, tower_height)

        # Draw the tower roof
        roof_width = tower_width / 5
        roof_height = roof_width
        roof_x = tower_x
        roof_y = tower_y - roof_height
        painter.drawRect(roof_x, roof_y, roof_width, roof_height)
        painter.drawRect(roof_x + roof_width*2, roof_y, roof_width, roof_height)
        painter.drawRect(roof_x+ roof_width*4, roof_y, roof_width, roof_height)




        # Draw the tower door
        brush = QBrush(self.city.player.color, Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        door_width = self.tile_size / 5
        door_height = self.tile_size / 3
        door_x = self.tile_size / 2 - door_width / 2
        door_y = tower_y + tower_height - door_height
        painter.drawRect(door_x, door_y, door_width, door_height)

    def UpdateLocation(self):
        self.coordinates = self.city.coordinates
        self.setPos(self.coordinates[0] * self.tile_size, self.coordinates[1] * self.tile_size)


    def mousePressEvent(self, *args, **kwargs):
        if self.city.player.game.map.attacking_unit == None and self.city.player == self.city.player.game.player:
            gui = self.city.player.game.gui
            gui.city_options_side_panel(self.city)
        elif self.city.player.game.map.attacking_unit == None:
            pass
        else:
            self.city.player.game.map.set_defending_city(self.city)

    def remove_from_scene(self):
        if self.scene() is not None:
            self.scene().removeItem(self)