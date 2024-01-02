from scr.units.battleunit import BattleUnit
from scr.game.archergraphicsitem import ArcherGraphicsItem

class Archer(BattleUnit):

    def __init__(self, player, tile):
        super().__init__(player, tile)
        self.range = 2
        self.name = 'Archer'
        self.type = 'ar'
        self.health_points = 70
        self.cost = 2


    def paint_unit_graphics_item(self, tile_size):
        self.graphicsitem = ArcherGraphicsItem(self, tile_size)
        return self.graphicsitem