import random
from collections import defaultdict
import pickle


class MonteCarloAgent:
    def __init__(self, epsilon=1.0, epsilon_min=0.05, epsilon_decay=0.999):
        self.Q = defaultdict(float)
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

    def choose_action(self, state, actions):
        if random.random()< self.epsilon:
            return random.choice(actions)
        qs = [self.Q[(state,a)] for a in actions]
        max_q = max(qs)

        best_actions = [a for a in actions if self.Q[(state, a)] == max_q]
        return random.choice(best_actions)

    def update_Q(self, episode, reward, alpha = 0.1):
        visited = set()

        for state, action in episode:
            if (state, action) not in visited:
                self.Q[(state,action)] += (reward - self.Q[(state, action)]) * alpha
                visited.add((state, action))

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def save(self, path="q_table.pkl"):
        with open(path, "wb") as f:
            pickle.dump(dict(self.Q), f)

    def load(self, path="q_table.pkl"):
        with open(path, "rb") as f:
            self.Q = defaultdict(float, pickle.load(f))
