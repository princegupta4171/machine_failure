import streamlit as st
import pickle
import numpy as np
import time

# Page config
st.set_page_config(
    page_title="Machine Failure Prediction",
    page_icon="⚙️",
    layout="centered"
)

# Load model
model1 = pickle.load(open("machinefailure.pkl", "rb"))

# -------------------- CSS --------------------
st.markdown("""
<style>
/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #1f4037, #99f2c8, #1c92d2, #f2fcfe);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Card */
.card {
    background-color: white;
    padding: 0px;
    border-radius: 18px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
    overflow: hidden;
}

/* Card header */
.card-header {
    background: linear-gradient(90deg, #1c92d2, #1f4037);
    color: white;
    padding: 18px;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}

/* Card body */
.card-body {
    padding: 30px;
}

/* Title */
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #0f172a;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #334155;
    margin-bottom: 25px;
}

/* Pulse animation for failure */
.pulse {
    animation: pulse 1.5s infinite;
    color: red;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.08); }
    100% { transform: scale(1); }
}

/* Footer */
.footer {
    text-align: center;
    color: #1f2933;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- UI --------------------
st.markdown('<div class="title">⚙️ Machine Failure Prediction</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict machine health using real-time sensor inputs</div>',
    unsafe_allow_html=True
)

# ---------- CARD START ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

# Card header (FIXED)
st.markdown(
    '<div class="card-header">🔧 Enter Sensor Values</div>',
    unsafe_allow_html=True
)

# Card body
st.markdown('<div class="card-body">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("🌡 Temperature (°C)", min_value=0.0)
    vibration = st.number_input("📈 Vibration", min_value=0.0)

with col2:
    pressure = st.number_input("🧪 Pressure", min_value=0.0)
    rpm = st.number_input("⚙️ RPM", min_value=0.0)

st.markdown("<br>", unsafe_allow_html=True)

# Centered button
btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])
with btn_col2:
    predict = st.button("🚀 Predict Machine Status")

# Close card body & card
st.markdown('</div></div>', unsafe_allow_html=True)
# ---------- CARD END ----------

# -------------------- Prediction --------------------
if predict:
    with st.spinner("Analyzing machine health..."):
        time.sleep(1.5)

    X = np.array([[temperature, vibration, pressure, rpm]])
    prediction = model1.predict(X)

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction[0] == 1:
        st.markdown(
            '<div class="pulse">🚨 MACHINE FAILURE LIKELY!<br>Immediate maintenance required.</div>',
            unsafe_allow_html=True
        )
    else:
        st.success("✅ MACHINE IS SAFE! All systems running normally.")
        st.balloons()

# Footer
st.markdown("<br><hr><div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
