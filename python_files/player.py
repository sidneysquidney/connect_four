import numpy as np
import random

from grid import Grid, GridRef, Piece, ListFlatten, WinState, Point, get_lines, get_lines_from_position

class Player:
    # player class that parents Human and AI
    def __init__(self, token: Piece):
        self.token = token
        
class Human(Player):
    # human class that asks for user input of valid moves (0-6), then updates the board
    def make_move(self, grid: Grid):
        valid_moves = grid.valid_moves()
        while True:
            move = input(f'Make a move within {valid_moves}')
            if move.isdigit() and int(move) in valid_moves:
                return grid.update(self.token, int(move))
            
class AI(Player):
    
    def score1(self, grid):
    # scores lines in play 
        lines = ListFlatten(get_lines(grid)).result
        score = 0
        for line in lines:
            pass
            
            
        

class RandomAI(AI):
    # random ai that makes a random move out of the available valid moves
    def make_move(self, grid):
        valid_moves = grid.valid_moves()
        move = random.choice(valid_moves)
        return grid.update(self.token, move)
    
class SidsAI(AI):
    # sids original AI
    def make_move(self, grid):
        pass

# GridChild class - carries over grid, space, last move, level, 