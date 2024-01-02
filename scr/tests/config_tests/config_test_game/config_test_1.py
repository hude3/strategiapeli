import unittest
from scr.game.game import Game
from scr.game.game_errors import CorruptedConfigureFileError


class TestConfig1(unittest.TestCase):       # testaa että heittääkö configurointi erroria kun ai color puuttuu


    def test_game_options(self):

        check = False
        try:
            game = Game()
        except CorruptedConfigureFileError:
            check = True

        self.assertTrue(check)


if __name__ == '__main__':
    unittest.main()