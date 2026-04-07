
import random
from data import users, courses

class CourseEnv:

    def reset(self):
        self.user = random.choice(users)
        return (self.user["interest"], self.user["level"])

    def step(self, action):
        course = next(c for c in courses if c["id"] == action)

        reward = 0

        if course["category"] == self.user["interest"]:
            reward += 10
        else:
            reward -= 5

        if course["level"] == self.user["level"]:
            reward += 5

        next_state = self.reset()
        return next_state, reward
