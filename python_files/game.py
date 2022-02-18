import numpy as np

from grid import Grid, Piece, PDICT
from player import Player, Human, RandomAI, MiniMax1AI, MiniMax0AI, MiniMax2AI, MiniMax3AI, MiniMax4AI, MiniMax5AI, MiniMax6AI, EasyAI, MediumAI, HardAI

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
            

class_dict = {0: MiniMax0AI, 1: MiniMax1AI, 2: MiniMax2AI, 3: MiniMax3AI, 4: MiniMax4AI, 5: MiniMax5AI, 6: MiniMax6AI}
score_dict = {n: [] for n in range(7)}
players = [1,2]


# for p1 in players:
#     for p2 in players:
#         game = Game(class_dict[p1](Piece.RED), class_dict[p2](Piece.YELLOW))
#         result = game.play()
#         score_dict[p1].append(PDICT[result].score)
#         score_dict[p2].append(-PDICT[result].score)
        
# print(score_dict)
       
# results = {0: [1, 1, -1, -1, -1, -1, -1], 1: [1, 0, -1, 0, -1, -1, -1], 2: [1, -1, 0, 1, -1, 1, 1], 3: [1, 0, 0, 1, 1, -1, 1], 4: [-1, 0, 1, 0, 1, -1, -1], 5: [1, 1, 1, 0, 0, 0, 0], 6: [1, 0, 1, 1, 1, 1, 0]} 

game = Game(Human(Piece.RED), HardAI(Piece.YELLOW))
game.play()
# print(o)
            
# when game gets to end (3 available moves left - and minimax depth == 4, what then...)

# apply some amout of randomness
# make different levels 

# 