# Tic-Tac-Toe Monte Carlo Reinforcement Learning Agent

A self-playing Monte Carlo agent that learns to play perfect (or near-perfect) Tic-Tac-Toe through thousands of random games.

The agent uses **first-visit Monte Carlo control** with ε-greedy exploration and learns a Q-value table for state-action pairs.

After training, it plays very strongly — usually drawing or winning against human players when both play optimally.

https://github.com/ArmanMoradi001/tic-tac-toe-monte-carlo

## Features

- Classic 3×3 Tic-Tac-Toe environment
- Monte Carlo on-policy learning (first-visit)
- ε-greedy exploration with exponential decay
- Saves and loads learned Q-table (`q_table.pkl`)
- Human vs agent gameplay mode (you play as O)

## Project Structure
tic-tac-toe-monte-carlo/
├── env.py          # Game rules, board, win checking, step function
├── agent.py        # MonteCarloAgent – choose_action, update_Q, save/load
├── train.py        # Self-play training loop (500,000 episodes by default)
├── play.py         # Human vs trained agent interactive game
├── q_table.pkl     # Trained Q-values (after running train.py)
└── README.md

## Requirements

Python 3.8+
numpy          # (optional – only if you later vectorize)
pickle         # standard library
random         # standard library
collections    # standard library
No external packages are strictly required.
## Installation

Clone the repository
```bash
git clone https://github.com/ArmanMoradi001/tic-tac-toe-monte-carlo.git
cd tic-tac-toe-monte-carlo
```

(Optional) Create virtual environment

python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
Usage
1. Train the agent
   python train.py

Default: 500,000 episodes
Progress printed every 50,000 episodes
Saves q_table.pkl when finished

You can change the number of episodes by editing train() call:
Pythontrained_agent = train(episodes=1_000_000)
2. Play against the trained agent
Bashpython play.py

You play as O (second player)
Agent plays as X (first player)
Enter numbers 0–8 to place your mark

3. Quick test: agent vs agent (self-play evaluation)
You can add this snippet to a new file or run in Jupyter/Colab:
Pythonfrom env import TicTacToeEnv
from agent import MonteCarloAgent

agent = MonteCarloAgent(epsilon=0)
agent.load("q_table.pkl")

wins_x = wins_o = draws = 0
for _ in range(1000):
    env = TicTacToeEnv()
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state, env.available_actions())
        state, reward, done = env.step(action)
    if reward == 1:   wins_x += 1
    elif reward == -1: wins_o += 1
    else:             draws += 1

print(f"X: {wins_x}  |  O: {wins_o}  |  Draws: {draws}")
Results (after 500k episodes)

Very high draw rate in self-play
Agent rarely loses when going second
Strong performance against humans — beats most casual players

Known Limitations / Possible Improvements

Pure Monte Carlo → high variance (especially early in learning)
Single agent plays both sides (symmetric learning)
Tuple state representation → slow for very large episode counts
No discounting / no TD backup

Future ideas:

Use TD(λ) or SARSA / Q-learning
Separate agents for X and O
Ternary state encoding (0–19682) for faster lookups
Add alpha decay / better exploration schedule

License
MIT License
Feel free to use, modify, and share.
Happy gaming & learning!
Arman Moradi – 2026
