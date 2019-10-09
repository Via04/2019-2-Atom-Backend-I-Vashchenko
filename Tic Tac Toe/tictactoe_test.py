import unittest
from tictactoe import Field


class TestTicTacToe(unittest.TestCase):
    def test1(self):
        gamet = Field()
        gamet.make_turn(0, 0)
        gamet.make_turn(0, 1)
        gamet.make_turn(1, 1)
        gamet.make_turn(0, 2)
        gamet.make_turn(2, 2)
        gamet.draw()
        self.assertTrue(gamet.is_end())
        self.assertEqual(gamet.show_winner(), 1)

    def test2(self):
        gamet = Field()
        gamet.make_turn(1, 1)
        gamet.make_turn(0, 0)
        gamet.make_turn(1, 0)
        gamet.make_turn(0, 2)
        gamet.make_turn(1, 2)
        gamet.draw()
        self.assertTrue(gamet.is_end())
        self.assertEqual(gamet.show_winner(), 1)

    def test3(self):
        gamet = Field()
        gamet.make_turn(1, 0)
        gamet.make_turn(1, 1)
        gamet.make_turn(2, 0)
        gamet.make_turn(0, 0)
        gamet.make_turn(2, 1)
        gamet.make_turn(2, 2)
        gamet.draw()
        self.assertTrue(gamet.is_end())
        self.assertEqual(gamet.show_winner(), 2)


if __name__ == '__main__':
    unittest.main()
