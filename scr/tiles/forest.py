from scr.tiles.tile import Tile


# Tilen alaluokka


class Forest(Tile):


    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'f'