from scr.units.unit import Unit

import random
import math




class BattleUnit(Unit):


    def __init__(self, player, tile):         # muodostaa BattleUnitin perusominaisuudet
        super().__init__(player, tile)
        self.health_points = 100        # lukuarvot vielä heittoja
        self.range = 1
        self.combat_strength = 10
        self.has_attacked = False


    def attack(self, unit):       # hyökkää toisen kimppuun
        distance = abs(self.coordinates[0] - unit.coordinates[0]) + abs(self.coordinates[1] - unit.coordinates[1])
        if unit.dead == False and unit.player != self.player and unit.health_points != None and distance <= self.range:    # eli onko kyseessä battle vai supportunit
            self.player.game.gui.event_happens(f"{self.player.name:s}'s {self.name:s} has attacked {unit.player.name:s}'s {unit.name:s}")
            damage = self.calculate_damage(unit)
            unit.take_damage(damage)
            self.player.game.gui.attack_button.setText('Cannot attack')
            self.player.game.map.set_attacking_unit(None)
            self.player.game.map.set_defending_unit(None)
            self.has_attacked = True
            if self.player.game.gui.unit_panel != None:
                self.player.game.gui.unit_panel.hide()
                self.player.game.gui.unit_panel = None
        elif unit.player != self.player and distance <= self.range:          # kyseessä support, kuolee samantien
            self.player.game.gui.event_happens(f"{self.player.name:s}'s {self.name:s} has attacked {unit.player.name:s}'s {unit.name:s}")
            unit.die()
            self.player.game.gui.attack_button.setText('Cannot attack')
            self.player.game.map.set_attacking_unit(None)
            self.player.game.map.set_defending_unit(None)
            self.has_attacked = True
            if self.player.game.gui.unit_panel != None:
                self.player.game.gui.unit_panel.hide()
                self.player.game.gui.unit_panel = None
        else:
            return False


    def attack_city(self, city):
        distance = abs(self.coordinates[0] - city.coordinates[0]) + abs(self.coordinates[1] - city.coordinates[1])
        damage = self.calculate_damage(city)

        if distance <= self.range and city.player != self.player:
            self.player.game.gui.event_happens(f"{self.player.name:s}'s {self.name:s} has attacked {city.player.name:s}'s city")
            city.take_damage(damage)
            self.player.game.gui.attack_button.setText('Cannot attack')
            self.player.game.map.set_attacking_unit(None)
            self.player.game.map.set_defending_city(None)
            self.has_attacked = True
            if self.player.game.gui.unit_panel != None:
                self.player.game.gui.unit_panel.hide()
                self.player.game.gui.unit_panel = None

        else:
            return False
    def take_damage(self, damage):      # ottaa vahinkoa
        hp = self.health_points
        if hp - damage <= 0:
            self.health_points = 0
            self.die()
        elif hp - damage > 0:
            self.health_points = hp - damage
        self.graphicsitem.setToolTip(f'{self.name:s} belonging to {self.player.name:s} / hp: {self.health_points:d}')


    def set_next_turn(self):
        self.has_moved = False
        self.has_attacked = False

    def set_health_points(self, hp):
        self.health_points = hp


    Seed = 3849

    def calculate_damage(self, unit2):  # parametrit BattleUnitteja, 1 hyökkää 2 kohti
        random.seed(BattleUnit.Seed)

        combat_strength1 = self.combat_strength
        combat_strength2 = unit2.combat_strength
        defence_bonus = unit2.tile.defence_bonus  # unit 2 tilen antama bonus puolustukseen

        # damage on integer simppeliyden vuoksi
        damage = int(30 * math.exp(((combat_strength1 - (combat_strength2 * defence_bonus)) / 25)  * (random.randint(75, 125) / 100)))

        return damage

    def set_combat_strength(self, cs):
        self.combat_strength = cs
    def set_range(self, range):
        self.range = range