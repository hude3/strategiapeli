import unittest
import random, math
from scr.units.unit import Unit
from scr.units.battleunit import BattleUnit
from scr.units.supportunit import SupportUnit
from scr.tiles.tile import Tile
from scr.tiles.forest import Forest
from scr.tiles.hills import Hills
from scr.game.player import Player
from scr.game.game_errors import CorruptedConfigureFileError, CorruptedSaveFileError
from scr.game.startwindow import StartWindow

from scr.game.game_init import GameInit



class TestUnit(unittest.TestCase):







    def test_dying(self):
        player1 = Player('1', 0)
        tile = Forest(10, 10)
        battleunit = BattleUnit(player1, tile)



        battleunit.die()

        self.assertEqual(tile.unit,None)        # testaa, että onko Tile tyhjä hahmon kuoltua
        self.assertEqual(battleunit.dead, True) # testaa, onko hahmo kuollut
        self.assertFalse(battleunit.die())      # testaa, voiko hahmo kuolla, kun on kuollut


    def test_damage_system(self):       # testaa toimiiko damage systeemi oikein ja kuoleeko hahmo
        player1 = Player('1', 0)
        player2 = Player('2', 0)
        tile1 = Forest(10,10)
        tile2 = Hills(10,11)
        battleunit1 = BattleUnit(player1, tile1)
        battleunit2 = BattleUnit(player2, tile2)
        random_seed = BattleUnit.Seed



        random.seed(random_seed)
        damage = int(30 * math.exp(((battleunit1.combat_strength - (battleunit2.combat_strength * battleunit2.tile.defence_bonus)) / 25)  * (random.randint(75, 125) / 100)))

        self.assertEqual(battleunit1.attack(battleunit2),damage)


        battleunit1.attack(battleunit2)

        battleunit1.attack(battleunit2)

        battleunit1.attack(battleunit2)


        self.assertEqual(tile2.unit, None)  # testaa, että onko Tile tyhjä hahmon kuoltua
        self.assertEqual(battleunit2.dead, True)  # testaa, onko hahmo kuollut
        self.assertFalse(battleunit2.die())  # testaa, voiko hahmo kuolla, kun on kuollut




class TestGameInit(unittest.TestCase):


    def test_header(self):
        file = open('test_save_header.txt', 'r')
        game_init = GameInit()

        game = game_init.load_game(file)

        file.close()

        self.assertFalse(game)

    def test_game_info(self):
        file = open('test_save_game_info.txt', 'r')
        game_init = GameInit()

        game = game_init.load_game(file)

        file.close()

        self.assertFalse(game)

    def test_player_info(self):
        file = open('test_save_player_info.txt', 'r')
        game_init = GameInit()

        game = game_init.load_game(file)

        file.close()

        self.assertFalse(game)









if __name__ == '__main__':
    unittest.main()