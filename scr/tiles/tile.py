from scr.game.tilegraphicsitem import TileGraphicsItem


# yläluokka kaikille Tile olioille

# huom. luokan pohjalle tehty TileGraphicsItem-olio



class Tile:

    def __init__(self, x, y):
        self.unit = None
        self.city = None
        self.type = None
        self.movement = 1       # kerroin, joka kertoo Tilen helppokulkuisuudesta
        self.defence_bonus = 1  # kerroin, joka kertoo Tilen puolustusbonuksesta
        self.location = (x, y)
        self.tile_clicked = False




    def set_unit(self,unit):    # metodi lisää unitin Tilelle
        if self.unit == None:
            self.unit = unit
        else:
            return False

    def delete_unit(self):      # poistaa Unitin tileltä
        if self.unit != None:
            self.unit = None
        else:
            return False




    def set_city(self, city):   # asettaa kaupungin
        if self.city == None:
            self.city = city
        else:
            return False

    def delete_city(self):      # poistaa cityn tileltä
        if self.city != None:
            self.city = None


    def get_location(self):     # palauttaa sijainnin
        return self.location

    def set_map(self, map):     # asettaa tilelle kartan
        self.map = map

    def set_color(self, tuple): # asettaa tilen värin
        self.color = tuple

    def set_defence_mp(self, defence):      # asettaa tilen defence multiplierin
        self.defence_bonus = defence
    def make_tile_graphics_item(self, tile_size):       # luodaan täällä tilegraphicsitem, jotta jokaisella tilellä olisi oma

        self.tile_graphics_item = TileGraphicsItem(self, tile_size)
        return self.tile_graphics_item