from scr.units.battleunit import BattleUnit
from scr.game.swordmangraphicsitem import SwordManGraphicsItem


class Swordsman(BattleUnit):

    def __init__(self, player, tile):
        super().__init__(player, tile)
        self.name = 'Swordsman'
        self.health_points = 150
        self.combat_strength = 15
        self.speed = 2
        self.type = 'sw'
        self.cost = 2

    def paint_unit_graphics_item(self, tile_size):
        self.graphicsitem = SwordManGraphicsItem(self, tile_size)
        return self.graphicsitem


