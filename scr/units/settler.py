from scr.units.supportunit import SupportUnit
from scr.game.settlergraphicsitem import SettlerGraphicsItem
from scr.tiles.city import City

class Settler(SupportUnit):


    def __init__(self, player, tile):
        super().__init__(player, tile)
        self.name = 'Settler'
        self.type = 'se'
        self.cost = 5

    def paint_unit_graphics_item(self, tile_size):
        self.graphicsitem = SettlerGraphicsItem(self, tile_size)
        return self.graphicsitem



    def build_city(self):
        city = City(self.player, self.tile)
        self.die()
