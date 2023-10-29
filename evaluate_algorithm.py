# Filename: evaluate_algorithm.py

from n_step_rl_algorithm import NStepRLAlgorithm
import matplotlib.pyplot as plt

def evaluate_algorithm(environment, n_values, num_episodes):
    for n in n_values:
        algo = NStepRLAlgorithm(n=n, environment=environment)
        algo.train(num_episodes=num_episodes)
        # Plot value functions, policy, sum of rewards, etc.
        # Save or display the plots

# Evaluate on different environments
if __name__ == "__main__":
    environments = ['Blackjack-v0', 'Taxi-v3', 'CliffWalking-v0', 'FrozenLake-v1']
    n_values = [1, 2, 3, 4, float('inf')]  # Include infinity for Monte Carlo
    num_episodes = 1000

    for env in environments:
        evaluate_algorithm(environment=env, n_values=n_values, num_episodes=num_episodes)
