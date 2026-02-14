import streamlit as st
import plotly.graph_objects as go
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Health Risk AI", page_icon="🧠", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* 💣 KILL STREAMLIT HEADER + BAR + GHOST ELEMENTS */
[data-testid="stHeader"] {display: none;}
[data-testid="stToolbar"] {display: none;}
[data-testid="stDecoration"] {display: none;}
[data-testid="stStatusWidget"] {display: none;}
hr {display: none;}   /* ← THIS kills glowing bar */

/* REMOVE TOP SPACING */
.block-container {
    padding-top: 0.5rem;
}

/* 🌌 BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0E1117, #1C1F26);
    color: white;
    overflow: hidden;
}

/* ✨ GLOW PARTICLES */
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: radial-gradient(rgba(0,255,150,0.15) 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0.15;
    z-index: -2;
}

/* 💊 FLOATING PILLS */
.pill {
    position: fixed;
    width: 40px;
    animation: float 10s infinite linear;
    opacity: 0.15;
}

@keyframes float {
    from { transform: translateY(100vh); }
    to { transform: translateY(-10vh); }
}

/* 🧊 GLASS PANEL */
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

/* 🎯 RESULT COLORS */
.low {color: #00FF9C; font-size: 26px; font-weight: bold;}
.medium {color: #FFD700; font-size: 26px; font-weight: bold;}
.high {color: #FF4B4B; font-size: 26px; font-weight: bold;}

/* 🚀 BUTTON */
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

# ---------------- FLOATING PILLS ----------------
for i in range(6):
    st.markdown(
        f'<img class="pill" src="https://cdn-icons-png.flaticon.com/512/2966/2966481.png" '
        f'style="left:{random.randint(0,100)}%; animation-duration:{random.randint(8,14)}s;">',
        unsafe_allow_html=True
    )

# ---------------- HEADER ----------------
st.markdown('<h1 style="text-align:center;">🧠 AI Health Risk Predictor</h1>', unsafe_allow_html=True)
st.markdown('<h4 style="text-align:center; color: #00FF9C;">💊 Advanced Health Insight Engine</h4>', unsafe_allow_html=True)

# ---------------- INPUT PANEL ----------------
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
        risk_label = "Low Risk"
        color_class = "low"
    elif risk_score < 160:
        risk_label = "Medium Risk"
        color_class = "medium"
    else:
        risk_label = "High Risk"
        color_class = "high"

    st.markdown(f'<div class="{color_class}">Prediction: {risk_label}</div>', unsafe_allow_html=True)

    # ---------------- GAUGE ----------------
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text': "Risk Score"},
        gauge={
            'axis': {'range': [0, 200]},
            'bar': {'color': "cyan"},
            'steps': [
                {'range': [0, 120], 'color': "#00FF9C"},
                {'range': [120, 160], 'color': "#FFD700"},
                {'range': [160, 200], 'color': "#FF4B4B"},
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
