import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Smart Transport AI", layout="wide")

# ----------------------------
# Create Dataset
# ----------------------------
data = {
    "waiting_time": [20, 5, 15, 2, 25, 10, 30, 3, 12, 18],
    "travel_time": [30, 15, 25, 10, 35, 20, 40, 12, 22, 28],
    "age": [25, 35, 28, 40, 22, 30, 19, 45, 33, 27],
    "mode": ["bus", "car", "taxi", "car", "bus", "taxi", "bus", "car", "taxi", "bus"],
    "income": [50000, 150000, 80000, 200000, 40000, 120000, 30000, 250000, 90000, 60000],
}

df = pd.DataFrame(data)

# ----------------------------
# Train Model
# ----------------------------
X = df[["income", "waiting_time", "travel_time", "age"]]
y = df["mode"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# ----------------------------
# Title
# ----------------------------
st.title("🚍 Smart Transport Decision System (Abuja)")
st.markdown("AI-powered system to predict the best transport mode based on user inputs.")

# ----------------------------
# Layout
# ----------------------------
col1, col2 = st.columns(2)

# ----------------------------
# Left Column - Dataset
# ----------------------------
with col1:
    st.header("📊 Dataset Overview")
    st.dataframe(df)

    st.subheader("📈 Mode Distribution")
    mode_counts = df["mode"].value_counts()
    st.bar_chart(mode_counts)

# ----------------------------
# Right Column - Prediction
# ----------------------------
with col2:
    st.header("🔮 Prediction Panel")

    income = st.slider("Monthly Income (₦)", 20000, 300000, 50000)
    waiting_time = st.slider("Waiting Time (minutes)", 1, 60, 10)
    travel_time = st.slider("Travel Time (minutes)", 5, 60, 20)
    age = st.slider("Age", 18, 60, 30)

    if st.button("Predict Mode"):
        input_data = np.array([[income, waiting_time, travel_time, age]])
        prediction = model.predict(input_data)[0]

        if prediction == "bus":
            st.success("🚍 Recommended Mode: PUBLIC BUS")
        elif prediction == "car":
            st.success("🚗 Recommended Mode: PRIVATE CAR")
        else:
            st.success("🚕 Recommended Mode: TAXI")

# ----------------------------
# Insights Section
# ----------------------------
st.markdown("---")
st.header("📌 Key Insights")

st.markdown("""
- Higher income users tend to prefer private cars  
- Longer waiting times reduce the likelihood of using buses  
- Travel time significantly influences transport mode choice  
- Improving bus availability can shift users from cars to public transport  
""")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("Built with Machine Learning + Streamlit 🚀")