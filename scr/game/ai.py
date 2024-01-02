import random
class AI:
    def __init__(self):
        self.init_city_actions()
        self.init_battleunit_actions()
        self.init_settler_actions()
        self.current_action = None



    def init_city_actions(self):
        self.city_actions = []
        self.city_actions.append(BuildArcher())
        self.city_actions.append(BuildSwordsman())
        self.city_actions.append(BuildKnight())
        self.city_actions.append(BuildSettler())
        self.city_actions.append(DoNothing())

    def init_battleunit_actions(self):
        self.battleunit_actions = []
        self.battleunit_actions.append(MoveToUnits())
        self.battleunit_actions.append(MoveToCity())
        self.battleunit_actions.append(AttackUnits())
        self.battleunit_actions.append(AttackCity())
        self.battleunit_actions.append(DoNothing())

    def init_settler_actions(self):
        self.settler_actions = []
        self.settler_actions.append(MoveToSettle())
        self.settler_actions.append(Settle())



    def evaluate_battleunit_actions(self, game, unit):      # arvioi battleunittien tehtäviä päätöksiä
        for action in self.battleunit_actions:
            action.evaluate(game, unit)

        self.battleunit_actions.sort(key=lambda x: x.priority, reverse=True)
        self.current_action = self.battleunit_actions[0]


    def evaluate_settler_actions(self, game, settler):      # arvioi settlerin päätökset
        for action in self.settler_actions:
            action.evaluate(game, settler)
        self.settler_actions.sort(key=lambda x: x.priority, reverse=True)
        self.current_action = self.settler_actions[0]


    def evaluate_city_actions(self, game, city):            # arvioi kaupunkien päätökset
        for action in self.city_actions:
            action.evaluate(game, city)
        self.city_actions.sort(key=lambda x: x.priority, reverse=True)
        self.current_action = self.city_actions[0]

    def execute_action(self):
        self.current_action.execute()




class Action:

    def __init__(self):
        self.priority = None


    def evaluate(self, game, unit):       # määritellään alaluokissa
        pass

    def execute(self):
        pass

    def calculate_distance(self, unit1, unit2):                 # laskee unittien etäisyyden
        distance = abs(unit1.coordinates[0] - unit2.coordinates[0]) + abs(unit1.coordinates[1] - unit2.coordinates[1])
        return distance

    def calculate_shortest_distance(self, game, unit):                  # määrittää lyhimmän etäisyyden
        unit_distance = None
        city_distance = None
        closest_unit = None
        closest_city = None
        for enemy_unit in game.player.units_list:
            measurement = self.calculate_distance(unit, enemy_unit)
            if unit_distance == None:
                unit_distance = measurement
                closest_unit = enemy_unit
            elif measurement <= unit_distance:
                unit_distance = measurement
                closest_unit = enemy_unit
        for enemy_city in game.player.cities_list:
            measurement2 = self.calculate_distance(unit, enemy_city)
            if city_distance == None:
                city_distance = measurement2
                closest_city = enemy_city
            elif measurement2 <= city_distance:
                city_distance = measurement2
                closest_city = enemy_city
        return unit_distance, city_distance, closest_unit, closest_city

    def calculate_shortest_distance_to_own_city(self, game, unit):          # laskee lyhimmän etäisyyden
        city_distance = None
        closest_city = None
        for city in game.AI.cities_list:
            measurement2 = self.calculate_distance(unit, city)
            if city_distance == None:
                city_distance = measurement2
                closest_city = city
            elif measurement2 <= city_distance:
                city_distance = measurement2
                closest_city = city

        return city_distance, closest_city





    def calculate_moving_direction2(self, unit1, unit2):                     # erittäin suuri erittäin epäselkeä pathfinding koodi, tein itse koska halusin, varmasti selvempiä ratkaisuja löytyy
                                                                             # hahmo liikkuu siis ensisijaisesti siihen suuntaan missä sillä on pidempi matka vihollista kohti
        map = unit1.player.game.map
        tiles_list = []
        if abs(unit1.coordinates[0] - unit2.coordinates[0]) >= abs(unit1.coordinates[1] - unit2.coordinates[1]):
            if unit1.coordinates[0] - unit2.coordinates[0] <= 0:
                tiles_list.append(map.get_tile(unit1.coordinates[0] + 1,unit1.coordinates[1]))
                if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
            else:
                tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
        else:
            if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                tiles_list.append(map.get_tile(unit1.coordinates[0],unit1.coordinates[1] + 1))
                if unit1.coordinates[0] - unit2.coordinates[0] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
            else:
                tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))

        for tile in tiles_list:
            if tile:
                move = unit1.move_to(tile)
            else:
                move = False
            if move:
                return True
            else:
                diagonal_tiles = [map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1] - 1),map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1] + 1), map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]-1),map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]+1)]
                for tiles in diagonal_tiles:
                    if tiles:
                        move = unit1.move_to(tiles)
                    else:
                        move = False
                    if move:
                        return True


    def calculate_fleeing_direction(self, unit1, unit2):                # sama kuin ylempi metodi paitsi, että tiles list käännetään ympäri
        map = unit1.player.game.map
        tiles_list = []
        if abs(unit1.coordinates[0] - unit2.coordinates[0]) >= abs(unit1.coordinates[1] - unit2.coordinates[1]):
            if unit1.coordinates[0] - unit2.coordinates[0] <= 0:
                tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
            else:
                tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
        else:
            if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                if unit1.coordinates[0] - unit2.coordinates[0] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
            else:
                tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] - 1))
                if unit1.coordinates[1] - unit2.coordinates[1] <= 0:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))
                else:
                    tiles_list.append(map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]))
                    tiles_list.append(map.get_tile(unit1.coordinates[0], unit1.coordinates[1] + 1))

        tiles_list.reverse()
        x = random.randint(1,5)
        if x == 5:
            random.shuffle(tiles_list)
        for tile in tiles_list:
            if tile:
                move = unit1.move_to(tile)
            else:
                move = False
            if move:
                return True
            else:
                diagonal_tiles = [map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1] - 1),map.get_tile(unit1.coordinates[0] - 1, unit1.coordinates[1] + 1), map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]-1),map.get_tile(unit1.coordinates[0] + 1, unit1.coordinates[1]+1)]
                for tiles in diagonal_tiles:
                    if tiles:
                        move = unit1.move_to(tiles)
                    else:
                        move = False
                    if move:
                        return True





class MoveToUnits(Action):

    def __init__(self):
        super().__init__()


    def evaluate(self, game, unit):
        self.unit = unit
        distance = self.calculate_shortest_distance(game, unit)
        unit_distance = distance[0]
        city_distance = distance[1]
        self.closest_unit = distance[2]

        if unit_distance == None:
            self.priority = 0
        elif unit_distance > unit.range:
            self.priority = 100
        else:
            self.priority = 0


    def execute(self):

        for i in range(self.unit.speed):
            self.calculate_moving_direction2(self.unit, self.closest_unit)


class MoveToCity(Action):

    def __init__(self):
        super().__init__()


    def evaluate(self, game, unit):
        distance = self.calculate_shortest_distance(game, unit)
        unit_distance = distance[0]
        city_distance = distance[1]
        self.unit = unit
        self.closest_city = distance[3]
        if city_distance == None:
            self.priority = 0
        elif city_distance > unit.range:
            self.priority = 99
        else:
            self.priority = 0

    def execute(self):
        for i in range(self.unit.speed):
            self.calculate_moving_direction2(self.unit, self.closest_city)






class AttackUnits(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, unit):
        self.unit = unit
        distance = self.calculate_shortest_distance(game, unit)
        unit_distance = distance[0]
        city_distance = distance[1]
        self.closest_unit = distance[2]
        if unit_distance == None:
            self.priority = 0
        elif unit_distance <= unit.range:
            self.priority = 125
        else:
            self.priority = 0

    def execute(self):
        if self.unit != None and self.closest_unit != None:
            self.unit.attack(self.closest_unit)


class AttackCity(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, unit):
        distance = self.calculate_shortest_distance(game, unit)
        unit_distance = distance[0]
        city_distance = distance[1]
        self.unit = unit
        self.closest_city = distance[3]
        if city_distance == None:
            self.priority = 0
        elif city_distance <= unit.range:
            self.priority = 110
        else:
            self.priority = 0


    def execute(self):
        if self.unit != None and self.closest_city != None:
            self.unit.attack_city(self.closest_city)

class Settle(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, unit):
        distance = self.calculate_shortest_distance_to_own_city(game,unit)[0]
        self.settler = unit

        if distance != None:
            self.priority = distance * 15
        else:
            self.priority = 101



    def execute(self):
        self.settler.build_city()
        self.settler.player.game.gui.add_city_items()
        self.settler.player.game.gui.update_city_positions()


class MoveToSettle(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, unit):
        self.settler = unit
        self.closest_city = self.calculate_shortest_distance_to_own_city(game, unit)[1]
        self.priority = 100

    def execute(self):
        for i in range(self.settler.speed):
            self.calculate_fleeing_direction(self.settler, self.closest_city)







class BuildSettler(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, city):
        self.city = city
        self.game = game
        money = self.city.player.money
        if money < 5:
            self.priority = 0
        if money >= 5:
            priority = 20
            if len(game.player.cities_list) >= len(game.AI.cities_list):
                priority += 50 * len(game.player.cities_list) - len(game.AI.cities_list)


            for unit in game.AI.units_list:
                if unit.type == 'se':
                    priority += -19

            self.priority = priority



    def execute(self):
        self.game.build_unit('se', self.city)
        self.game.gui.add_unit_items()



class BuildSwordsman(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, city):
        self.city = city
        self.game = game
        money = self.city.player.money
        if money < 2:
            self.priority = 0
        if money >= 2:
            priority = 0
            if len(game.player.units_list) >= len(game.AI.units_list):
                priority += 20 * len(game.player.units_list) - len(game.AI.units_list)

            if len(game.player.cities_list) >= len(game.AI.cities_list):
                priority += -10 * len(game.player.cities_list) - len(game.AI.cities_list)

            for unit in game.AI.units_list:
                if unit.type == 'sw':
                    priority += -10

            self.priority = priority

    def execute(self):
        self.game.build_unit('sw', self.city)
        self.game.gui.add_unit_items()

class BuildArcher(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, city):
        self.city = city
        self.game = game
        money = self.city.player.money
        if money < 2:
            self.priority = 0
        if money >= 2:
            priority = 0
            if len(game.player.units_list) >= len(game.AI.units_list):
                priority += 20 * len(game.player.units_list) - len(game.AI.units_list)

            if len(game.player.cities_list) >= len(game.AI.cities_list):
                priority += -10 * len(game.player.cities_list) - len(game.AI.cities_list)

            for unit in game.AI.units_list:
                if unit.type == 'ar':
                    priority += -10

            self.priority = priority

    def execute(self):
        self.game.build_unit('ar', self.city)
        self.game.gui.add_unit_items()

class BuildKnight(Action):

    def __init__(self):
        super().__init__()

    def evaluate(self, game, city):
        self.city = city
        self.game = game
        money = self.city.player.money
        if money < 3:
            self.priority = 0
        if money >= 3:
            priority = 0
            if len(game.player.units_list) >= len(game.AI.units_list):
                priority += 20 * len(game.player.units_list) - len(game.AI.units_list)

            if len(game.player.cities_list) >= len(game.AI.cities_list):
                priority += -10 * len(game.player.cities_list) - len(game.AI.cities_list)

            for unit in game.AI.units_list:
                if unit.type == 'sw':
                    priority += -10

            self.priority = priority

    def execute(self):
        self.game.build_unit('kn', self.city)
        self.game.gui.add_unit_items()


class DoNothing(Action):
    def __init__(self):
        super().__init__()
        self.priority = 1
