from env import TicTacToeEnv
from agent import MonteCarloAgent

def print_board(state):
    symbols = {1: "X", -1: "O", 0: " "}
    b = [symbols[x] for x in state]
    print()
    print(f"{b[0]} | {b[1]} | {b[2]}")
    print("--+---+--")
    print(f"{b[3]} | {b[4]} | {b[5]}")
    print("--+---+--")
    print(f"{b[6]} | {b[7]} | {b[8]}")
    print()

def play():
    env = TicTacToeEnv()
    agent = MonteCarloAgent(epsilon=0)
    agent.load("q_table.pkl")

    state = env.reset()
    done = False

    print("You are O (player -1)")
    print_board(state)

    while not done:
        if env.current_player == 1:
            action = agent.choose_action(state, env.available_actions())
            print(f"Agent plays: {action}")
        else:
            action = int(input("Your move (0-8): "))
            while action not in env.available_actions():
                action = int(input("Invalid move. Try again: "))

        state, reward, done = env.step(action)
        print_board(state)

    if reward == 1:
        print("Agent wins 😎")
    elif reward == -1:
        print("You win 🎉")
    else:
        print("Draw 🤝")


if __name__ == "__main__":
    play()
