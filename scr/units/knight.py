from scr.units.battleunit import BattleUnit
from scr.game.knightgraphicsitem import KnightGraphicsItem

class Knight(BattleUnit):

    def __init__(self, player, tile):
        super().__init__(player, tile)
        self.speed = 3
        self.name = 'Knight'
        self.type = 'kn'
        self.cost = 3

    def paint_unit_graphics_item(self, tile_size):
        self.graphicsitem = KnightGraphicsItem(self, tile_size)
        return self.graphicsitem