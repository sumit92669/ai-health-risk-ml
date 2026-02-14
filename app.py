import streamlit as st

st.title("AI-Based Disease Risk Prediction System")

st.write("Enter your basic health details:")

age = st.number_input("Age", 1, 100)
weight = st.number_input("Weight (kg)", 30, 150)
bp = st.number_input("Blood Pressure", 80, 200)
sugar = st.number_input("Sugar Level", 70, 300)

if st.button("Predict Risk"):

    risk_score = (bp + sugar + weight) / 3

    if risk_score < 120:
        risk = "Low Risk"
    elif risk_score < 160:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    st.subheader("Prediction Result:")
    st.write(risk)
