import numpy as np
import unittest

from grid import Grid, GridRef, Piece, WinState, Point, get_lines, get_lines_from_position
from test_variables import g1, g2, g3, g4, g5, g

class TestGrid(unittest.TestCase):
    def test_start(self):
    # grid init
        self.assertEqual(g, 'sid')
        self.assertEqual(type(g1.grid[0,0]), Piece)
        self.assertEqual(g1.grid[0,0].value, ' ')
        self.assertEqual(g1.grid.shape, (6,7))
        self.assertEqual(len(g1.space), 7)
        self.assertEqual(g1.space[0], 0)
        self.assertEqual(g1.last_move, (0,0))
        self.assertEqual(type(g1.last_move), Point)
        
    def test_functions(self):
    # valid_moves, make_move, update, get_winner, get_win_state
        self.assertEqual(g2.last_move, (5, 0))
        self.assertTrue(g2.space[0])
        self.assertNotIn(0, g2.valid_moves())
        self.assertIn(1, g2.valid_moves())
        self.assertEqual(g2.update(Piece.RED, 1), (False, Piece.EMPTY))
        self.assertEqual(g2.grid[0, 1], Piece.RED)
        self.assertEqual(g3.update(Piece.YELLOW, 3), (True, Piece.YELLOW))
        self.assertEqual(g3.last_move, (0, 3))
        self.assertTrue(g3.get_winner(Piece.YELLOW))
        self.assertFalse(g3.get_winner(Piece.RED))
        self.assertEqual(g4.get_win_state(Piece.YELLOW), (True, Piece.EMPTY))
        self.assertRaises(ValueError, g2.make_move, Piece.YELLOW, 0)
        self.assertFalse(g5.get_winner(Piece.RED))
        self.assertFalse(g5.get_winner(Piece.YELLOW))
        
unittest.main()