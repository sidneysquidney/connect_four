import numpy as np

from grid import Grid, GridRef, Piece, WinState, Point, get_lines, get_lines_from_position

# from game import TestGrid

g1 = Grid()
g2 = Grid()
g3 = Grid()
g4 = Grid()
g5 = Grid()
g = 'sid'

# g2.grid[:, 0] = Piece.RED
for x in range(6):
    g2.make_move(Piece.RED, 0)
    
for x in range(3):
    g3.make_move(Piece.YELLOW, x)
    
for x in range(7):
    for y in range(6):
        g4.make_move(Piece.RED, x)
        
for x in range(3):
    g5.make_move(Piece.RED, 3)
    g5.make_move(Piece.YELLOW, 3)
# print(g2.grid)

# t1 = TestGrid()
# t1.grid = g5.grid

# t1.print_grid()

# print(g2.valid_moves())
char = {
        Piece.RED : '⚈',
        Piece.YELLOW : '◯',
        Piece.EMPTY : '_'
    }
def print_grid(grid):
    for line in np.flipud(grid):
        print('|' + ' '.join([char[p] for p in line]) + '|')
        
print_grid(g5.grid)