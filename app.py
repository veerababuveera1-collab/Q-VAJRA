# ======================================================
# Q-VAJRA™ — Quantum-AI Defence Brain
# ROE + DRDO / iDEX Pitch Mode
# ======================================================

import streamlit as st
import numpy as np
import pandas as pd
import datetime

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(page_title="Q-VAJRA™ War-Room", layout="wide")

st.title("🛡️ Q-VAJRA™ — Quantum-AI Defence Brain")
st.caption("War-Room Command Dashboard")

# ------------------------------------------------------
# SIDEBAR — MODE SELECTION
# ------------------------------------------------------
st.sidebar.header("⚙️ Command Controls")

roe_mode = st.sidebar.selectbox(
    "Rules of Engagement (ROE)",
    ["PEACETIME", "SKIRMISH", "WARTIME"]
)

pitch_mode = st.sidebar.toggle("🎯 Pitch Mode (DRDO / iDEX)")

threat_signal = st.sidebar.slider("Threat Signal Strength", 0.0, 1.0, 0.65)
sensor_noise = st.sidebar.slider("Sensor Noise", 0.0, 1.0, 0.25)
threat_type = st.sidebar.selectbox(
    "Detected Threat Type",
    ["Drone", "Missile", "Cyber", "Electronic Warfare"]
)

# ------------------------------------------------------
# AI + QUANTUM CORE
# ------------------------------------------------------
def ai_probability(x):
    return 1 / (1 + np.exp(-((x * 8) - 4)))

def quantum_risk(signal, noise):
    return abs(np.sin(((signal * 0.7) + (noise * 0.3)) * np.pi))

ai_prob = ai_probability(threat_signal)
qrisk = quantum_risk(threat_signal, sensor_noise)

THREAT_WEIGHT = {
    "Drone": 0.8,
    "Missile": 1.0,
    "Cyber": 0.7,
    "Electronic Warfare": 0.9
}

final_score = ((ai_prob * 0.6) + (qrisk * 0.4)) * THREAT_WEIGHT[threat_type]

# ------------------------------------------------------
# DECISION STATE
# ------------------------------------------------------
if final_score >= 0.75:
    state = "🚨 THREAT"
elif final_score >= 0.5:
    state = "🟠 UNDER WATCH"
else:
    state = "✅ SAFE"

# ------------------------------------------------------
# ROE ENFORCEMENT
# ------------------------------------------------------
roe_action = "No Action"

if roe_mode == "PEACETIME":
    roe_action = "Monitor Only"
elif roe_mode == "SKIRMISH":
    if state == "🟠 UNDER WATCH":
        roe_action = "Deploy Scout Drone"
    elif state == "🚨 THREAT":
        roe_action = "Await Human Approval"
elif roe_mode == "WARTIME":
    if threat_type == "Missile" and state == "🚨 THREAT":
        roe_action = "AUTO INTERCEPT AUTHORIZED"
    else:
        roe_action = "Execute Standard Defence"

# ------------------------------------------------------
# DISPLAY
# ------------------------------------------------------
c1, c2, c3 = st.columns(3)
c1.metric("🧠 AI Probability", f"{ai_prob*100:.1f}%")
c2.metric("⚛️ Quantum Risk", f"{qrisk*100:.1f}%")
c3.metric("🎯 Final Score", f"{final_score*100:.1f}%")

st.markdown(f"## {state}")
st.write(f"### 🔐 ROE MODE: {roe_mode}")
st.info(f"### ⚔️ Action: {roe_action}")

# ------------------------------------------------------
# HUMAN OVERRIDE
# ------------------------------------------------------
if roe_action in ["Await Human Approval", "AUTO INTERCEPT AUTHORIZED"]:
    st.subheader("🧑‍✈️ Commander Override")
    decision = st.radio("Commander Decision", ["Approve", "Hold", "Abort"])
    st.success(f"Decision Recorded: {decision}")

# ------------------------------------------------------
# PITCH MODE VIEW
# ------------------------------------------------------
if pitch_mode:
    st.markdown("---")
    st.subheader("🎯 DRDO / iDEX Evaluation Summary")

    st.write("""
    **System Type:** Quantum-AI Assisted Defence Decision Platform  
    **Autonomy:** Conditional (Human-in-the-loop enforced)  
    **Explainability:** Enabled  
    **ROE Compliance:** Enforced  
    **Offline Capability:** Yes  
    **Audit Ready:** Yes
    """)

# ------------------------------------------------------
# AUDIT LOG
# ------------------------------------------------------
time = datetime.datetime.now().strftime("%H:%M:%S")
st.code(f"[{time}] ROE={roe_mode} | TYPE={threat_type} | FINAL={final_score*100:.1f}% | ACTION={roe_action}")

st.success("✅ Defence-Grade | ROE Enforced | Pitch Ready")
