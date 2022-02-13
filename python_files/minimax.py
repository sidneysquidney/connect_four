import numpy as np
from enum import Enum
from collections import namedtuple
import math
from typing import List

from grid import Grid, Piece, Point, PDICT, GRIDREF, WinState, print_grid

WinState = namedtuple('WinState', ['is_ended', 'winner'])
Point = namedtuple('Point', ['r', 'c'])
ColScore = namedtuple('Colscore', ['c', 'score'])
PlayerState = namedtuple('PlayerState', ['minmax', 'score', 'print'])

class GridChild(Grid): 
    # update grid, declare if winner, score func, get valid inputs - make children
    def __init__(self, 
                 grid: np.ndarray, 
                 space: np.ndarray, 
                 parent: Grid, 
                 current_player: Piece, 
                 column: int): 
        self.grid = grid
        self.space = space
        self.last_move = Point(0, 0)
        self.parent = parent
        self.current_player = current_player
        self.win_state = self.update(self.current_player, column)
        self.children = {}
        
    def change_player(self):
        return Piece.RED if self.current_player == Piece.YELLOW else Piece.YELLOW
    
    def update(self, player: Piece, column: int) -> WinState:
        if column != None:
            return super().update(player, column)
        else:
            return WinState(False, Piece.EMPTY)
        
    def get_win_state_score(self, player: Piece) -> WinState:
        state = super().get_win_state(player)
        if state.winner != Piece.EMPTY:
            return PDICT[state.winner].score * math.inf
        return 0
        
    def score(self):
    # score function that says how many lines are active and can be filled to win
        if self.win_state.is_ended:
            return ColScore(self.last_move.c, self.get_win_state_score(self.current_player))
        lsts = GRIDREF.get_lines(self.grid)
        score = 0
        for lst in lsts:
            sub_list = [lst[i: i + 4] for i in range(len(lst) - 3)]
            lst_score = set()
            for sub in sub_list:
                four_score = set()
                for n in sub:
                    four_score.add(PDICT[n].score)
                lst_score.add(sum(four_score))
            score += sum(lst_score)
        return ColScore(self.last_move.c, score)

    def make_children(self):
    # the children are the possible moves from the current grid. The depth is how many times this iterates.
        for col in self.valid_moves():
            self.children[col] = GridChild(self.grid.copy(), 
                                            self.space.copy(), 
                                            self, 
                                            self.current_player, 
                                            col)
            
    def print_grid(self):
        # flips grid upside down and prints grid
        print()
        for line in np.flipud(self.grid):
            print('|' + ' '.join([PDICT[p].print for p in line]) + '|')

        
class MiniMax:
    def __init__(self, grid: Grid, current_player: Piece, depth_limit: int):
        self.current_player = current_player
        self.grid = grid
        self.depth_limit = depth_limit
        self.tree = self.create_tree()
        
    def create_tree(self):
        return GridChild(self.grid.grid.copy(), 
                         self.grid.space.copy(), 
                         None, 
                         self.current_player, 
                         None)
        
    def minimax_move(self):
        return self.minimax(self.tree, self.depth_limit, self.current_player).c

    def minimax(self, current_node: GridChild, depth: int, player: Piece):
        if current_node.win_state.is_ended or depth == 0:
            # print(current_node.score())
            # current_node.print_grid()
            return current_node.score()
        elif PDICT[player].max:
            max_eval = ColScore(None, -math.inf)
            current_node.make_children()
            for child in current_node.children:
                eval = self.minimax(current_node.children[child], depth - 1, current_node.change_player())
                if eval.score >= max_eval.score:
                    max_eval = ColScore(child, eval.score)
            return max_eval
        else:
            min_eval = ColScore(None, math.inf)
            current_node.make_children()
            for child in current_node.children:
                eval = self.minimax(current_node.children[child], depth - 1, current_node.change_player())
                if eval.score <= min_eval.score:
                    min_eval = ColScore(child, eval.score)
            return min_eval
                
# |_ _ _ ◯ _ _ _|
# |_ _ _ ⚈ _ _ _|
# |_ _ _ ◯ _ _ _|
# |_ _ _ ⚈ _ ⚈ ⚈|
# |_ _ _ ◯ _ ◯ ◯|
# |_ _ _ ⚈ ◯ ⚈ ⚈|

g2 = Grid()  

g2.grid[:, 3] = Piece.YELLOW
g2.grid[0, :] = Piece.RED
g2.grid[2, :] = Piece.RED
g2.grid[1, :] = Piece.YELLOW
g2.grid[:, :3] = Piece.EMPTY
g2.grid[1:, 4] = Piece.EMPTY
g2.grid[0, 4] = Piece.YELLOW
g2.grid[4, 3] = Piece.RED
g2.space = np.array([0,0,0,6,1,3,3])



# print_grid(g2.grid)
            
# g1 = Grid()
# m = MiniMax(g2, Piece.RED, 4)

# print(m.minimax_move())

# minimax doesn't do winning move - should do