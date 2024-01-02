import sys





# Unit toimii yläluokkana BattleUnit ja SupportUnit alaluokille, joiden alaluokat
# taas ovat pelin ns. hahmot



class Unit:


    def __init__(self, player, tile):
        self.set_tile(tile)
        self.name = None
        self.speed = 2
        self.health_points = None
        self.set_player(player)
        self.dead = False
        self.coordinates = self.tile.get_location()
        self.unit_pressed = False
        self.move_pressed = False
        self.has_moved = False
        self.graphicsitem = None
        self.cost = None



    def set_name(self, name):               # asettaa unitille nimen
        self.name = name



    def set_player(self,player):            # asettaa unitille pelaajan
        self.player = player
        self.player.units_list.append(self)


    def change_player(self, player):        # tilanteessa, jossa Unitin omistaja vaihtuu
        if player == self.player:
            return False
        else:
            self.player = player


    def set_tile(self, tile):       # asettaa hahmon tilelle
        self.tile = tile
        self.tile.set_unit(self)



    def delete_from_tile(self):             # poistaa tileltä
        if self.tile != None:
            self.tile.delete_unit()
            self.tile = None
        else:
            return False


    def move_to(self, tile):    # metodi, jolla hahmoa liikutetaan
        tile_location = tile.location
        own_location = self.coordinates
        distance = abs(tile_location[0] - own_location[0]) + abs(tile_location[1] - own_location[1])
        if distance <= self.speed and self.has_moved == False and tile.type != 'w' and tile.type != 'm' and tile.unit == None:                  # laskee siis muuttuuko etäisyys max speed
            self.delete_from_tile()
            self.set_tile(tile)
            self.coordinates = self.tile.location
            self.player.game.gui.update_unit_positions()
            self.player.game.gui.move_button.setText('Move to')
            self.player.game.gui.game.map.set_moving_unit(None)
            if self.player.name != 'AI':
                self.has_moved = True
            if self.player.game.gui.unit_panel != None:
                self.player.game.gui.unit_panel.hide()
                self.player.game.gui.unit_panel = None
            return True
        else:
            return False

    def set_next_turn(self):                # nollaa liikkumisen eli asettaa seuraavan vuoron
        self.has_moved = False





    def die(self):              # metodi, jolla hahmo tapetaan
        if self.dead == False:
            self.dead = True
            self.delete_from_tile()
            index = self.player.units_list.index(self)
            self.player.units_list.pop(index)
            index = self.player.game.gui.unit_items_list.index(self.graphicsitem)
            self.player.game.gui.unit_items_list.pop(index)
            self.graphicsitem.remove_from_scene()
            self.player.game.gui.scene.update()
            self.player.game.gui.event_happens(f"{self.player.name:s}'s {self.name:s} has died")
            if len(self.player.cities_list) == 0:
                self.player.game.end_game(self.player.name)
        else:
            return False


    def get_name(self):     # palauttaa nimen
        return self.name

    def get_player(self):       # palauttaa pelaajan
        return self.player

    def get_tile(self):         # palauttaa tilen
        return self.tile

    def paint_unit_graphics_item(self, tile_size):
        pass

    def set_speed(self, speed):         # asettaa nopeuden
        self.speed = speed