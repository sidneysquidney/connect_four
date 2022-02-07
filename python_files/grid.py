import numpy as np
from enum import Enum
from collections import namedtuple

class Piece(Enum):
    EMPTY = ' '
    RED = 'R'
    YELLOW = 'Y'
    
WinState = namedtuple('WinState', ['is_ended', 'winner'])
Point = namedtuple('Point', ['x', 'y'])

class ListFlatten:
    def __init__(self, group):
        self.result = []
        self.backtrack(group)
        
    def backtrack(self, group):
        if type(group[0]) != list:
            self.result.append(group)
        else:
            for item in group:
                self.backtrack(item)

def get_lines(grid):
    # returns a list of lines (that have a length greater than 4) from the grid - rows, columns, both diagonals
    return [[list(x) for x in grid], 
            [list(grid[:,c]) for c in range(7)], 
            [list(np.diag(grid, x)) for x in range(-2, 4)], 
            [list(np.diag(np.fliplr(grid), x)) for x in range(-2, 4)]]

def get_lines_from_position(x, y, grid):
#   gets the lines from coordinates[x,y]
    l1, l2, l3, l4 = grid_reference.lines_dict[grid_reference.number_grid[x,y]]
    lines = []
    lines.append(grid[l1,:])
    if isinstance(l2, int):
        lines.append(grid[:, l2])
    if isinstance(l3, int):
        lines.append(np.diag(grid, l3))
    if isinstance(l4, int):
        lines.append(np.diag(np.fliplr(grid), l4))
    return lines

class GridRef:
    # a Grid Reference class to locate lines from a specific coordinate
    def __init__(self):
        self.number_grid = np.arange(42).reshape(6,7)
        self.lines_dict = {n: [None] * 4 for n in range(42)}
        self.apply_lines_to_lines_dict()
        
    def apply_lines_to_lines_dict(self):
        groups = get_lines(self.number_grid)
        for i in range(42):
            for r in range(7):
                for ind in range(4):
                    if r == 6:
                        if i in groups[1][r]:
                            self.lines_dict[i][1] = r
                    elif ind < 2:
                        if i in groups[ind][r]:
                            self.lines_dict[i][ind] = r
                    else:
                        if i in groups[ind][r]:
                            self.lines_dict[i][ind] = r - 2
                            
grid_reference = GridRef()

class Grid:
    # main grid class
    def __init__(self): 
        self.grid = np.full((6,7), Piece.EMPTY, dtype = Piece)
        self.space = np.zeros(7, dtype = int)
        self.last_move = Point(0,0)
        
    def valid_moves(self):
    # returns an array of indexes that have space
        return np.nonzero(self.space < 6)[0]

    def make_move(self, player: Piece, column):
    # inputs the player counter into the next available space in the column
        if self.space[column] == 6:
            raise ValueError(f'Column {column} is full')
        else:
            self.grid[self.space[column], column] = player
            self.last_move = Point(self.space[column], column)
            self.space[column] += 1
            
    def update(self, player, column):
    # makes a move in col, then returns the WinState tuple
        self.make_move(player, column)
        return self.get_win_state(player)
    
    def get_winner(self, player: Piece):
    # searches through the lines at the coordinates of the last move. if 4 in a row found returns True
        lines = get_lines_from_position(self.last_move.x, self.last_move.y, self.grid)
        for line in lines:
            count = 1
            for i in range(1, len(line)):
                if line[i] == line[i - 1]:
                    count += 1
                else:
                    count = 1
                if count == 4:
                    if line[i] == player:
                        return True
        return False
        
    # def get_winner(self, player: Piece):
    # # searches through the lines at the coordinates of the last move. if 4 in a row found returns True
    #     lines = get_lines_from_position(self.last_move.x, self.last_move.y, self.grid)
    #     for line in lines:
    #         sub_lines = [line[x - 4: x] for x in range(4, len(line) + 1)]
    #         for sub in sub_lines:
    #             if sum(sub == player) == 4:
    #                 return True
    #     return False
    
    def get_win_state(self, player):
        # returns a WinState tuple [0] is a bool telling 'is_ended', [1] tells the winner/ empty
        if self.get_winner(player):
            return WinState(True, player)
        elif not any(self.valid_moves()):
            return WinState(True, Piece.EMPTY)
        else:
            return WinState(False, Piece.EMPTY)