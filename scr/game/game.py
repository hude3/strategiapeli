from scr.game.map import Map
from scr.game.player import Player
from scr.game.gui import GUI, WinnerWindow
from scr.units.swordsman import Swordsman
from scr.units.archer import Archer
from scr.units.knight import Knight
from scr.units.settler import Settler
from scr.game.game_configuring import Configure
from scr.game.ai_player import Aiplayer
from scr.game.ai import AI

# tämä olio vastaa pelin hallinnasta


class Game:

    def __init__(self):
        self.config = Configure()               # tuottaa configurointiolion johon tallennetaan peliin riippuvat arvot
        self.config.config()


        self.map = None
        self.gui = None
        self.player = None
        self.ai_brain = AI()
        self.set_AI()
        self.set_turn_counter()









    def set_random_map(self, width, height):                    # tekee pelille satunnaisgeneraation kartan ja asettaa sen ala ja yläkulmiin settlerit pelin aloittamista varten
        self.map = Map(width, height,self)

        settler = Settler(self.player, self.map.get_tile(0, 0))
        settler.set_speed(self.config.se_speed)
        aisettler = Settler(self.AI, self.map.get_tile(width-1,height-1))
        aisettler.set_speed(self.config.se_speed)
    def set_saved_map(self, width, height):                     # tekee pelille kartan tallennustiedoston pohjalta
        self.map = Map(width, height, self, False)
        self.map.game = self

    def set_player(self, name, money=0):                        # asettaa pelaajan ja sen rahamäärän
        self.player = Player(name, money)
        self.player.set_game(self)
        self.player.set_color(self.config.pl_color)

    def set_AI(self, name=None, money=0):                       # asettaa aipelaajan
        self.AI = Aiplayer(name, money)
        self.AI.set_game(self)
        self.AI.set_color(self.config.ai_color)

    def set_gui(self, tile_size):                               # luo grafiikanhallinnointiolion
        self.gui = GUI(self.map, tile_size)

    def set_turn_counter(self, turn=1):                         # laskee vuorot, automaattisesti alussa vuoro on 1
        self.turn_counter = turn

    def next_turn(self):
        self.ai_turn()

        for i in range(len(self.player.units_list)):
            self.player.units_list[i].set_next_turn()
        for i in range(len(self.AI.units_list)):
            self.AI.units_list[i].set_next_turn()

        self.player.money = self.player.money + len(self.player.cities_list)    # lisää pelaajille rahaa, 1 raha per vuoro per kaupunki
        self.AI.money = self.AI.money + len(self.AI.cities_list)

        self.turn_counter += 1

    def build_unit(self, unit, city):           # rakentaa unitin, kun peli on kesken, rahaa vastaan

                                                # unit saa parametrikseen numeron
                                                # swordsman = sw
                                                # archer = ar
                                                # knight = kn
                                                # settler = se
                                                # builder = bu

        build_coordinates = (city.coordinates[0],city.coordinates[1])       # rakentaa unitin cityn päälle





        if unit == 'sw' and city.player.money >= self.config.sw_cost:        # eli rahaa vaaditaan kaksi, että voi luoda swordsmanin
            build_unit = Swordsman(city.player,self.map.get_tile(build_coordinates[0], build_coordinates[1]))
            build_unit.set_speed(self.config.sw_speed)
            build_unit.set_combat_strength(self.config.sw_combat)
            build_unit.set_health_points(self.config.sw_hp)
            build_unit.set_name(self.config.sw_name)
            build_unit.set_range(self.config.sw_range)
            city.player.money += -self.config.sw_cost
        elif unit == 'ar' and city.player.money >= self.config.ar_cost:
            build_unit = Archer(city.player,self.map.get_tile(build_coordinates[0], build_coordinates[1]))
            build_unit.set_speed(self.config.ar_speed)
            build_unit.set_combat_strength(self.config.ar_combat)
            build_unit.set_health_points(self.config.ar_hp)
            build_unit.set_name(self.config.ar_name)
            build_unit.set_range(self.config.ar_range)
            city.player.money += -self.config.ar_cost
        elif unit == 'kn' and city.player.money >= self.config.kn_cost:
            build_unit = Knight(city.player,self.map.get_tile(build_coordinates[0], build_coordinates[1]))
            build_unit.set_speed(self.config.kn_speed)
            build_unit.set_combat_strength(self.config.kn_combat)
            build_unit.set_health_points(self.config.kn_hp)
            build_unit.set_name(self.config.kn_name)
            build_unit.set_range(self.config.kn_range)
            city.player.money += -self.config.kn_cost
        elif unit == 'se' and city.player.money >= self.config.se_cost:
            build_unit = Settler(city.player,self.map.get_tile(build_coordinates[0], build_coordinates[1]))
            build_unit.set_speed(self.config.se_speed)
            build_unit.set_name(self.config.se_name)
            city.player.money += -self.config.se_cost

        else:
            return False
        self.gui.money_label.setText(f'Money amount: {self.player.money:d}')
        build_unit.paint_unit_graphics_item

    def build_saved_unit(self, unit, tile, player):         # rakentaa unitin tallennustiedoston pohjalta



        if unit == 'sw':  # eli rahaa vaaditaan kaksi, että voi luoda swordsmanin
            build_unit = Swordsman(player, tile)
            build_unit.set_speed(self.config.sw_speed)
            build_unit.set_combat_strength(self.config.sw_combat)
            build_unit.set_health_points(self.config.sw_hp)
            build_unit.set_name(self.config.sw_name)
            build_unit.set_range(self.config.sw_range)
        elif unit == 'ar':
            build_unit = Archer(player, tile)
            build_unit.set_speed(self.config.ar_speed)
            build_unit.set_combat_strength(self.config.ar_combat)
            build_unit.set_health_points(self.config.ar_hp)
            build_unit.set_name(self.config.ar_name)
            build_unit.set_range(self.config.ar_range)

        elif unit == 'kn':
            build_unit = Knight(player, tile)
            build_unit.set_speed(self.config.kn_speed)
            build_unit.set_combat_strength(self.config.kn_combat)
            build_unit.set_health_points(self.config.kn_hp)
            build_unit.set_name(self.config.kn_name)
            build_unit.set_range(self.config.kn_range)

        elif unit == 'se':
            build_unit = Settler(player, tile)
            build_unit.set_speed(self.config.se_speed)
            build_unit.set_name(self.config.se_name)



        else:
            return False

        return build_unit

    def end_game(self, name):                       # lopettaa pelin
        self.gui.close()
        if name == self.AI.name:
            self.window = WinnerWindow(self.player.name, self.turn_counter)
        else:
            self.window = WinnerWindow(self.AI.name, self.turn_counter)
        pass



    def ai_turn(self):                              # aktivoi ai:n vuoron
        for ai_unit in self.AI.units_list:
            if ai_unit.health_points == None:       # settlerillä hp on none
                self.ai_brain.evaluate_settler_actions(self, ai_unit)
                self.ai_brain.execute_action()
            else:
                self.ai_brain.evaluate_battleunit_actions(self, ai_unit)
                self.ai_brain.execute_action()
        for ai_city in self.AI.cities_list:
            self.ai_brain.evaluate_city_actions(self, ai_city)
            self.ai_brain.execute_action()