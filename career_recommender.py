# career_recommender.py

import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load or create dataset with more careers
data = {
    "maths": [8, 5, 9, 4, 6, 7, 3, 6, 7, 6, 4, 5],
    "logic": [9, 6, 8, 5, 7, 5, 4, 7, 9, 8, 6, 5],
    "creativity": [6, 9, 5, 7, 4, 6, 9, 8, 5, 7, 8, 6],
    "programming": [9, 7, 9, 6, 5, 8, 4, 6, 8, 9, 5, 6],
    "communication": [7, 8, 6, 7, 9, 5, 8, 7, 8, 6, 9, 7],
    "career": [
        "Data Scientist",
        "UI/UX Designer",
        "Web Developer",
        "Cybersecurity Expert",
        "Cloud Engineer",
        "AI/ML Engineer",
        "Graphic Designer",
        "Android Developer",
        "Software Tester",
        "Product Manager",
        "Content Creator",
        "DevOps Engineer"
    ]
}
df = pd.DataFrame(data)

X = df.drop("career", axis=1)
y = df["career"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Streamlit UI (simple and clear interface)
st.set_page_config(page_title="Career Path Recommender", layout="centered")
st.markdown("""
    <style>
        .reportview-container {
            background-color: #f9f9f9;
            color: #333333;
        }
        .stSlider > div > div > div > div {
            background: #e0e0e0;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("\U0001F4BB AI Career Path Recommender")
st.subheader("Answer a few quick questions and discover your ideal tech career!")

maths = st.slider("Maths Skill", 0, 10, 5)
logic = st.slider("Logical Thinking", 0, 10, 5)
creativity = st.slider("Creativity", 0, 10, 5)
programming = st.slider("Programming Skills", 0, 10, 5)
communication = st.slider("Communication Skills", 0, 10, 5)

if st.button("\U0001F680 Recommend Career"):
    user_input = np.array([[maths, logic, creativity, programming, communication]])
    prediction = model.predict(user_input)
    st.success(f"\U0001F4C8 Suggested Career Path: **{prediction[0]}**")

    career_info = {
        "Data Scientist": "Analyze data to extract insights using ML and statistics.",
        "UI/UX Designer": "Design user-friendly interfaces and enhance user experience.",
        "Web Developer": "Create and maintain websites and web apps.",
        "Cybersecurity Expert": "Protect systems from cyber threats and breaches.",
        "Cloud Engineer": "Build and manage cloud infrastructure and services.",
        "AI/ML Engineer": "Develop AI algorithms and machine learning models.",
        "Graphic Designer": "Craft engaging graphics and branding visuals.",
        "Android Developer": "Design apps for Android devices using Java/Kotlin.",
        "Software Tester": "Ensure software quality through structured testing.",
        "Product Manager": "Oversee product development from idea to delivery.",
        "Content Creator": "Produce digital content like blogs, videos, and more.",
        "DevOps Engineer": "Automate and streamline development and operations."
    }
    st.info(career_info.get(prediction[0], "More details coming soon..."))
