import numpy as np

from grid import Grid, Piece
from player import Player, Human, RandomAI, MiniMax1AI, MiniMax0AI

class Game:
    char = {
        Piece.RED : '⚈',
        Piece.YELLOW : '◯',
        Piece.EMPTY : '_'
    }
    
    def __init__(self, player_1: Player, player_2: Player):
        self.grid = Grid()
        self.p1 = player_1
        self.p2 = player_2
        self.current_player = self.p1
        self.next_player = self.p2
        
    def change_player(self):
        # switches current_player and next_player
        self.current_player, self.next_player = self.next_player, self.current_player
        
    def print_grid(self):
        # flips grid upside down and prints grid
        print()
        for line in np.flipud(self.grid.grid):
            print('|' + ' '.join([self.char[p] for p in line]) + '|')
            
    def play(self):
        # plays the game with 2 players until the game has ended - win/draw
        while True:
            self.print_grid()
            # print(self.grid.grid)
            state = self.current_player.make_move(self.grid)
            if state.is_ended:
                self.print_grid()
                print(state.winner)
                return state.winner
            self.change_player()
            
game = Game(MiniMax1AI(Piece.RED), MiniMax0AI(Piece.YELLOW))
game.play()
            
# when game gets to end (3 available moves left - and minimax depth == 4, what then...)