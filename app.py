import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import plotly.graph_objects as go

# ================= V5 BLACK & WHITE LUXURY =================
st.set_page_config(
    page_title="Starbucks Calorie Predictor — Black Edition",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #FFFFFF; }
    section[data-testid="stSidebar"] { background-color: #000000 !important; }
    section[data-testid="stSidebar"] * { color: #FFFFFF !important; }
    section[data-testid="stSidebar"] button { background-color: #1A1A1A !important; color: white !important; border: 1px solid #333 !important; }
    section[data-testid="stSidebar"] button:hover { background-color: #FFFFFF !important; color: #000000 !important; }

    /* HERO BLACK */
    .hero-bw {
        background: #000000;
        padding: 50px 50px;
        border-radius: 0px;
        color: white;
        border-bottom: 5px solid #000;
    }
    .hero-bw h1 { color: white; font-size: 52px; font-weight: 900; margin: 0; line-height: 1.0; letter-spacing: -1.5px; text-transform: uppercase; }
    .hero-bw p { color: #B0B0B0; font-size: 15px; margin-top: 14px; max-width: 600px; line-height: 1.6; }
    .hero-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; }
    .hero-badge { border: 1px solid white; padding: 6px 14px; font-size: 11px; letter-spacing: 2px; font-weight: 700; }
    .hero-num { font-size: 11px; letter-spacing: 2px; color: #B0B0B0; }

    /* CARDS B&W */
    .card-bw {
        background: #FFFFFF;
        padding: 34px;
        border: 1.5px solid #000000;
        border-radius: 0px;
        height: 100%;
    }
    .card-bw:hover { box-shadow: 8px 8px 0px #000000; transition: 0.2s; }
    .card-title { font-size: 13px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; color: #000; margin-bottom: 5px; }
    .card-sub { font-size: 13px; color: #777; margin-bottom: 22px; }

    /* METRIC B&W */
    .metric-bw { border: 1.5px solid #000; padding: 16px; background: #FFF; }
    .metric-bw b { font-size: 10px; letter-spacing: 2px; color: #777; }
    .metric-bw span { font-size: 28px; font-weight: 900; color: #000; display: block; margin-top: 2px; }

    /* BUTTONS */
    .stButton > button { background-color: #000000 !important; color: #FFFFFF !important; border-radius: 0px !important; border: 1.5px solid #000 !important; font-weight: 800 !important; letter-spacing: 1px !important; text-transform: uppercase !important; padding: 12px !important; }
    .stButton > button:hover { background-color: #FFFFFF !important; color: #000000 !important; }

    /* SLIDERS B&W */
    .stSlider > div > div > div > div { background-color: #000000 !important; }

    .footer-bw { text-align: center; color: #999; font-size: 11px; letter-spacing: 1.5px; margin-top: 60px; padding-top: 20px; border-top: 1.5px solid #000; text-transform: uppercase; }
    .divider-bw { border-top: 1.5px solid #000; margin: 20px 0; }
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

# ================= GAUGE B&W =================
def gauge_bw(conf, label):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=conf,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': label.upper(), 'font': {'size': 14, 'color': '#000', 'family': 'Inter'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#000"},
            'bar': {'color': "#000000", 'thickness': 0.25},
            'bgcolor': "white",
            'borderwidth': 1.5,
            'bordercolor': "#000000",
            'steps': [{'range': [0, 50], 'color': '#F2F2F2'}, {'range': [50, 100], 'color': '#E5E5E5'}],
            'threshold': {'line': {'color': "#000", 'width': 4}, 'thickness': 0.8, 'value': conf}
        }
    ))
    fig.update_layout(height=230, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor="white", font={'family': "Inter"})
    return fig

# ================= SIDEBAR BLACK =================
with st.sidebar:
    st.markdown("# ☕ STARBUCKS")
    st.markdown("**CALORIE PREDICTOR**")
    st.markdown("`BLACK EDITION • V5.0`")
    st.markdown("---")
    st.markdown("### PRESETS — REAL MENU")
    if st.button("01  BLACK COFFEE — 5 KCAL", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 0.1, 0.0, 0.3
    if st.button("02  CAFFE LATTE — 190 KCAL", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 7.0, 15.0, 12.0
    if st.button("03  CARAMEL FRAPPUCCINO — 370 KCAL", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 15.0, 54.0, 5.0
    if st.button("04  STRAWBERRY AÇAI — 90 KCAL", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 0.1, 22.0, 0.0
    st.markdown("---")
    st.markdown("**MODEL**")
    st.caption("Decision Tree Classifier")
    st.caption("Accuracy: 94.2% • Features: 3")
    st.caption("Dataset: Starbucks USA Menu")
    st.markdown("---")
    st.caption("NULHASSAN — LAHORE, PK")
    st.caption("© 2026 • BLACK EDITION")

# ================= HERO BLACK =================
st.markdown("""
<div class="hero-bw">
    <div class="hero-top">
        <div class="hero-badge">● AI NUTRITION LAB — PRO</div>
        <div class="hero-num">EST. 2026 / LAHORE — PK</div>
    </div>
    <h1>Know Your Drink.<br>Before You Sip It.</h1>
    <p>Minimal. Precise. Honest. Our Black Edition AI reads Fat, Carbs & Protein and tells you in 1 second if your drink is High Calorie (>150 kcal) or not. No colors. No distraction. Just truth.</p>
</div>
""", unsafe_allow_html=True)
st.write("")
st.write("")

# ================= DASHBOARD B&W =================
c1, c2 = st.columns([1, 1.35], gap="large")

with c1:
    st.markdown('<div class="card-bw">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">01 — Drink Composition</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-sub">Enter values from nutrition label. Black Edition will do the rest.</div>', unsafe_allow_html=True)
    
    fat = st.slider("FAT — (g)", 0.0, 30.0, st.session_state.get('fat', 2.0), 0.5)
    carb = st.slider("CARBS — (g)", 0.0, 100.0, st.session_state.get('carb', 25.0), 1.0)
    protein = st.slider("PROTEIN — (g)", 0.0, 30.0, st.session_state.get('protein', 4.0), 0.5)
    
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.markdown('<div class="divider-bw"></div>', unsafe_allow_html=True)
    
    m1, m2 = st.columns(2)
    with m1:
        st.markdown(f"<div class='metric-bw'><b>EST. CALORIES</b><span>{est_cal} KCAL</span></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-bw'><b>DAILY VALUE</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    
    st.write("")
    total = fat+carb+protein if (fat+carb+protein)>0 else 1
    st.write(f"**MACRO SPLIT:** FAT {fat/total*100:.0f}%  /  CARBS {carb/total*100:.0f}%  /  PROTEIN {protein/total*100:.0f}%")
    st.progress(int((fat+carb+protein)/160*100))
    st.caption(f"TOTAL MACROS: {fat+carb+protein:.1f}g  |  FORMULA: F*9 + C*4 + P*4")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card-bw">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">02 — AI Intelligence Report</div>', unsafe_allow_html=True)
    
    if not model_loaded:
        st.error("Model file missing.")
    else:
        if st.button("ANALYZE DRINK → GET PRO REPORT", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            
            if pred == 1:
                label = "High Calorie"
                conf = prob[1]*100
                health = max(15, 100 - int(est_cal/2.2))
                st.markdown(f"""
                <div style="background:#000; color:white; padding:24px; border:1.5px solid #000;">
                    <span style="border:1px solid white; padding:4px 10px; font-size:10px; letter-spacing:2px;">⚠ HIGH CALORIE ALERT</span>
                    <h2 style="color:white; margin:12px 0 0 0; font-size:28px; font-weight:900;">{est_cal} KCAL — {label.upper()}</h2>
                    <p style="color:#B0B0B0; font-size:13px; margin:6px 0 0 0;">Exceeds 150 kcal limit. Recommended for occasional consumption only.</p>
                </div>
                """, unsafe_allow_html=True)
                tip = f"<div style='border:1.5px solid #000; padding:14px; font-size:13px;'><b>SMART SWAP:</b> Non-fat milk + Sugar-free Vanilla + No Whip. Saves ~{int(est_cal*0.4)} kcal. Ask barista for 'LIGHT' version.</div>"
            else:
                label = "Low / Med Calorie"
                conf = prob[0]*100
                health = min(96, 100 - int(est_cal/5))
                st.markdown(f"""
                <div style="background:#FFF; color:#000; padding:24px; border:1.5px solid #000;">
                    <span style="background:#000; color:white; padding:4px 10px; font-size:10px; letter-spacing:2px;">✓ HEALTHY CHOICE</span>
                    <h2 style="color:#000; margin:12px 0 0 0; font-size:28px; font-weight:900;">{est_cal} KCAL — {label.upper()}</h2>
                    <p style="color:#777; font-size:13px; margin:6px 0 0 0;">Perfect. Under your 150 kcal goal. Enjoy guilt-free.</p>
                </div>
                """, unsafe_allow_html=True)
                tip = f"<div style='border:1.5px solid #000; padding:14px; font-size:13px;'><b>EXCELLENT:</b> Ye choice bilkul sahi hai. Aap apne daily goal ke andar hain. Keep it up.</div>"

            st.write("")
            col_a, col_b = st.columns([1.2, 1])
            with col_a:
                st.plotly_chart(gauge_bw(conf, label), use_container_width=True, config={'displayModeBar': False})
            with col_b:
                st.write("")
                st.markdown(f"<div class='metric-bw'><b>HEALTH SCORE</b><span>{health} / 100</span></div>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"<div class='metric-bw'><b>CONFIDENCE</b><span>{conf:.1f}%</span></div>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"<div class='metric-bw'><b>CATEGORY</b><span style='font-size:15px;'>{label}</span></div>", unsafe_allow_html=True)
            
            st.write("")
            st.markdown(tip, unsafe_allow_html=True)
            
            report = f"""STARBUCKS - BLACK EDITION REPORT
Generated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}

Fat: {fat}g | Carbs: {carb}g | Protein: {protein}g
Estimated Calories: {est_cal} kcal
AI Prediction: {label} | Confidence: {conf:.1f}%
Health Score: {health}/100
Model: Decision Tree

Developed by NulHassan | Lahore, Pakistan
"""
            st.write("")
            st.download_button("DOWNLOAD OFFICIAL REPORT ↓", report, file_name=f"Starbucks_Black_Report_{datetime.now().strftime('%Y%m%d')}.txt", use_container_width=True)
            
        else:
            st.markdown("""
            <div style="border:1.5px dashed #000; padding:50px; text-align:center; background:#FAFAFA;">
                <div style="font-size:50px;">☕</div>
                <div style="font-weight:900; font-size:18px; letter-spacing:1px;">READY TO ANALYZE</div>
                <div style="font-size:13px; color:#777; margin-top:8px;">Left se macros set karen ya sidebar se preset select karen.<br>Phir <b>ANALYZE</b> dabayen. 1 second me report milegi.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **WHY BLACK EDITION?**
            - **Luxury Minimal:** Sirf Black & White. No distraction.
            - **Agency Look:** Dribbble / Awwwards award-winning style.
            - **Gauge Meter:** Real-time confidence.
            - **Smart Swaps:** AI khud calories kam karne ka tarika batayega.
            """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='footer-bw'>© 2026 — STARBUCKS AI LAB • BLACK EDITION • CRAFTED BY NULHASSAN • LAHORE, PAKISTAN • NOT AFFILIATED WITH STARBUCKS CORP.</div>", unsafe_allow_html=True)import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import plotly.graph_objects as go

# ================= V4 ULTRA PRO CONFIG =================
st.set_page_config(
    page_title="Starbucks Calorie Predictor Pro | AI Nutrition Lab",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= V4 ULTRA PRO CSS =================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #F6F1EB; }
    
    /* HERO - STARBUCKS ORIGINAL */
    .hero-v4 {
        background: #1E3932;
        padding: 40px 45px;
        border-radius: 28px;
        color: white;
        position: relative;
        overflow: hidden;
        border: 1px solid #2D4A42;
    }
    .hero-v4::after {
        content: "☕";
        position: absolute;
        right: 30px;
        top: 10px;
        font-size: 140px;
        opacity: 0.07;
    }
    .hero-v4 h1 { color: white; font-size: 48px; font-weight: 800; margin: 0; line-height: 1.1; }
    .hero-v4 p { color: #B0D5C8; font-size: 16px; margin-top: 12px; max-width: 650px; }
    .hero-badge { display: inline-block; background: #00704A; color: white; padding: 6px 14px; border-radius: 100px; font-size: 12px; font-weight: 700; margin-bottom: 12px; letter-spacing: 0.5px; }
    
    /* PRO CARDS */
    .card-v4 {
        background: #FFFFFF;
        padding: 32px;
        border-radius: 22px;
        box-shadow: 0 12px 40px rgba(30, 57, 50, 0.06);
        border: 1px solid #EDE5D8;
        height: 100%;
    }
    .card-title { font-size: 20px; font-weight: 800; color: #1E3932; margin-bottom: 6px; }
    .card-sub { font-size: 13px; color: #8A8A8A; margin-bottom: 20px; }
    
    /* METRICS */
    .metric-v4 { background: #F9F5F0; border: 1px solid #EDE5D8; padding: 16px; border-radius: 14px; text-align: left; }
    .metric-v4 b { font-size: 12px; color: #8A8A8A; text-transform: uppercase; letter-spacing: 0.5px; }
    .metric-v4 span { font-size: 24px; font-weight: 800; color: #1E3932; display: block; margin-top: 4px; }
    
    /* TIPS */
    .tip-high { background: #FFF1F0; border-left: 4px solid #D5002B; padding: 14px 18px; border-radius: 10px; color: #7A1F1F; font-size: 13px; }
    .tip-low { background: #E8F5E9; border-left: 4px solid #00704A; padding: 14px 18px; border-radius: 10px; color: #1E3932; font-size: 13px; }
    
    .footer-v4 { text-align: center; color: #A99E93; font-size: 12px; margin-top: 50px; padding: 20px; border-top: 1px solid #EDE5D8; }
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

# ================= GAUGE WITH PLOTLY - REAL PRO FEATURE =================
def gauge_chart(confidence, label):
    color = "#00704A" if "Low" in label else "#D5002B"
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': label, 'font': {'size': 16, 'color': '#1E3932'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#EDE5D8"},
            'bar': {'color': color, 'thickness': 0.3},
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
                {'range': [0, 50], 'color': '#F9F5F0'},
                {'range': [50, 100], 'color': '#F0EDE8'}],
            'threshold': {'line': {'color': color, 'width': 4}, 'thickness': 0.8, 'value': confidence}
        }
    ))
    fig.update_layout(height=220, margin=dict(l=20,r=20,t=50,b=20), paper_bgcolor="white", font={'family': "Plus Jakarta Sans"})
    return fig

# ================= SIDEBAR V4 =================
with st.sidebar:
    st.markdown("### ☕ Starbucks AI Lab")
    st.markdown("**Calorie Predictor Pro v4.0**")
    st.markdown('<span style="background:#1E3932;color:#B0D5C8;padding:6px 12px;border-radius:20px;font-size:11px;">● LIVE • MODEL READY</span>', unsafe_allow_html=True)
    st.divider()
    st.markdown("#### ⚡ Quick Presets (Real Menu)")
    if st.button("Tall Black Coffee - 5 kcal", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 0.1, 0.0, 0.3
    if st.button("Grande Caffe Latte - 190 kcal", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 7.0, 15.0, 12.0
    if st.button("Venti Caramel Frappuccino - 370 kcal", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 15.0, 54.0, 5.0
    if st.button("Strawberry Açaí Refresher - 90 kcal", use_container_width=True):
        st.session_state.fat, st.session_state.carb, st.session_state.protein = 0.1, 22.0, 0.0
    st.divider()
    st.markdown("**Model Info**")
    st.caption("Decision Tree • 3 Features • Trained on Starbucks USA Menu 2024 • Accuracy 94.2%")
    st.divider()
    st.caption("👨‍💻 NulHassan | Lahore, PK | v4.0")

# ================= HERO V4 =================
st.markdown("""
<div class="hero-v4">
    <div class="hero-badge">● STARBUCKS AI NUTRITION LAB • PRO EDITION</div>
    <h1>Know Your Drink<br>Before You Sip It.</h1>
    <p>Our AI analyzes Fat, Carbs & Protein to predict if your drink is High Calorie (>150 kcal). Get Health Score, Smart Swaps & Professional Report instantly. Built for health-conscious coffee lovers.</p>
</div>
""", unsafe_allow_html=True)
st.write("")

# ================= DASHBOARD V4 =================
c1, c2 = st.columns([1, 1.4], gap="large")

with c1:
    st.markdown('<div class="card-v4">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🥤 1. Drink Composition</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-sub">Enter values from nutrition label or use presets from sidebar.</div>', unsafe_allow_html=True)
    
    fat = st.slider("Fat (g)", 0.0, 30.0, st.session_state.get('fat', 2.0), 0.5)
    carb = st.slider("Carbs (g)", 0.0, 100.0, st.session_state.get('carb', 25.0), 1.0)
    protein = st.slider("Protein (g)", 0.0, 30.0, st.session_state.get('protein', 4.0), 0.5)
    
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.divider()
    
    m1, m2 = st.columns(2)
    with m1:
        st.markdown(f"<div class='metric-v4'><b>EST. CALORIES</b><span>{est_cal} kcal</span></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-v4'><b>DAILY VALUE</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    
    st.write("")
    st.write(f"**Macro Split:** Fat {fat/(fat+carb+protein+0.01)*100:.0f}% • Carbs {carb/(fat+carb+protein+0.01)*100:.0f}% • Protein {protein/(fat+carb+protein+0.01)*100:.0f}%")
    st.progress(int((fat+carb+protein)/160*100))
    st.caption(f"Total Macros: {fat+carb+protein:.1f}g")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card-v4">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📊 2. AI Intelligence Report</div>', unsafe_allow_html=True)
    
    if not model_loaded:
        st.error("Model file missing. 'starbucks_decision_tree_model.joblib' upload karen.")
    else:
        if st.button("🚀 ANALYZE DRINK - GET PRO REPORT", type="primary", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            
            if pred == 1:
                label = "High Calorie"
                conf = prob[1]*100
                st.markdown(f"""
                <div style="background:#1E3932; padding:20px; border-radius:14px; color:white;">
                    <span style="background:#D5002B; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:700;">HIGH CALORIE ALERT</span>
                    <h2 style="margin:10px 0 0 0; color:white;">{est_cal} kcal • {label}</h2>
                    <p style="margin:5px 0 0 0; color:#B0D5C8; font-size:13px;">This drink exceeds 150 kcal limit. Recommended for occasional consumption.</p>
                </div>
                """, unsafe_allow_html=True)
                health = max(15, 100 - int(est_cal/2.2))
                tip_text = f"<div class='tip-high'><b>💡 Smart Swap:</b> Ask for <b>Non-fat milk + Sugar-free Vanilla + No Whip</b>. Saves ~{int(est_cal*0.4)} kcal instantly. Ask barista for 'Light' version.</div>"
            else:
                label = "Low / Med Calorie"
                conf = prob[0]*100
                st.markdown(f"""
                <div style="background:#00704A; padding:20px; border-radius:14px; color:white;">
                    <span style="background:white; color:#00704A; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:700;">HEALTHY CHOICE</span>
                    <h2 style="margin:10px 0 0 0; color:white;">{est_cal} kcal • {label}</h2>
                    <p style="margin:5px 0 0 0; color:#D4E9E2; font-size:13px;">Perfect! This drink is under your 150 kcal goal. Enjoy guilt-free.</p>
                </div>
                """, unsafe_allow_html=True)
                health = min(96, 100 - int(est_cal/5))
                tip_text = f"<div class='tip-low'><b>✅ Excellent:</b> Ye choice bilkul sahi hai. Aap daily 2000 kcal goal ke andar hain. Keep it up!</div>"

            st.write("")
            col_a, col_b = st.columns([1.2, 1])
            with col_a:
                st.plotly_chart(gauge_chart(conf, label), use_container_width=True, config={'displayModeBar': False})
            with col_b:
                st.write("")
                st.markdown(f"<div class='metric-v4'><b>HEALTH SCORE</b><span>{health} / 100</span></div>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"<div class='metric-v4'><b>CONFIDENCE</b><span>{conf:.1f}%</span></div>", unsafe_allow_html=True)
                st.write("")
                st.markdown(f"<div class='metric-v4'><b>CATEGORY</b><span style='font-size:16px;'>{label}</span></div>", unsafe_allow_html=True)

            st.write("")
            st.markdown(tip_text, unsafe_allow_html=True)
            
            # Professional Text Report
            report = f"""STARBUCKS CALORIE PREDICTOR PRO - OFFICIAL REPORT
Generated: {datetime.now().strftime('%d %B %Y, %I:%M %p')}

NUTRITION INPUT:
Fat: {fat} g | Carbs: {carb} g | Protein: {protein} g
Estimated Calories: {est_cal} kcal (Formula: F*9+C*4+P*4)

AI RESULT:
Prediction: {label}
Confidence: {conf:.1f}%
Health Score: {health}/100
Model: Decision Tree (Starbucks Menu 2024)

Recommendation: {tip_text}

Developed by NulHassan | Lahore, Pakistan
For educational purpose only.
"""
            st.write("")
            st.download_button("📄 Download Official Pro Report", report, file_name=f"Starbucks_Pro_Report_{datetime.now().strftime('%Y%m%d')}.txt", use_container_width=True, type="primary")
            
        else:
            st.markdown("""
            <div style="background:#F9F5F0; border:2px dashed #EDE5D8; padding:45px; border-radius:18px; text-align:center;">
                <div style="font-size:48px; margin-bottom:10px;">☕</div>
                <div style="font-weight:800; font-size:18px; color:#1E3932;">Ready to Analyze Your Drink</div>
                <div style="font-size:13px; color:#8A8A8A; margin-top:6px;">Left se macros set karen, presets use karen, phir <b>ANALYZE</b> dabayen.<br>AI aap ko 1 second me professional report dega.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **Why Pro Version is Different:**
            - **Gauge Meter:** Real-time confidence visualization
            - **Health Score:** 0-100 score for quick decision
            - **Smart Swaps:** AI suggests how to reduce calories
            - **Agency Design:** Built with Starbucks original #1E3932 palette
            """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='footer-v4'>© 2026 Starbucks AI Lab Pro v4.0 | Crafted by NulHassan | Lahore, Pakistan 🇵🇰 | Not affiliated with Starbucks Corporation. Built for Portfolio & Educational Demo.</div>", unsafe_allow_html=True)import streamlit as st
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
