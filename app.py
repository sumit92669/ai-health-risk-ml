import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Health Risk AI", page_icon="🧠", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0E1117, #1C1F26);
    background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
    color: white;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #AAAAAA;
    margin-bottom: 35px;
}

/* GLASS CARD EFFECT */
.card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 25px rgba(0,255,150,0.25);
}

/* RESULT COLORS */
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

/* BUTTON */
div.stButton > button {
    background-color: #00FF9C;
    color: black;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #00CC7A;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🧠 AI Health Risk Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Offline Lifestyle Disease Risk Estimation System</div>', unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🩺 Enter Health Parameters")

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

        st.subheader("💊 Preventive Suggestions")
        st.write("• Maintain balanced diet")
        st.write("• Regular exercise")
        st.write("• Routine health checkups")

    elif risk_score < 160:
        st.markdown('<div class="result-medium">⚠️ Medium Risk</div>', unsafe_allow_html=True)
        st.write("Some parameters are slightly elevated.")

        st.subheader("💊 Lifestyle Adjustments")
        st.write("• Reduce sugar intake")
        st.write("• Monitor blood pressure")
        st.write("• Increase physical activity")

        st.subheader("💉 Possible Medical Advice")
        st.write("• Mild BP regulation medicines (doctor consultation)")
        st.write("• Dietary sugar control")

    else:
        st.markdown('<div class="result-high">🚨 High Risk</div>', unsafe_allow_html=True)
        st.write("Your parameters suggest elevated health risks.")

        st.subheader("💊 Immediate Recommendations")
        st.write("• Consult medical professional")
        st.write("• Strict diet control")
        st.write("• Regular monitoring")

        st.subheader("💉 Possible Medical Interventions")
        st.write("• Blood pressure management medicines")
        st.write("• Glucose regulation treatments")

        st.subheader("⚠️ General Side Effects Awareness")
        st.write("• Dizziness")
        st.write("• Fatigue")
        st.write("• Mild nausea")

    st.markdown('</div>', unsafe_allow_html=True)
