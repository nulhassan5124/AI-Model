import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw

# ================= PRO SETUP =================
st.set_page_config(
    page_title="Starbucks Calorie Predictor Pro",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .hero { background: linear-gradient(135deg, #006241 0%, #1E3932 100%); padding: 35px; border-radius: 20px; color: white; text-align: center; }
    .hero h1 { color: white; font-size: 42px; margin:0; font-weight: 800; }
    .hero p { color: #D4E9E2; font-size: 16px; margin-top: 8px; }
    .pro-card { background:white; padding: 25px; border-radius: 18px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border: 1px solid #EEF2F7; }
    .badge { background: #006241; color: white; padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; }
    .disclaimer { background: #FFF8E1; border-left: 5px solid #FFB300; padding: 12px; border-radius: 10px; font-size: 13px; }
    .footer { text-align:center; color: #95A5A6; font-size: 13px; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    return joblib.load('starbucks_decision_tree_model.joblib')

try:
    model = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"Model file missing. 'starbucks_decision_tree_model.joblib' ko app.py ke saath rakhen. Error: {e}")

# ================= PROFESSIONAL REPORT GENERATOR =================
def create_report_image(fat, carb, protein, est_cal, pred_label, conf, health_score):
    W, H = 1200, 900
    img = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,W,160], fill='#006241')
    draw.text((50,30), "STARBUCKS  |  Calorie Predictor Pro", fill='white')
    draw.text((50,75), "Smart Nutrition Analysis Report", fill='#D4E9E2')
    draw.text((50,110), f"Date: {datetime.now().strftime('%d %B %Y, %I:%M %p')}  |  Report ID: SB-{datetime.now().strftime('%Y%m%d')}-1042", fill='white')
    y=200
    draw.text((50,y), "NUTRITION SUMMARY", fill='#006241')
    y+=40
    draw.line([(50,y),(W-50,y)], fill='#E0E0E0', width=2)
    y+=30
    draw.text((50,y), f"Fat: {fat} g   |   Carbs: {carb} g   |   Protein: {protein} g", fill='black')
    y+=50
    draw.text((50,y), f"Estimated Calories: ~{est_cal} kcal  (Formula: Fat*9 + Carb*4 + Protein*4)", fill='black')
    y+=60
    draw.text((50,y), f"PREDICTION: {pred_label}", fill='#006241' if 'Low' in pred_label else '#C0392B')
    y+=45
    draw.text((50,y), f"Confidence: {conf:.1f}%  |  Health Score: {health_score}/100", fill='black')
    y+=60
    draw.rectangle([50,y, W-50, y+130], fill='#FFF8E1', outline='#FFB300')
    draw.text((70, y+15), "DISCLAIMER: This is AI prediction based on Decision Tree model.", fill='black')
    draw.text((70, y+45), "Actual calories may vary by size, milk, syrup & toppings.", fill='black')
    draw.text((70, y+75), "For accurate diet plan, consult a nutritionist.", fill='black')
    draw.text((50, H-50), "© 2026 Starbucks Predictor Pro | Developed by NulHassan | For Educational Purpose", fill='grey')
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## ☕ **Starbucks Pro**")
    st.markdown('<span class="badge">PRO v2.0</span>', unsafe_allow_html=True)
    st.write("")
    st.markdown("**Model:** Decision Tree Classifier")
    st.markdown("**Features:** Fat, Carbs, Protein")
    st.markdown("**Target:** High Calorie > 150 kcal")
    st.divider()
    st.markdown("### 📊 How It Works")
    st.write("1. Nutrition values dalen")
    st.write("2. AI Decision Tree analyze karega")
    st.write("3. Instant Calorie Category + Report")
    st.divider()
    st.markdown("### 👨‍💻 Developer")
    st.write("**NulHassan**")
    st.write("Lahore, Pakistan")
    if st.button("🔄 Reset"):
        st.rerun()

# ================= HERO =================
st.markdown("""
<div class="hero">
    <h1>☕ Starbucks Calorie Predictor Pro</h1>
    <p>Know Your Drink Before You Sip It | AI-Powered Nutrition Intelligence | Decision Tree Model</p>
</div>
""", unsafe_allow_html=True)
st.write("")

# ================= MAIN =================
col1, col2 = st.columns([1, 1.25], gap="large")

with col1:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.subheader("🥤 1. Enter Nutrition Details")
    st.write("Apne drink ke label se values select karen.")
    
    fat = st.slider("Fat (g)", 0.0, 30.0, 2.0, 0.5, help="Total Fat from nutrition label")
    carb = st.slider("Carbohydrates (g)", 0.0, 100.0, 25.0, 1.0, help="Total Carbs including sugar")
    protein = st.slider("Protein (g)", 0.0, 30.0, 4.0, 0.5, help="Total Protein")
    
    # Quick Presets
    st.write("**Quick Presets:**")
    p1, p2, p3 = st.columns(3)
    if p1.button("Black Coffee"):
        st.session_state['preset'] = (0.0, 0.0, 0.0)
    if p2.button("Latte"):
        st.session_state['preset'] = (7.0, 15.0, 8.0)
    if p3.button("Frappuccino"):
        st.session_state['preset'] = (8.0, 55.0, 5.0)
    
    # Live Estimated Calories
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.divider()
    st.metric("Estimated Calories (Formula)", f"{est_cal} kcal")
    st.progress(min(int(est_cal/300*100), 100))
    st.caption("Formula: Fat*9 + Carb*4 + Protein*4")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if model_loaded:
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)
        st.subheader("📊 2. AI Prediction Report")
        
        if st.button("🔍 Predict Calorie Category", type="primary", use_container_width=True):
            input_data = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            prediction = model.predict(input_data)[0]
            probs = model.predict_proba(input_data)[0]
            
            # Logic
            if prediction == 1:
                pred_label = "High Calorie (>150 kcal)"
                conf = probs[1]*100
                st.error(f"🚨 **Prediction: {pred_label}**")
                health_score = max(10, 100 - int(est_cal/3))
            else:
                pred_label = "Low / Med Calorie (<=150 kcal)"
                conf = probs[0]*100
                st.success(f"✅ **Prediction: {pred_label}**")
                health_score = min(95, 100 - int(est_cal/5))
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Confidence", f"{conf:.1f}%")
            m2.metric("Est. Calories", f"{est_cal} kcal")
            m3.metric("Health Score", f"{health_score}/100")
            
            st.write("**Confidence Meter**")
            st.progress(int(conf))
            
            st.write("**Nutrition Breakdown**")
            total_macro = fat + carb + protein if (fat+carb+protein)>0 else 1
            st.write(f"Fat: {fat}g - {fat/total_macro*100:.1f}%")
            st.progress(int(fat/total_macro*100))
            st.write(f"Carbs: {carb}g - {carb/total_macro*100:.1f}%")
            st.progress(int(carb/total_macro*100))
            st.write(f"Protein: {protein}g - {protein/total_macro*100:.1f}%")
            st.progress(int(protein/total_macro*100))
            
            # Smart Tip
            if prediction == 1:
                st.warning("💡 **Smart Tip:** Sugar-free syrup + Skim milk use karen, calories 40% tak kam ho jayengi.")
            else:
                st.info("💡 **Great Choice:** Ye drink aap ke daily goal ke liye safe hai. Enjoy!")
            
            # Report
            report_buf = create_report_image(fat, carb, protein, est_cal, pred_label, conf, health_score)
            st.divider()
            st.image(report_buf, caption="Professional Report Preview", use_container_width=True)
            st.download_button(
                "📄 Download Professional Report (PNG)",
                data=report_buf,
                file_name=f"Starbucks_Report_{datetime.now().strftime('%Y%m%d')}.png",
                mime="image/png",
                use_container_width=True,
                type="primary"
            )
            st.markdown("<div class='disclaimer'>⚠️ <b>Disclaimer:</b> Ye AI prediction hai, actual Starbucks calories size/milk/syrup se change ho sakti hain.</div>", unsafe_allow_html=True)
        else:
            st.info("👈 Left side se values select karen aur **Predict** button dabayen.")
            st.markdown("""
            ### Why Use This?
            ✅ **Instant:** 2 second me result  
            ✅ **Smart:** Decision Tree model trained on real Starbucks data  
            ✅ **Healthy Choices:** Health Score se pata chalta hai drink kitna healthy hai  
            ✅ **Shareable:** Professional report download kar ke doston ko bhejo
            """)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p class='footer'>© 2026 Starbucks Predictor Pro | Developed by NulHassan | Lahore, Pakistan | For Educational Purpose Only</p>", unsafe_allow_html=True)
