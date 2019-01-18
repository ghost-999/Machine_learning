
#https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
#https://gym.openai.com/docs/

import numpy as np
import random
from IPython.display import clear_output


import gym



env = gym.make("Taxi-v2").env


env.reset() # reset environment to a new, random state
env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()


print(env.P[329])


q_table = np.zeros([env.observation_space.n, env.action_space.n])

"""Training the agent"""



# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# For plotting metrics
all_epochs = []
all_penalties = []

for i in range(1, 100001):
    state = env.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False
    
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values

        next_state, reward, done, info = env.step(action) 
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1
        
    if i % 100 == 0:
        clear_output(wait=True)
        print("Episode: %d" %i)

print("Training finished.\n")


"""
0 = south
1 = north
2 = east
3 = west
4 = pickup
5 = dropoff
print("penalty to go in each direction in this state: lesser is better")
print(q_table[329])
"""


"""Evaluate agent's performance after Q-learning"""

total_epochs, total_penalties = 0, 0
episodes = 100

for _ in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0
    
    done = False
    
    while not done:
        
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        epochs += 1

    total_penalties += penalties
    total_epochs += epochs


print("episodes")
print(episodes)
print("average timestep per episode")
k=total_epochs / episodes
print(k)
print("Average penalties per episode")
c=total_penalties / episodes
print(c)
