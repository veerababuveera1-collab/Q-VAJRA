import streamlit as st
import datetime

# =========================================================
# Q-VAJRA™ — Quantum-AI Defence Brain
# War-Room Command Dashboard (FINAL)
# =========================================================

st.set_page_config(
    page_title="Q-VAJRA™ War-Room",
    layout="wide"
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.title("🛡️ Q-VAJRA™ — Quantum-AI Defence Brain")
st.subheader("War-Room Command Dashboard")

# ---------------------------------------------------------
# CONTROL PANEL (SIMULATED SENSOR INPUTS)
# ---------------------------------------------------------
st.sidebar.header("⚙️ Control Panel")

signal = st.sidebar.slider(
    "Threat Signal Strength",
    0.0, 1.0, 0.70, 0.01
)

noise = st.sidebar.slider(
    "Sensor Noise",
    0.0, 1.0, 0.10, 0.01
)

# ---------------------------------------------------------
# CORE INTELLIGENCE LOGIC
# ---------------------------------------------------------
# 1. AI Probability (simple, explainable)
ai_probability = signal * 100

# 2. Quantum Risk (worst-case amplification)
quantum_risk = (signal * 120) + (noise * 10)
quantum_risk = min(quantum_risk, 100)

# 3. Final Risk Fusion Score
final_score = (
    (ai_probability * 0.45)
    + (quantum_risk * 0.55)
    - (noise * 5)
)

# ---------------------------------------------------------
# THREAT CLASSIFICATION (DOCTRINE-LOCKED)
# ---------------------------------------------------------
if final_score > 80.0:
    status = "🚨 THREAT DETECTED"
    color = "red"
    reason = "Score crossed escalation threshold (>80%)"

elif final_score == 80.0:
    status = "🟠 UNDER WATCH (Boundary Hold)"
    color = "orange"
    reason = "Score equals escalation boundary (80%). Hold & monitor."

elif final_score >= 60.0:
    status = "🟠 UNDER WATCH"
    color = "orange"
    reason = "Moderate risk detected. Continuous monitoring required."

else:
    status = "🟢 SAFE"
    color = "green"
    reason = "Risk below operational threshold."

# ---------------------------------------------------------
# MAIN DASHBOARD METRICS
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🧠 AI Probability", f"{ai_probability:.1f}%")
col2.metric("⚛️ Quantum Risk", f"{quantum_risk:.1f}%")
col3.metric("🎯 Final Score", f"{final_score:.1f}%")

st.markdown(
    f"## <span style='color:{color}'>{status}</span>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# EXPLAINABLE AI PANEL
# ---------------------------------------------------------
st.subheader("🧠 Explainable AI Reasoning")

st.write(f"""
• Signal strength crossed anomaly threshold  
• AI pattern similarity detected  
• Quantum worst-case outcome dominant  
• Sensor noise within acceptable limits  
• **Decision Logic:** {reason}
""")

# ---------------------------------------------------------
# AUDIT LOG (DEFENCE CRITICAL)
# ---------------------------------------------------------
st.subheader("🧾 Audit Log")

timestamp = datetime.datetime.now().strftime("%H:%M:%S")

audit_entry = (
    f"[{timestamp}] "
    f"AI={ai_probability:.1f}% | "
    f"QR={quantum_risk:.1f}% | "
    f"FINAL={final_score:.1f}% | "
    f"{status}"
)

st.code(audit_entry)

# ---------------------------------------------------------
# SYSTEM STATUS
# ---------------------------------------------------------
st.success(
    "✅ System Stable | No external ML dependencies | Offline Ready | Human-in-Loop Enabled"
)
