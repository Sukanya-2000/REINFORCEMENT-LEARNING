# Reinforcement Learning Project

## Overview
This project focuses on implementing and evaluating an n-step RL control algorithm that encompasses various algorithms from one-step TD to Monte Carlo. The algorithm is applied to different environments, including Blackjack, Taxi, Cliff Walking, and Frozen Lake.

## Implementation (n_step_rl_algorithm.py)
The core of the implementation resides in `n_step_rl_algorithm.py`. The file contains a class named `NStepRLAlgorithm`, which encapsulates the n-step RL control algorithm. Hyperparameters such as the discount factor, learning rate, and n-step value can be adjusted for experimentation.

## Task I - Algorithm Implementation
The n-step RL algorithm implemented in `NStepRLAlgorithm` is a flexible approach that unifies one-step TD to Monte Carlo. By adjusting the n-step value, the algorithm seamlessly transitions between different methods. The script includes a training loop that iterates through episodes, updating Q-values based on the observed rewards.

## Task II - Evaluations (evaluate_algorithm.py)
To assess the algorithm's performance, the `evaluate_algorithm.py` script is employed. This script iterates over different environments, varying the n-step value. Plots illustrating value functions, policies, and the sum of rewards over episodes are generated for visual analysis.

### Running the Evaluation
Execute the following command in the terminal:

```bash
python evaluate_algorithm.py
```

## Task III - Report Generation (generate_report.py)
The `generate_report.py` script creates a Jupyter notebook containing a detailed report for each task. It covers explanations of the environment properties, the parameter selection process, and placeholders for plotting results. Running this script generates a comprehensive report encapsulating the project's insights.

### Running the Report Generator
Execute the following command in the terminal:

```bash
python generate_report.py
```

## Task IV - Demo
For the demo session scheduled for October 31, 2023, showcase the optimal solutions derived from the algorithm. Utilize the n-step RL algorithm to learn optimal policies, tune the algorithm parameters, plot the results, and demonstrate the efficiency of the learned policies.

## Output
The scripts produce insightful plots showcasing the evolution of value functions, policies, and the sum of rewards across episodes for each environment. The Jupyter notebook (`Task III - Report`) provides in-depth explanations and visualizations, offering a clear understanding of the project's outcomes.

**Note:** Ensure you have Python 3 installed, along with the required dependencies (numpy, gym, matplotlib), before running the scripts.
