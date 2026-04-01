# 🧠 AI Focus & Mental Wellness Assistant

> A Streamlit-powered AI application that helps students balance academic performance with mental wellness through personalized insights and predictive analytics.

**Live Demo:** [ai-student-wellness-assistant.streamlit.app](https://ai-student-wellness-assistant.streamlit.app/)  
**GitHub:** [DilaknaH/ai-student-wellness-assistant](https://github.com/DilaknaH/ai-student-wellness-assistant)

---

## Project Overview

The **AI Focus & Mental Wellness Assistant** is an intelligent web application designed to support students in managing their study habits, focus levels, and mental health. Using machine learning, the app:

✅ **Predicts academic performance** based on daily input metrics  
✅ **Analyzes stress & mood patterns** to detect burnout risks  
✅ **Delivers personalized feedback** with motivational quotes and study tips  
✅ **Visualizes habit trends** through interactive charts  
✅ **Tracks progress over time** with local data persistence

Built with **Streamlit**, **Scikit-learn**, and **Pandas**, this project demonstrates end-to-end ML pipeline skills—from data preprocessing to deployment.

---

## Key Features

### AI-Powered Insights
- Linear Regression model predicts performance score (0-100%) based on study hours, sleep, and focus levels
- Rule-based wellness engine provides contextual feedback for stress, anxiety, or low focus

### Modern UI/UX
- Clean dark theme with custom CSS gradients and responsive layout
- Sticky header navigation with clear visual hierarchy
- Card-style feedback sections with color-coded alerts (success/warning/error)
- Interactive sliders and intuitive mood selector

### Data Visualization & Tracking
- Real-time bar charts showing habit distribution
- CSV-based local storage for progress tracking across sessions
- Exportable user data for personal analysis

### Personalized Support
- Rotating motivational quotes and study tips
- Context-aware wellness messages based on user input
- Encouraging feedback loop to promote healthy habits

---

## Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Python 3.x, Scikit-learn, Pandas |
| **Frontend** | Streamlit, Custom CSS3, HTML5 |
| **Data** | CSV storage, In-memory processing |
| **DevOps** | Git, GitHub, Streamlit Cloud |
| **ML** | Linear Regression, Feature Engineering, Model Training |

---

## How to Run Locally

### Prerequisites
- Python 3.8+
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/DilaknaH/ai-student-wellness-assistant.git
   cd ai-student-wellness-assistant
   ```

2. **Create & activate virtual environment** *(recommended)*
   ```bash
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**
   ```bash
   streamlit run app_ui.py
   ```

5. **Open in browser**
   ```
   http://localhost:8501
   ```

---

## Project Structure

```
ai-student-wellness-assistant/
├── app_ui.py           # Main Streamlit application (UI + logic)
├── model.py            # ML model training & prediction functions
├── data.csv            # Training dataset for model initialization
├── user_data.csv       # Local storage for user session data (auto-generated)
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

---

## Why This Project Matters for AI Careers

This project demonstrates **practical, interview-ready skills**:

🔹 **End-to-End ML Pipeline**: Data → Model → Prediction → UI → Deployment  
🔹 **User-Centric Design**: Solves a real student pain point with empathy  
🔹 **Clean Code Practices**: Modular structure, clear variable naming, comments  
🔹 **Deployment Experience**: Live Streamlit Cloud deployment  
🔹 **Problem-Solving**: Balances technical accuracy with wellness-focused UX  

---

##  Sample Output

![App Preview](https://via.placeholder.com/800x400/222831/DFD0B8?text=AI+Wellness+Assistant+Preview)

*Features shown:*
- Performance prediction metric
- Color-coded feedback cards
- Interactive habit visualization
- Motivational wellness messages

---

## Future Enhancements *(Roadmap)*

- [ ] Add user authentication & cloud database (Firebase/Supabase)
- [ ] Integrate NLP for journaling/mood analysis
- [ ] Expand model to include more features (exercise, social time)
- [ ] Add exportable weekly reports (PDF)
- [ ] Implement A/B testing for advice effectiveness
- [ ] Add mobile-responsive design improvements

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## Author

**Dilakna Godagamage**  
Undergraduate | AI & Machine Learning Enthusiast  
 

> *"Building AI that cares about people, not just predictions."*

---

## Acknowledgments

- Streamlit community for excellent documentation
- Scikit-learn for accessible ML tools
- Mental health advocates inspiring wellness-focused tech

---

> ⭐ **If you found this project helpful, please give it a star!** It helps others discover it too.


