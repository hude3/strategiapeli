from scr.tiles.tile import Tile


# Plains tulee olemaan ns. perus-Tile eli sillä ei ole oikeastaan mitään erikoisuuksia
class Plains(Tile):

    def __init__(self,x,y):
        super().__init__(x,y)
        self.type = 'p'
