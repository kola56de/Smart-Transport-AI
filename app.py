import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Smart Transport AI", layout="wide")
st.header("📊 Dataset Overview")

st.header("🔮 Prediction Panel")
# Create Dataset
data = {
    "waiting_time": [20, 5, 15, 2, 25, 10, 30, 3, 12, 18],
    "travel_time": [30, 15, 25, 10, 35, 20, 40, 12, 22, 28],
    "age": [25, 35, 28, 40, 22, 30, 19, 45, 33, 27],
    "mode": ['bus', 'car', 'taxi', 'car', 'bus', 'taxi','bus', 'car', 'taxi', 'bus'],
    "income": [50000, 150000, 80000, 200000, 40000, 120000, 30000, 250000, 90000,60000],
}

df = pd.DataFrame(data)

# Train model
X = df[["income", "waiting_time", "travel_time", "age"]]
y = df["mode"]

model = RandomForestClassifier()
model.fit(X, y)

# Streamlit UI
st.title("🚍 Smart Transport Predictor")

st.write("Dataset Preview:")
st.dataframe(df)

income = st.slider("Income", 20000, 300000, 50000)
waiting_time = st.slider("Waiting Time", 1, 60, 10)
travel_time = st.slider("Travel Time", 5, 60, 20)
age = st.slider("Age", 18, 60, 30)

if st.button("Predict"):
    prediction = model.predict([[income, waiting_time, travel_time, age]])
    st.success(f"Recommended Mode: {prediction[0]}")


