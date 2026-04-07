from env import CourseEnv
from agent import Agent
from data import courses

env = CourseEnv()
actions = [c["id"] for c in courses]
agent = Agent(actions)

episodes = 10   # keep small for testing

for ep in range(episodes):
    state = env.reset()
    print("Start State:", state)

    for step in range(5):
        action = agent.choose_action(state)
        next_state, reward = env.step(action)

        print(f"Action: {action}, Reward: {reward}")

        agent.update(state, action, reward, next_state)
        state = next_state

    print(f"Episode {ep} done\n")

print("Training Complete ✅")
print("Q Table:", agent.q_table)
