import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw
import math

# ================= PRO SETUP V3 =================
st.set_page_config(
    page_title="Starbucks Calorie Predictor Pro",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main { background-color: #F7F5F2; }
    
    .hero { 
        background: linear-gradient(135deg, #006241 0%, #1E3932 50%, #000000 100%); 
        padding: 45px 30px; border-radius: 24px; color: white; text-align: left; 
        display: flex; justify-content: space-between; align-items: center;
    }
    .hero h1 { color: white; font-size: 46px; margin:0; font-weight: 800; letter-spacing: -1px; }
    .hero p { color: #D4E9E2; font-size: 17px; margin-top: 10px; }
    .hero-right { background: rgba(255,255,255,0.12); padding: 15px 25px; border-radius: 15px; text-align: center; backdrop-filter: blur(10px); }
    
    .pro-card { 
        background:white; padding: 30px; border-radius: 20px; 
        box-shadow: 0 10px 35px rgba(0,0,0,0.05); border: 1px solid #EDEBE9; 
        transition: all 0.3s;
    }
    .pro-card:hover { box-shadow: 0 15px 45px rgba(0,0,0,0.08); }
    
    .metric-box { background: #F9F9F7; padding: 15px; border-radius: 12px; border: 1px solid #eee; text-align: center; }
    .stSlider > div > div > div > div { background-color: #006241 !important; }
    .footer { text-align:center; color: #A0A0A0; font-size: 13px; margin-top: 50px; padding-top: 20px; border-top: 1px solid #eee; }
</style>
""", unsafe_allow_html=True)

# ================= MODEL =================
@st.cache_resource
def load_model():
    return joblib.load('starbucks_decision_tree_model.joblib')

try:
    model = load_model()
    model_loaded = True
except:
    model_loaded = False
    st.error("Model file 'starbucks_decision_tree_model.joblib' missing. Please upload it with app.py")

# ================= GAUGE GENERATOR =================
def create_gauge_image(conf, label):
    W,H = 400,220
    img = Image.new('RGB', (W,H), 'white')
    draw = ImageDraw.Draw(img)
    # Background arc
    draw.arc([20,20,380,380], start=200, end=340, fill='#EDEBE9', width=18)
    # Fill arc based on conf
    angle = 200 + (140 * conf / 100)
    draw.arc([20,20,380,380], start=200, end=angle, fill='#006241' if 'Low' in label else '#C0392B', width=18)
    draw.text((W//2-40, 90), f"{conf:.0f}%", fill='black')
    draw.text((W//2-60, 120), label, fill='grey')
    buf=BytesIO(); img.save(buf, format='PNG'); buf.seek(0); return buf

# ================= SIDEBAR V3 =================
with st.sidebar:
    st.markdown("## ☕ **Starbucks**")
    st.markdown("#### Calorie Predictor")
    st.markdown('<span style="background:#006241;color:white;padding:5px 12px;border-radius:20px;font-size:12px;">PRO v3.0 • LIVE</span>', unsafe_allow_html=True)
    st.write("")
    st.markdown("**Model:** Decision Tree")
    st.markdown("**Accuracy:** 92% on Test Data")
    st.markdown("**Features:** 3 Macros")
    st.divider()
    st.markdown("### 🎯 Quick Presets")
    if st.button("☕ Black Coffee - 2 kcal", use_container_width=True):
        st.session_state.fat=0.0; st.session_state.carb=0.0; st.session_state.protein=0.3
    if st.button("🥛 Caffe Latte - 190 kcal", use_container_width=True):
        st.session_state.fat=7.0; st.session_state.carb=15.0; st.session_state.protein=12.0
    if st.button("🍫 Mocha Frappuccino - 370 kcal", use_container_width=True):
        st.session_state.fat=15.0; st.session_state.carb=54.0; st.session_state.protein=5.0
    if st.button("🍵 Matcha Latte - 200 kcal", use_container_width=True):
        st.session_state.fat=7.0; st.session_state.carb=26.0; st.session_state.protein=8.0
    st.divider()
    st.caption("Developed by NulHassan\nLahore, Pakistan 🇵🇰")

# ================= HERO V3 =================
st.markdown("""
<div class="hero">
    <div>
        <h1>☕ Starbucks<br>Calorie Predictor Pro</h1>
        <p>Know Your Drink Before You Sip It | AI-Powered Nutrition Intelligence<br>Trained on Real Starbucks Nutritional Data</p>
    </div>
    <div class="hero-right">
        <div style="font-size:32px;">🤖</div>
        <div style="font-size:14px; font-weight:600;">AI Model: Active</div>
        <div style="font-size:12px; color:#D4E9E2;">Decision Tree • Ready</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ================= MAIN DASHBOARD =================
col1, col2 = st.columns([1, 1.35], gap="large")

with col1:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.markdown("### 🥤 1. Enter Nutrition")
    st.caption("Label se values dalen. Hamara AI baqi khud karega.")
    
    # Use session state for presets
    fat = st.slider("Fat (g) - Charbi", 0.0, 30.0, st.session_state.get('fat', 2.0), 0.5)
    carb = st.slider("Carbohydrates (g) - Meetha", 0.0, 100.0, st.session_state.get('carb', 25.0), 1.0)
    protein = st.slider("Protein (g) - Taqat", 0.0, 30.0, st.session_state.get('protein', 4.0), 0.5)
    
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.divider()
    c1,c2 = st.columns(2)
    c1.metric("Estimated Calories", f"{est_cal} kcal", delta=f"{'High' if est_cal>150 else 'Low'}", delta_color="inverse")
    c2.metric("Daily Value %", f"{est_cal/2000*100:.1f}%", "of 2000 kcal")
    
    # Visual Macros
    st.write("**Macro Breakdown**")
    total = fat+carb+protein if (fat+carb+protein)>0 else 1
    st.write(f"🥑 Fat {fat/total*100:.0f}% | 🍞 Carbs {carb/total*100:.0f}% | 🥚 Protein {protein/total*100:.0f}%")
    st.progress(int(fat/total*100))
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    if model_loaded:
        st.markdown("### 📊 2. AI Prediction Dashboard")
        
        if st.button("🚀 ANALYZE DRINK NOW - Predict", type="primary", use_container_width=True):
            input_df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0]
            
            if pred == 1:
                label = "High Calorie"
                conf = prob[1]*100
                st.markdown(f"""
                <div style="background:#FDEDEC; border:1px solid #F5B7B1; padding:20px; border-radius:15px;">
                    <h2 style="color:#C0392B; margin:0;">🚨 High Calorie - {est_cal} kcal</h2>
                    <p style="margin:5px 0 0 0; color:#922B21;">This drink is above 150 kcal. Consider low-fat milk / less syrup.</p>
                </div>
                """, unsafe_allow_html=True)
                tip = "💡 Pro Tip: 'Non-fat milk + Sugar-free syrup' se 80 kcal tak kam ho sakta hai. Barista se 'Light' bolen."
                health = max(20, 100 - int(est_cal/2.5))
            else:
                label = "Low / Med Calorie"
                conf = prob[0]*100
                st.markdown(f"""
                <div style="background:#EAFAF1; border:1px solid #A9DFBF; padding:20px; border-radius:15px;">
                    <h2 style="color:#1E8449; margin:0;">✅ Low Calorie - {est_cal} kcal</h2>
                    <p style="margin:5px 0 0 0; color:#1E8449;">Great choice! This drink fits your healthy lifestyle.</p>
                </div>
                """, unsafe_allow_html=True)
                tip = "💡 You are on track! Isi tarah healthy choices karte rahen."
                health = min(95, 100 - int(est_cal/6))

            st.write("")
            m1,m2,m3 = st.columns(3)
            m1.markdown(f"<div class='metric-box'><b>Confidence</b><br><span style='font-size:22px; font-weight:800;'>{conf:.1f}%</span></div>", unsafe_allow_html=True)
            m2.markdown(f"<div class='metric-box'><b>Health Score</b><br><span style='font-size:22px; font-weight:800;'>{health}/100</span></div>", unsafe_allow_html=True)
            m3.markdown(f"<div class='metric-box'><b>Category</b><br><span style='font-size:14px; font-weight:600;'>{label}</span></div>", unsafe_allow_html=True)
            
            st.write("")
            st.info(tip)
            
            # Downloadable Professional Report
            report_text = f"""Starbucks Calorie Predictor Pro - Report

Date: {datetime.now().strftime('%d %B %Y')}
Nutrition: Fat={fat}g, Carb={carb}g, Protein={protein}g
Estimated Calories: {est_cal} kcal
AI Prediction: {label} (Confidence {conf:.1f}%)
Health Score: {health}/100

Tip: {tip}

Disclaimer: AI prediction, actual may vary.
Developed by NulHassan
"""
            st.download_button("📄 Download Pro Report (TXT)", report_text, file_name="Starbucks_Pro_Report.txt", use_container_width=True)
            
        else:
            st.markdown("""
            <div style="background:#F9F9F7; padding:40px; border-radius:15px; text-align:center; border:2px dashed #E5E8E8;">
                <div style="font-size:50px;">☕</div>
                <h3>Ready to Analyze</h3>
                <p style="color:grey;">Left side se nutrition dalen aur <b>Analyze</b> dabayen.<br>AI aap ko instant report dega.</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            #### Why This Pro Version?
            - **Instant:** 1 sec me result, no waiting
            - **Accurate:** 92% accuracy on real Starbucks data
            - **Smart Tips:** AI aap ko healthier alternative batayega
            - **Health Score:** 0-100 tak score, samajhna asan
            """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2026 Starbucks Predictor Pro v3.0 | Crafted with ❤️ by NulHassan | Lahore, Pakistan | Not affiliated with Starbucks Corp. | For Educational Use</div>", unsafe_allow_html=True)
