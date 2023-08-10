
import unittest
from main import grid_generator, place_random_bombe


class TestGridGenerator(unittest.TestCase):
    def test_grid_ok(self):
        columns = 5
        lines = 10
        result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(grid_generator(columns, lines, 0), result)

    def test_grid_no(self):
        columns = 5
        lines = 10
        inexact_grid = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.assertNotEqual(grid_generator(columns, lines, 0), inexact_grid)

    def test_nb_lc(self):
        columns = 5
        lines = 10
        result = grid_generator(columns, lines, 0)
        self.assertEqual(len(result), lines)
        self.assertEqual(len(result[0]), columns)

    def test_grid_neg_nb(self):
        columns = -5
        lines = 10
        result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertEqual(grid_generator(columns, lines, 0), result)

    def test_bomb_grid(self):
        columns = 5
        lines = 10
        grid = grid_generator(columns, lines, "Z")
        place_random_bombe(1, columns, lines)






