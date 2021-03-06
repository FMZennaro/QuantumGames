# Code after: https://colab.research.google.com/drive/1KoAQ1C_BNtGV3sVvZCnNZaER9rstmy0s#scrollTo=ygl_gVmV_QP7

import numpy as np

def evaluate_model(model, env, num_steps=1000):
    episode_rewards = [0.0]
    obs = env.reset()
    for i in range(num_steps):
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        episode_rewards[-1] += reward[0]
        if done[0]:
            obs = env.reset()
            episode_rewards.append(0.0)
    
    mean_reward = round(np.mean(episode_rewards), 3)    
    return mean_reward, len(episode_rewards)-1

def evaluate_random(env, num_steps=1000):
    episode_rewards = [0.0]
    obs = env.reset()
    for i in range(num_steps):
        obs, reward, done, _ = env.step(env.action_space.sample())
        episode_rewards[-1] += reward
        if done:
            obs = env.reset()
            episode_rewards.append(0.0)
    
    mean_reward = round(np.mean(episode_rewards), 3)
    return mean_reward, len(episode_rewards)-1

def evaluate_biased(env, num_steps=1000):
    episode_rewards = [0.0]
    obs = env.reset()
    for i in range(num_steps):
        obs, reward, done, _ = env.step(0)
        episode_rewards[-1] += reward
        if done:
            obs = env.reset()
            episode_rewards.append(0.0)
    
    mean_reward = round(np.mean(episode_rewards), 3)
    return mean_reward, len(episode_rewards)-1