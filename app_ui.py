import streamlit as st
import random
import pandas as pd
from model import train_model
import os

# Page config
st.set_page_config(page_title="AI Student Wellness Assistant", layout="centered")

# 🎨 CUSTOM CSS
st.markdown("""
    <style>
    body {
        background-color: #222831;
        color: #DFD0B8;
    }
    .stApp {
        background-color: #222831;
    }
    
    /* Main Title Styling */
    .main-title {
        text-align: center;
        color: #DFD0B8;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
        padding: 20px;
        background: linear-gradient(135deg, #DFD0B8 0%, #948979 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #948979;
        font-size: 1.2em;
        margin-bottom: 30px;
        padding: 0 20px;
    }
    
    h1, h2, h3 {
        color: #DFD0B8;
    }
    
    .stButton>button {
        background-color: #DFD0B8;
        color: #222831;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #948979;
        color: white;
    }
    
    .stSlider > div {
        background-color: #393E46;
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Welcome Section - Enhanced Visibility */
    .welcome-container {
        background: linear-gradient(135deg, #393E46 0%, #2a2f3a 100%);
        border: 3px solid #DFD0B8;
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 8px 32px rgba(223, 208, 184, 0.2);
        text-align: center;
    }
    
    .welcome-container h2 {
        color: #DFD0B8;
        font-size: 2.5em;
        margin: 0 0 20px 0;
        font-weight: bold;
    }
    
    .welcome-message {
        background-color: #222831;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #DFD0B8;
        margin: 20px 0;
        font-size: 1.2em;
        line-height: 1.8;
        color: #DFD0B8;
    }
    
    /* How it Works Section */
    .how-it-works {
        background-color: #393E46;
        padding: 30px;
        border-radius: 20px;
        margin: 30px 0;
        border: 2px solid #948979;
    }
    
    .how-it-works h3 {
        color: #DFD0B8;
        font-size: 1.8em;
        margin-bottom: 20px;
    }
    
    .how-it-works ol {
        padding-left: 20px;
        line-height: 2;
        color: #DFD0B8;
    }
    
    .how-it-works li {
        margin: 15px 0;
        font-size: 1.1em;
    }
    
    .divider {
        border: none;
        border-top: 2px solid #393E46;
        margin: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- MAIN TITLE SECTION ---
st.markdown("""
    <div class="main-title">
        AI Focus & Mental Wellness Assistant
    </div>
    <div class="subtitle">
        Helping students manage study, focus, and mental health
    </div>
""", unsafe_allow_html=True)

# Load model
model = train_model()

# --- WELCOME SECTION - HIGHLY VISIBLE ---
st.markdown("""
    <div class="welcome-container">
        <h2> Welcome!</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="welcome-message">
        Hello! I am your AI companion. I'm here to help you balance your studies and mental health. 
        Let's work together to improve your focus!
    </div>
""", unsafe_allow_html=True)

# --- HOW IT WORKS SECTION ---
st.markdown("""
    <div class="how-it-works">
        <h3> What happens here?</h3>
        <p style="color: #DFD0B8; font-size: 1.1em; line-height: 1.8;">
            This platform uses Machine Learning to analyze your daily habits.
        </p>
        <p style="color: #DFD0B8; font-weight: bold; margin-top: 20px;">How it works:</p>
        <ol>
            <li><strong style="color: #DFD0B8;">Input:</strong> Tell me how much you studied, slept, and your current stress levels.</li>
            <li><strong style="color: #DFD0B8;">Analysis:</strong> I use a trained AI model to predict your potential performance.</li>
            <li><strong style="color: #DFD0B8;">Feedback:</strong> You receive personalized tips, motivational quotes, and wellness advice.</li>
            <li><strong style="color: #DFD0B8;">Tracking:</strong> Your data is saved so you can track your progress over time.</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# Inputs
st.subheader("Enter Your Daily Habits")

col1, col2 = st.columns(2)

with col1:
    study = st.slider("Study Hours", 0, 10, 2)
    sleep = st.slider("Sleep Hours", 0, 10, 5)

with col2:
    focus = st.slider("Focus Level", 1, 10, 5)
    stress = st.slider("Stress Level", 1, 10, 5)

mood = st.selectbox("Mood", ["Happy", "Neutral", "Stressed", "Anxious", "Tired"])

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

    st.markdown("## Results")

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