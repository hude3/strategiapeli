from scr.game.citygraphicsitem import CityGraphicsItem






class City:


    def __init__(self, player, tile):

        self.player = player
        self.tile = tile
        self.player.cities_list.append(self)
        self.coordinates = self.tile.location
        self.city_pressed = False
        self.health_points = 100
        self.combat_strength = 20
        self.dead = False


    def paint_graphics_item(self, tile_size):
        self.graphicsitem = CityGraphicsItem(self, tile_size)
        return self.graphicsitem

    def take_damage(self, damage):
        hp = self.health_points
        if hp - damage <= 0:
            self.health_points = 0
            self.die()
        elif hp - damage > 0:
            self.health_points = hp - damage
        self.graphicsitem.setToolTip(f'City belonging to {self.player.name:s} / hp: {self.health_points:d}')


    def die(self):
        if self.dead == False:
            self.dead = True
            self.delete_from_tile()
            index = self.player.cities_list.index(self)
            self.player.cities_list.pop(index)
            index = self.player.game.gui.city_items_list.index(self.graphicsitem)
            self.player.game.gui.city_items_list.pop(index)
            self.graphicsitem.remove_from_scene()
            if len(self.player.cities_list) == 0:
                self.player.game.end_game(self.player.name)
        else:
            return False

    def delete_from_tile(self):
        if self.tile != None:
            self.tile.delete_city()
            self.tile = None
        else:
            return False

    def set_hp(self,hp):
        self.health_points = hp