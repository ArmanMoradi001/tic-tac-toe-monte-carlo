

class TicTacToeEnv:

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [0] * 9
        self.current_player = 1  # 1 = X , -1 = O
        return self.get_state()
    
    def get_state(self):
        return tuple(self.board)
    
    def available_actions(self):
        return [i for i in range(9) if self.board[i]==0]
    
    def step(self, action):
        self.board[action]= self.current_player

        winner = self.check_winner()
        done = False
        reward = 0

        if winner == 1:
            reward = 1
            done = True
        elif winner == -1:
            reward = -1
            done = True
        elif len(self.available_actions())== 0:
            reward = 0
            done = True

        self.current_player *= -1
        return self.get_state(), reward, done
    
    def check_winner(self):
        wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
            ]
        
        for a,b,c in wins:
            if self.board[a]== self.board[b]== self.board[c]:
                return self.board[a]
            
        return None