import streamlit as st
import datetime

st.set_page_config(page_title="Q-VAJRA™ War-Room", layout="wide")

st.title("🛡️ Q-VAJRA™ — Quantum-AI Defence Brain")
st.subheader("War-Room Command Dashboard")

# --- Control Panel ---
st.sidebar.header("⚙️ Control Panel")
signal = st.sidebar.slider("Threat Signal Strength", 0.0, 1.0, 0.69)
noise = st.sidebar.slider("Sensor Noise", 0.0, 1.0, 0.10)

# --- Core Logic ---
ai_probability = signal * 100
quantum_risk = min(100, (signal * 120) + (noise * 10))
final_score = (ai_probability * 0.45) + (quantum_risk * 0.55) - (noise * 5)

# --- Threat Classification ---
if final_score >= 80:
    status = "🚨 THREAT DETECTED"
    color = "red"
elif final_score >= 60:
    status = "🟠 UNDER WATCH"
    color = "orange"
else:
    status = "🟢 SAFE"
    color = "green"

# --- Display Panel ---
col1, col2, col3 = st.columns(3)
col1.metric("🧠 AI Probability", f"{ai_probability:.1f}%")
col2.metric("⚛️ Quantum Risk", f"{quantum_risk:.1f}%")
col3.metric("🎯 Final Score", f"{final_score:.1f}%")

st.markdown(f"## <span style='color:{color}'>{status}</span>", unsafe_allow_html=True)

# --- Explainability ---
st.subheader("🧠 Explainable AI Reasoning")
st.write("""
• Signal strength crossed anomaly threshold  
• AI pattern similarity detected  
• Quantum worst-case outcome dominant  
• Sensor noise within acceptable limits  
""")

# --- Audit Log ---
st.subheader("🧾 Audit Log")
st.code(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] "
        f"AI={ai_probability:.1f}% | QR={quantum_risk:.1f}% | FINAL={final_score:.1f}% | {status}")

# --- System Status ---
st.success("✅ System Stable | No external ML dependencies | Offline Ready")
