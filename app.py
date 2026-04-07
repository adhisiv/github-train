import streamlit as st
from env import CourseEnv
from agent import Agent
from data import courses

st.set_page_config(page_title="AI Course Recommender", layout="centered")

st.title("🎓 AI Course Recommendation System")
st.markdown("### 🚀 Powered by Reinforcement Learning")

env = CourseEnv()
actions = [c["id"] for c in courses]
agent = Agent(actions)

state = env.reset()

st.subheader("👤 User Profile")
st.write(f"Interest: {state[0]}")
st.write(f"Level: {state[1]}")

if st.button("🎯 Recommend Course"):
    action = agent.choose_action(state)
    next_state, reward = env.step(action)

    course = next(c for c in courses if c["id"] == action)

    st.success(f"📚 Recommended Course: {course['name']}")
    st.info(f"🎯 Reward Score: {reward}")
    st.subheader("📊 Learning (Q-Table)")
st.write(agent.q_table)
if st.button("🔄 New User"):
    state = env.reset()
