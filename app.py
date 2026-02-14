import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Health Risk AI", page_icon="🧠", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 40px;
}

.card {
    background-color: #1C1F26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 15px rgba(0,255,150,0.3);
}

.result-low {
    color: #00FF9C;
    font-size: 28px;
    font-weight: bold;
}

.result-medium {
    color: #FFD700;
    font-size: 28px;
    font-weight: bold;
}

.result-high {
    color: #FF4B4B;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🧠 AI Health Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Offline Lifestyle Disease Risk Estimation System</div>', unsafe_allow_html=True)

# ---------------- INPUT SECTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

age = st.number_input("Age", 1, 100)
weight = st.number_input("Weight (kg)", 30, 150)
bp = st.number_input("Blood Pressure", 80, 200)
sugar = st.number_input("Sugar Level", 70, 300)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("🚀 Predict Health Risk"):

    risk_score = (bp + sugar + weight) / 3

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if risk_score < 120:
        st.markdown('<div class="result-low">✅ Low Risk</div>', unsafe_allow_html=True)
        st.write("Your health parameters indicate a relatively safe condition.")

        st.subheader("💊 Preventive Suggestions:")
        st.write("• Maintain balanced diet")
        st.write("• Regular exercise")
        st.write("• Routine checkups")

    elif risk_score < 160:
        st.markdown('<div class="result-medium">⚠️ Medium Risk</div>', unsafe_allow_html=True)
        st.write("Some parameters are slightly elevated.")

        st.subheader("💊 Suggested Lifestyle Adjustments:")
        st.write("• Reduce sugar intake")
        st.write("• Monitor blood pressure")
        st.write("• Increase physical activity")

        st.subheader("💉 Possible Medical Advice:")
        st.write("• Mild BP regulation medicines (doctor consultation)")
        st.write("• Dietary sugar control")

    else:
        st.markdown('<div class="result-high">🚨 High Risk</div>', unsafe_allow_html=True)
        st.write("Your parameters suggest elevated health risks.")

        st.subheader("💊 Immediate Recommendations:")
        st.write("• Consult medical professional")
        st.write("• Strict diet control")
        st.write("• Regular monitoring")

        st.subheader("💉 Possible Medical Interventions:")
        st.write("• Blood pressure management medicines")
        st.write("• Glucose regulation treatments")

        st.subheader("⚠️ Potential Side Effects (General Awareness):")
        st.write("• Dizziness")
        st.write("• Fatigue")
        st.write("• Mild nausea")

    st.markdown('</div>', unsafe_allow_html=True)
