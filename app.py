# ======================================================
# Q-VAJRA™ — Quantum-AI Defence Brain
# Streamlit Cloud SAFE VERSION (NO sklearn)
# ======================================================

import streamlit as st
import numpy as np
import pandas as pd

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Q-VAJRA™ Defence Brain",
    layout="wide"
)

st.title("🛡️ Q-VAJRA™ — Quantum-AI Defence Brain")
st.caption("AI Threat Reasoning + Quantum-Inspired Risk Fusion")

# ------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------
st.sidebar.header("⚙️ Control Panel")

threat_signal = st.sidebar.slider(
    "Threat Signal Strength",
    0.0, 1.0, 0.6
)

sensor_noise = st.sidebar.slider(
    "Sensor Noise",
    0.0, 1.0, 0.2
)

# ------------------------------------------------------
# AI LOGIC (Pure Python Logistic Function)
# ------------------------------------------------------
def ai_threat_probability(x):
    """
    Lightweight AI logic (logistic function)
    sklearn-free, cloud-safe
    """
    weight = 8.0
    bias = -4.0
    z = (x * weight) + bias
    return 1 / (1 + np.exp(-z))

ai_prob = ai_threat_probability(threat_signal)

# ------------------------------------------------------
# QUANTUM-INSPIRED RISK MODEL
# ------------------------------------------------------
def quantum_risk(signal, noise):
    superposition = (signal * 0.7) + (noise * 0.3)
    interference = np.sin(superposition * np.pi)
    return abs(interference)

quantum_score = quantum_risk(threat_signal, sensor_noise)

# ------------------------------------------------------
# FUSION DECISION
# ------------------------------------------------------
final_score = (ai_prob * 0.6) + (quantum_score * 0.4)

if final_score > 0.65:
    status = "🚨 THREAT DETECTED"
    color = "red"
elif final_score > 0.4:
    status = "⚠️ SUSPICIOUS"
    color = "orange"
else:
    status = "✅ SAFE"
    color = "green"

# ------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------
c1, c2, c3 = st.columns(3)

c1.metric("🧠 AI Probability", f"{ai_prob*100:.1f}%")
c2.metric("⚛️ Quantum Risk", f"{quantum_score*100:.1f}%")
c3.metric("🎯 Final Score", f"{final_score*100:.1f}%")

st.markdown("---")

st.markdown(
    f"<h2 style='color:{color}; text-align:center;'>{status}</h2>",
    unsafe_allow_html=True
)

# ------------------------------------------------------
# LOG TABLE
# ------------------------------------------------------
log = pd.DataFrame({
    "Metric": [
        "Threat Signal",
        "Sensor Noise",
        "AI Probability",
        "Quantum Risk",
        "Final Score"
    ],
    "Value": [
        threat_signal,
        sensor_noise,
        ai_prob,
        quantum_score,
        final_score
    ]
})

st.dataframe(log, use_container_width=True)

st.success("✅ System Stable | No external ML dependencies")
