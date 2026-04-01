import streamlit as st
import random
import pandas as pd
from model import train_model
import os

# Page config
st.set_page_config(page_title="AI Student Wellness Assistant", layout="centered")

# 🎨 CUSTOM CSS (YOUR THEME)
st.markdown("""
    <style>
    body {
        background-color: #222831;
        color: #DFD0B8;
    }
    .stApp {
        background-color: #222831;
    }
    h1, h2, h3 {
        color: #DFD0B8;
    }
    .stButton>button {
        background-color: #DFD0B8;
        color: #222831;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #948979;
        color: white;
    }
    .css-1d391kg, .stSlider, .stSelectbox {
        background-color: #393E46;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = train_model()

# Title
st.title("AI Focus & Mental Wellness Assistant")
st.caption("## Helping students manage study, focus, and mental health")
st.markdown("Built with AI + Python + Streamlit")

st.markdown("---")

# Inputs
st.subheader("Enter Your Daily Habits")

col1, col2 = st.columns(2)

with col1:
    study = st.slider("Study Hours", 0, 10, 2)
    sleep = st.slider("Sleep Hours", 0, 10, 5)

with col2:
    focus = st.slider("Focus Level", 1, 10, 5)
    stress = st.slider("Stress Level", 1, 10, 5)

mood = st.selectbox(" Mood", ["Happy", "Neutral", "Stressed", "Anxious", "Tired"])

st.markdown("---")

# Data
motivation_quotes = [
    "Success comes from discipline.",
    "Keep going even when it's hard.",
    "You are stronger than you think.",
    "I will become a successful AI engineer."
]

study_tips = [
    "Study a little every day.",
    "Consistency beats talent.",
    "Focus now, enjoy later."
]

support_messages = [
    "You are not alone. Take one step at a time.",
    "Progress is progress, no matter how small.",
    "Take care of your mind as much as your goals."
]

# Button
if st.button("Analyze My Status"):

    prediction = model.predict([[study, sleep, focus]])[0]
    prediction = round(prediction)

    st.markdown("##Results")

    st.metric("Predicted Performance", f"{prediction}%")

    # Feedback
    if stress > 7 or mood in ["Stressed", "Anxious"]:
        st.error("You might be experiencing burnout.")
        st.write(random.choice(motivation_quotes))

    elif focus < 4 or mood == "Tired":
        st.warning("Your focus is low.")
        st.write(random.choice(study_tips))

    elif prediction < 60:
        st.error("Performance is low.")
        st.write(random.choice(motivation_quotes))

    else:
        st.success("You're doing great!")
        st.write(random.choice(study_tips))

    # Support
    st.info(random.choice(support_messages))

    st.markdown("---")

    # Chart
    st.subheader("Habit Overview")

    chart_data = pd.DataFrame({
        "Category": ["Study", "Sleep", "Focus", "Stress"],
        "Value": [study, sleep, focus, stress]
    })

    st.bar_chart(chart_data.set_index("Category"))

    # Save data
    new_data = pd.DataFrame({
        "study": [study],
        "sleep": [sleep],
        "focus": [focus],
        "stress": [stress],
        "mood": [mood],
        "prediction": [prediction]
    })

    if os.path.exists("user_data.csv"):
        old_data = pd.read_csv("user_data.csv")
        combined = pd.concat([old_data, new_data], ignore_index=True)
        combined.to_csv("user_data.csv", index=False)
    else:
        new_data.to_csv("user_data.csv", index=False)

    st.success("Data saved successfully!")
