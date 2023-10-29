# Filename: n_step_rl_algorithm.py

import numpy as np
import gym

class NStepRLAlgorithm:
    def __init__(self, n, environment, gamma=0.9, alpha=0.1):
        self.n = n
        self.env = gym.make(environment)
        self.num_actions = self.env.action_space.n
        self.num_states = self.env.observation_space.n
        self.q_values = np.zeros((self.num_states, self.num_actions))
        self.gamma = gamma  # discount factor
        self.alpha = alpha  # learning rate

    def select_action(self, state):
        return np.argmax(self.q_values[state])

    def update_q_values(self, states, actions, rewards):
        T = len(states)
        if T < self.n:
            return  # Not enough steps to perform n-step update

        # Calculate n-step return
        n_step_return = sum([self.gamma**(t-i-1) * rewards[t] for i, t in enumerate(range(T))])

        # Update Q-values using n-step return
        state_to_update = states[0]
        action_to_update = actions[0]
        self.q_values[state_to_update, action_to_update] += self.alpha * (n_step_return - self.q_values[state_to_update, action_to_update])

    def train(self, num_episodes):
        for episode in range(num_episodes):
            state = self.env.reset()
            states, actions, rewards = [], [], []
            
            for t in range(self.n):
                action = self.select_action(state)
                next_state, reward, done, _ = self.env.step(action)

                states.append(state)
                actions.append(action)
                rewards.append(reward)

                if done:
                    break

                state = next_state

            self.update_q_values(states, actions, rewards)

    def plot_results(self, num_episodes, title):
        # Placeholder for basic plotting logic
        episodes = np.arange(1, num_episodes + 1)
        rewards = np.random.normal(0, 1, num_episodes)  # Replace with actual rewards
        
        plt.figure(figsize=(10, 6))
        plt.plot(episodes, rewards, label=f'n = {self.n}')
        plt.title(title)
        plt.xlabel('Episodes')
        plt.ylabel('Sum of Rewards')
        plt.legend()
        plt.show()

# Test your implementation on Blackjack environment
if __name__ == "__main__":
    n_step_algo = NStepRLAlgorithm(n=3, environment='Blackjack-v0')
    n_step_algo.train(num_episodes=1000)
