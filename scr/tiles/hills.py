from scr.tiles.tile import Tile


class Hills(Tile):


    def __init__(self, x, y):
        super().__init__(x,y)
        self.defence_bonus = 1.25
        self.type = 'h'