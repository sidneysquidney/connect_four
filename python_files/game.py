import numpy as np

from grid import Grid, Piece, PDICT
from player import Player, Human, RandomAI, MiniMax1AI, MiniMax0AI, MiniMax2AI, MiniMax3AI, MiniMax4AI, MiniMax5AI, MiniMax6AI, MediumAI, HardAI
    
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
        print(' 0 1 2 3 4 5 6 ')
        
    def print_winner(self, colour: Piece):
        if colour == Piece.RED:
            print('You win!')
        elif colour == Piece.YELLOW:
            print('You lose :(')
        else:
            print('Draw')
            
            
    def play(self):
        # plays the game with 2 players until the game has ended - win/draw
        while True:
            self.print_grid()
            state = self.current_player.make_move(self.grid)
            if state.is_ended:
                self.print_grid()
                self.print_winner(state.winner)
                # print(state.winner, 'is the winner!')
                return state.winner
            self.change_player()
       
class UIGame(Game): 
    def valid_move(self, move: int) -> bool:
        return move in self.grid.valid_moves()
    
    def make_move(self, move: int):
        self.grid.make_move(self.p1.token, move)
    
    def get_player_win_state(self):
        return self.grid.get_win_state(self.p1.token)
    
    def get_ai_win_state(self):
        # returns winstate
        return self.grid.get_win_state(self.p2.token)
    
    def ai_move(self):
        self.p2.make_move(self.grid)
    
    def last_move(self):
        return str(self.grid.last_move.r) + str(self.grid.last_move.c)
    
    

# class_dict = {0: MiniMax0AI, 1: MiniMax1AI, 2: MiniMax2AI, 3: MiniMax3AI, 4: MiniMax4AI, 5: MiniMax5AI, 6: MiniMax6AI}
# score_dict = {n: [] for n in range(7)}
# players = [1,2,3,4,5,6]


# for p1 in players:
#     for p2 in players:
#         game = Game(class_dict[p1](Piece.RED), class_dict[p2](Piece.YELLOW))
#         result = game.play()
#         score_dict[p1].append(PDICT[result].score)
#         score_dict[p2].append(-PDICT[result].score)
        
# print(score_dict)
levels = {'e': RandomAI, 'm': MediumAI, 'h': HardAI}
# results = {0: [1, 1, -1, -1, -1, -1, -1], 1: [1, 0, -1, 0, -1, -1, -1], 2: [1, -1, 0, 1, -1, 1, 1], 3: [1, 0, 0, 1, 1, -1, 1], 4: [-1, 0, 1, 0, 1, -1, -1], 5: [1, 1, 1, 0, 0, 0, 0], 6: [1, 0, 1, 1, 1, 1, 0]} 
if __name__ == '__main__':
    while True:
        level = input('(e)asy, (m)edium, or (h)ard?')
        if level in levels.keys():
            game = Game(Human(Piece.RED), levels[level](Piece.YELLOW))
            game.play()
            break
        else:
            print('input e for easy, m for medium, or h for hard')
 