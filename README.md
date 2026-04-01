# 🧠 AI Focus & Mental Wellness Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b.svg)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)
![Status](https://img.shields.io/badge/Status-Live-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> A Streamlit-powered AI application that helps students balance academic performance with mental wellness through personalized insights and predictive analytics.

🔗 **Live Demo:** [https://ai-student-wellness-assistant.streamlit.app/](https://ai-student-wellness-assistant.streamlit.app/)

📂 **GitHub Repo:** [https://github.com/DilaknaH/ai-student-wellness-assistant](https://github.com/DilaknaH/ai-student-wellness-assistant)

---

## Project Overview

The **AI Focus & Mental Wellness Assistant** is an intelligent web application designed to support students in managing their study habits, focus levels, and mental health.

Using machine learning, the app:

**Predicts academic performance** based on daily input metrics
**Analyzes stress & mood patterns** to detect burnout risks
**Delivers personalized feedback** with motivational quotes and study tips
**Visualizes habit trends** through interactive charts
**Tracks progress over time** with local data persistence

Built with **Streamlit**, **Scikit-learn**, and **Pandas**, this project demonstrates an **end-to-end ML pipeline** from data preprocessing to deployment.

---

## Key Features

### AI-Powered Insights

* Linear Regression model predicts performance score (0–100%)
* Rule-based wellness engine for stress, anxiety & focus analysis

### Modern UI/UX

* Dark theme with custom gradients
* Clean layout with card-based feedback
* Color-coded alerts (success / warning / error)
* Interactive sliders & mood selector

### Data Visualization & Tracking

* Real-time charts for habit insights
* CSV-based local storage
* Track progress across sessions

### Personalized Support

* Motivational quotes & study tips
* Context-aware wellness suggestions
* Positive feedback loop for habit building

---

## Tech Stack

| Category       | Technologies                 |
| -------------- | ---------------------------- |
| **Backend**    | Python, Scikit-learn, Pandas |
| **Frontend**   | Streamlit, HTML5, CSS3       |
| **Data**       | CSV Storage                  |
| **Deployment** | Git, GitHub, Streamlit Cloud |
| **ML**         | Linear Regression            |

---

## How to Run Locally

### Prerequisites

* Python 3.8+
* pip

### Setup

```bash
git clone https://github.com/DilaknaH/ai-student-wellness-assistant.git
cd ai-student-wellness-assistant
```

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
streamlit run app_ui.py
```

🔗 Open: [http://localhost:8501](http://localhost:8501)

---

## Project Structure

```
ai-student-wellness-assistant/
├── app_ui.py
├── model.py
├── data.csv
├── user_data.csv
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## Why This Project Stands Out

✔ End-to-End ML pipeline (Data → Model → UI → Deployment)
✔ Real-world problem solving (student mental wellness)
✔ Clean UI + strong UX thinking
✔ Deployable + live product
✔ Portfolio-ready for AI/ML roles

---

## Future Enhancements

* [ ] User authentication (Firebase / Supabase)
* [ ] NLP-based mood journaling
* [ ] More features (exercise, social time)
* [ ] PDF report generation
* [ ] Mobile optimization
* [ ] Smarter ML models

---

## Contributing

1. Fork the repo
2. Create branch (`feature/your-feature`)
3. Commit changes
4. Push
5. Open PR

---

## License

MIT License

---

## Author

**Dilakna Godagamage**
AI & Machine Learning Enthusiast

> *“Building AI that cares about people, not just predictions.”*

---

## Acknowledgments

* Streamlit community
* Scikit-learn
* Mental health awareness initiatives

---

⭐ **If you found this useful, give it a star!**

