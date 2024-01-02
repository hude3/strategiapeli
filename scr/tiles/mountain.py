from scr.tiles.tile import Tile


class Mountain(Tile):

    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = 'm'