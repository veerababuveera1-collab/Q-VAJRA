# ======================================================
# Q-VAJRA™ — Quantum-AI Defence Brain
# WAR-ROOM COMMAND DASHBOARD
# Threat Classification + NETRA Hook + Human Override
# ======================================================

import streamlit as st
import numpy as np
import pandas as pd
import datetime

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Q-VAJRA™ War-Room",
    layout="wide"
)

st.title("🛡️ Q-VAJRA™ — Quantum-AI Defence Brain")
st.caption("War-Room Command Dashboard")

# ------------------------------------------------------
# SIDEBAR — CONTROL PANEL
# ------------------------------------------------------
st.sidebar.header("⚙️ Control Panel")

threat_signal = st.sidebar.slider(
    "Threat Signal Strength",
    0.0, 1.0, 0.65
)

sensor_noise = st.sidebar.slider(
    "Sensor Noise",
    0.0, 1.0, 0.25
)

threat_type = st.sidebar.selectbox(
    "Detected Threat Type",
    ["Drone", "Missile", "Cyber", "Electronic Warfare"]
)

# ------------------------------------------------------
# AI LOGIC (Explainable, sklearn-free)
# ------------------------------------------------------
def ai_probability(signal):
    weight = 8.0
    bias = -4.0
    z = (signal * weight) + bias
    return 1 / (1 + np.exp(-z))

ai_prob = ai_probability(threat_signal)

# ------------------------------------------------------
# QUANTUM-INSPIRED RISK
# ------------------------------------------------------
def quantum_risk(signal, noise):
    superposition = (signal * 0.7) + (noise * 0.3)
    return abs(np.sin(superposition * np.pi))

quantum_score = quantum_risk(threat_signal, sensor_noise)

# ------------------------------------------------------
# THREAT TYPE WEIGHTING (CRITICAL FEATURE)
# ------------------------------------------------------
THREAT_WEIGHTS = {
    "Drone": 0.8,
    "Missile": 1.0,
    "Cyber": 0.7,
    "Electronic Warfare": 0.9
}

type_weight = THREAT_WEIGHTS[threat_type]

# ------------------------------------------------------
# FINAL FUSION ENGINE
# ------------------------------------------------------
final_score = ((ai_prob * 0.6) + (quantum_score * 0.4)) * type_weight

# ------------------------------------------------------
# DECISION LOGIC
# ------------------------------------------------------
if final_score >= 0.75:
    status = "🚨 THREAT"
    color = "red"
elif final_score >= 0.5:
    status = "🟠 UNDER WATCH"
    color = "orange"
else:
    status = "✅ SAFE"
    color = "green"

# ------------------------------------------------------
# DASHBOARD METRICS
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
# EXPLAINABLE AI REASONING
# ------------------------------------------------------
st.subheader("🧠 Explainable AI Reasoning")

reasons = []
if threat_signal > 0.6:
    reasons.append("• Signal strength crossed anomaly threshold")
if ai_prob > 0.6:
    reasons.append("• AI pattern similarity detected")
if quantum_score > 0.7:
    reasons.append("• Quantum worst-case outcome dominant")
if sensor_noise < 0.4:
    reasons.append("• Sensor noise within acceptable limits")

reasons.append(f"• Threat Type Classified as: {threat_type}")
reasons.append("• Decision Logic: Moderate risk detected. Continuous monitoring required." if status != "🚨 THREAT"
               else "• Decision Logic: High confidence threat. Escalation required.")

for r in reasons:
    st.write(r)

# ------------------------------------------------------
# NETRA / GARUDA-NAYAN HOOK (SIMULATION)
# ------------------------------------------------------
st.subheader("📡 Autonomous Response Layer")

if status == "🟠 UNDER WATCH":
    st.info("NETRA Action: 🛰️ Scout Drone Dispatched for Recon")
elif status == "🚨 THREAT":
    st.warning("NETRA Action: 🔒 Awaiting Human Authorization")
else:
    st.success("NETRA Action: No deployment required")

# ------------------------------------------------------
# HUMAN-IN-LOOP OVERRIDE (MANDATORY FOR DEPLOYMENT)
# ------------------------------------------------------
if status == "🚨 THREAT":
    st.subheader("🧑‍✈️ Commander Override Panel")

    decision = st.radio(
        "Commander Decision",
        ["Approve Intercept", "Hold / Monitor", "Abort"]
    )

    st.write(f"📝 Commander Decision Recorded: **{decision}**")

# ------------------------------------------------------
# AUDIT LOG
# ------------------------------------------------------
st.subheader("🧾 Audit Log")

timestamp = datetime.datetime.now().strftime("%H:%M:%S")

log_entry = f"[{timestamp}] TYPE={threat_type} | AI={ai_prob*100:.1f}% | QR={quantum_score*100:.1f}% | FINAL={final_score*100:.1f}% | {status}"

st.code(log_entry)

st.success("✅ System Stable | Offline Ready | Human-in-Loop Enabled | Defence Safe")
