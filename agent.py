import random

class Agent:
    def __init__(self, actions):
        self.q_table = {}
        self.actions = actions
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        qs = [self.get_q(state, a) for a in self.actions]
        return self.actions[qs.index(max(qs))]

    def update(self, state, action, reward, next_state):
        max_q_next = max([self.get_q(next_state, a) for a in self.actions])

        old_q = self.get_q(state, action)

        new_q = old_q + self.alpha * (reward + self.gamma * max_q_next - old_q)

        self.q_table[(state, action)] = new_q
