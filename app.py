# ======================================================
# Q-VAJRA™ — AI + Quantum Defence Brain (Demo Version)
# Streamlit Cloud Safe | sklearn fixed
# ======================================================

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Q-VAJRA™ Defence Brain",
    layout="wide"
)

# ------------------------------------------------------
# TITLE
# ------------------------------------------------------
st.title("🛡️ Q-VAJRA™ — Quantum-AI Defence Brain")
st.caption("AI Threat Prediction + Quantum-Inspired Risk Simulation")

# ------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------
st.sidebar.header("⚙️ Control Panel")

threat_level = st.sidebar.slider(
    "Threat Signal Strength",
    min_value=0.0,
    max_value=1.0,
    value=0.6
)

sensor_noise = st.sidebar.slider(
    "Sensor Noise",
    min_value=0.0,
    max_value=1.0,
    value=0.2
)

# ------------------------------------------------------
# AI MODEL (Simple Logistic Regression)
# ------------------------------------------------------
@st.cache_resource
def load_ai_model():
    # Dummy training data
    X = np.array([
        [0.1], [0.2], [0.3],
        [0.6], [0.7], [0.9]
    ])
    y = np.array([0, 0, 0, 1, 1, 1])  # 0 = SAFE, 1 = THREAT

    model = LogisticRegression()
    model.fit(X, y)
    return model

model = load_ai_model()

# AI Prediction
ai_prob = model.predict_proba([[threat_level]])[0][1]

# ------------------------------------------------------
# QUANTUM-INSPIRED RISK SIMULATION (Symbolic)
# ------------------------------------------------------
def quantum_risk_simulation(signal, noise):
    """
    Quantum-inspired superposition risk score
    (No real quantum hardware — safe demo)
    """
    superposition = (signal * 0.7) + (noise * 0.3)
    interference = np.sin(superposition * np.pi)
    risk_score = abs(interference)
    return min(risk_score, 1.0)

quantum_risk = quantum_risk_simulation(threat_level, sensor_noise)

# ------------------------------------------------------
# FINAL FUSION DECISION
# ------------------------------------------------------
final_score = (ai_prob * 0.6) + (quantum_risk * 0.4)

if final_score > 0.65:
    decision = "🚨 THREAT DETECTED"
    color = "red"
elif final_score > 0.4:
    decision = "⚠️ SUSPICIOUS"
    color = "orange"
else:
    decision = "✅ SAFE"
    color = "green"

# ------------------------------------------------------
# DASHBOARD DISPLAY
# ------------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "🧠 AI Threat Probability",
    f"{ai_prob*100:.1f}%"
)

col2.metric(
    "⚛️ Quantum Risk Score",
    f"{quantum_risk*100:.1f}%"
)

col3.metric(
    "🎯 Final Fusion Score",
    f"{final_score*100:.1f}%"
)

st.markdown("---")

st.markdown(
    f"<h2 style='color:{color}; text-align:center;'>{decision}</h2>",
    unsafe_allow_html=True
)

# ------------------------------------------------------
# LOG PANEL
# ------------------------------------------------------
st.subheader("📡 System Log")

log_data = pd.DataFrame({
    "Parameter": [
        "Threat Signal",
        "Sensor Noise",
        "AI Probability",
        "Quantum Risk",
        "Final Score"
    ],
    "Value": [
        threat_level,
        sensor_noise,
        ai_prob,
        quantum_risk,
        final_score
    ]
})

st.dataframe(log_data, use_container_width=True)

st.success("System running normally. No missing modules detected.")
