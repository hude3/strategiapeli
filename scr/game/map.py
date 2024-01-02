# tämä tiedosto hoitaa pelin kartan luomisen
from scr.tiles.water import Water
from scr.tiles.plains import Plains
from scr.tiles.mountain import Mountain
from scr.tiles.forest import Forest
from scr.tiles.hills import Hills

import random



class Map:

    seed = 69




    def __init__(self, width, height,game, random=True):      # kartan muodostaminen kutoskierroksen tehtävästä RobotWorld
        self.tiles = [None] * width
        self.game = game
        for x in range(self.get_width()):
            self.tiles[x] = [None] * height

        if random:                                          # parametri random kertoo että muodostetaanko kartta randomisti vai tallennustiedostosta
            self.set_tiles()


        self.moving_unit = None
        self.attacking_unit = None
        self.defending_unit = None
        self.defending_city = None



    def get_width(self):            # palauttaa kartan leveyden
        
        return len(self.tiles)

    def set_game(self, game):
        self.game = game

    def get_length(self):           # palauttaa pituuden

        return len(self.tiles[0])

    def set_tiles(self):            # asettaa laatat satunnaisgeneraatiolla
        #water = w
        #plains = p
        #mountain = m
        #hills = h
        #forest = f

        tile_types = ['w', 'p', 'm', 'h', 'f']
        tile_weights = [self.game.config.w_amount, self.game.config.p_amount, self.game.config.m_amount, self.game.config.h_amount, self.game.config.f_amount]      # antaa satunnaisgeneraatiolle jokaisen laatan painoarvon,
                                                # kirjoitan ulkoiseen tiedostoon myöhemmin



        for x in range(self.get_width()):
            for y in range(self.get_length()):
                tile_type = random.choices(tile_types, weights = tile_weights)

                self.tiles[x][y] = self.make_tile_object(tile_type[0], x, y)
                self.tiles[x][y].set_map(self)


    def make_tile_object(self,type, x, y):     # palauttaa oikean tile olion tyyppiä vastaan
        if type == 'w':
            tile = Water(x,y)
            tile.set_color(self.game.config.w_color)
            tile.set_defence_mp(self.game.config.w_def)
            return tile
        elif type == 'p':
            tile = Plains(x,y)
            tile.set_color(self.game.config.p_color)
            tile.set_defence_mp(self.game.config.p_def)
            return tile
        elif type == 'm':
            tile = Mountain(x,y)
            tile.set_color(self.game.config.m_color)
            tile.set_defence_mp(self.game.config.m_def)
            return tile
        elif type == 'h':
            tile = Hills(x,y)
            tile.set_color(self.game.config.h_color)
            tile.set_defence_mp(self.game.config.h_def)
            return tile
        elif type == 'f':
            tile = Forest(x,y)
            tile.set_color(self.game.config.f_color)
            tile.set_defence_mp(self.game.config.f_def)
            return tile

    def get_tile(self, x, y):
        width = self.get_width()
        length = self.get_length()
        if (x < 0) or (x >= width) or (y < 0) or (y >= length):
            return False
        else:
            return self.tiles[x][y]

    def set_moving_unit(self, unit):        # määrittelee mikä unit liikkuu
        self.moving_unit = unit

    def set_attacking_unit(self, unit):     # määrittelee mikä unit hyökkää
        self.attacking_unit = unit

    def set_defending_unit(self, unit):     # asettaa puolustavan unitin
        self.defending_unit = unit

        if self.attacking_unit != None:
            self.attacking_unit.attack(self.defending_unit)

    def set_defending_city(self, city):     # asettaa puolustavan cityn
        self.defending_city = city

        if self.attacking_unit != None:
            self.attacking_unit.attack_city(self.defending_city)


    def set_tile_to_move_to(self, tile):
        self.tile_to_move = tile

        if self.moving_unit != None:
            self.moving_unit.move_to(tile)


    def set_saved_tile(self, type, x, y):                   # typet: f = forest, w = water, h = hills, m = mountain, p = plains
                                                            # asettaa tilet tallennuksen pohjalta
        self.tiles[x][y] = self.make_tile_object(type, x, y)
        self.tiles[x][y].set_map(self)


