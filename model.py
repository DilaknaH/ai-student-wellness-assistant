import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    data = pd.read_csv("data.csv")
    
    X = data[["study_hours", "sleep_hours", "focus_level"]]
    y = data["performance"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    return model
