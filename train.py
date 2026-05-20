from env import TicTacToeEnv
from agent import MonteCarloAgent


def train(episodes = 500_000):
    env = TicTacToeEnv()
    agent = MonteCarloAgent()

    for ep in range(episodes):
        state = env.reset()
        episode = []
        done = False

        while not done:
            actions = env.available_actions()
            action = agent.choose_action(state, actions)

            next_state, reward, done = env.step(action)

            episode.append((state,action))
            state = next_state
        agent.update_Q(episode, reward)

        agent.decay_epsilon()
        
        if ep % 50_000 == 0:
                        print(f"Episode {ep} | epsilon = {agent.epsilon:.3f}")

                        
    agent.save("q_table.pkl")
    print("Training finished & model saved!")
    return agent


if __name__ == "__main__":
    trained_agent = train()