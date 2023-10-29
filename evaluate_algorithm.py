# Filename: evaluate_algorithm.py

import numpy as np
import gym
import matplotlib.pyplot as plt
from n_step_rl_algorithm import NStepRLAlgorithm

# Helper function to plot results
def plot_results(algo, environment, num_episodes, title):
    # Placeholder for plotting logic
    pass

# Evaluate on different environments
if __name__ == "__main__":
    environments = ['Blackjack-v0', 'Taxi-v3', 'CliffWalking-v0', 'FrozenLake-v1']
    n_values = [1, 2, 3, 4, float('inf')]  # Include infinity for Monte Carlo
    num_episodes = 1000

    for env in environments:
        for n in n_values:
            algo = NStepRLAlgorithm(n=n, environment=env)

            # Custom tuning for each environment
            if env == 'Blackjack-v0':
                algo.alpha = 0.01  # Adjust the learning rate for Blackjack
                algo.gamma = 0.9   # Adjust the discount factor for Blackjack
            elif env == 'Taxi-v3':
                algo.alpha = 0.1   # Adjust the learning rate for Taxi
                algo.gamma = 0.95  # Adjust the discount factor for Taxi
            elif env == 'CliffWalking-v0':
                algo.alpha = 0.05  # Adjust the learning rate for Cliff Walking
                algo.gamma = 0.99  # Adjust the discount factor for Cliff Walking
            elif env == 'FrozenLake-v1':
                algo.alpha = 0.02  # Adjust the learning rate for Frozen Lake
                algo.gamma = 0.98  # Adjust the discount factor for Frozen Lake

            algo.train(num_episodes=num_episodes)

            # Placeholder: You may want to customize this based on your specific plotting needs
            plot_results(algo, env, num_episodes, f'{env} - n={n}')
