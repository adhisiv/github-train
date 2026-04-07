# 🎓 AI Course Recommendation System

🚀 A Reinforcement Learning-based system that recommends personalized online courses using an OpenEnv simulation environment.

---

## 📌 Features

- 🤖 Q-Learning Agent
- 🔄 OpenEnv Environment (step, reset, reward)
- 🎯 Personalized Recommendations
- 🖥️ Streamlit Web UI

---

## 🧠 How It Works

- The agent observes user state (interest, level)
- It selects a course (action)
- Receives reward based on match
- Learns optimal recommendations over time

---

## ▶️ How to Run

```bash
python train.py
python -m streamlit run app.py
