import streamlit as st
import pandas as pd
import joblib

# ---------- PAGE SETUP - LIGHT THEME ----------
st.set_page_config(page_title="Starbucks Calorie Predictor", page_icon="☕", layout="centered")

# ---------- SESSION STATE FIX ----------
if "fat" not in st.session_state:
    st.session_state.fat = 2.0
    st.session_state.carb = 25.0
    st.session_state.protein = 4.0

def set_preset(f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

# ---------- CSS - EXACT LIKE YOUR REFERENCE IMAGE ----------
st.markdown("""
<style>
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 750px; padding-top: 2rem; }
    
    /* Center Logo */
    .logo-container { text-align: center; margin-bottom: 10px; }
    .logo-circle {
        width: 85px; height: 85px; background: #00704A; border-radius: 50%;
        display: inline-flex; align-items: center; justify-content: center;
        color: white; font-size: 50px; font-weight: 900; font-family: serif;
        border: 4px solid #E8F0E8;
    }
    .logo-text { font-size: 10px; letter-spacing: 3px; color: #00704A; font-weight: 700; margin-top: 6px; }
    .main-title { text-align: center; font-size: 28px; font-weight: 800; color: #1E3932; margin: 12px 0 0 0; }
    .main-sub { text-align: center; font-size: 13px; color: #777; margin-top: 6px; line-height: 1.5; }
    .badge-center {
        text-align: center; margin-top: 12px;
    }
    .badge-center span {
        background: #E8F5E9; color: #00704A; padding: 5px 12px; border-radius: 20px;
        font-size: 10px; font-weight: 700; letter-spacing: 1px;
    }
    
    /* Tabs */
    .tabs { display: flex; justify-content: center; gap: 15px; margin-top: 25px; margin-bottom: 10px; border-bottom: 1px solid #EEE; padding-bottom: 10px; }
    .tab-active { font-weight: 700; color: #000; border-bottom: 2px solid #000; padding-bottom: 4px; font-size: 13px; }
    .tab-inactive { color: #999; font-size: 13px; }
    
    /* Example Drinks Card */
    .example-card {
        background: #FAFAFA; border: 1px solid #EEE; border-radius: 12px;
        padding: 20px; margin-top: 15px;
    }
    
    /* Buttons Green */
    .stButton > button {
        background: #00704A !important; color: white !important;
        border-radius: 8px !important; border: none !important;
        font-weight: 600 !important; font-size: 13px !important;
        height: 38px !important;
    }
    .stButton > button:hover { background: #1E3932 !important; }
    
    /* Reset Button White */
    div[data-testid="column"]:has(button[kind="secondary"]) button {
        background: white !important; color: #00704A !important; border: 1px solid #00704A !important;
    }
    
    /* Metrics */
    .metric-box {
        background: #F9F9F9; border: 1px solid #EEE; border-radius: 10px;
        padding: 14px; text-align: left;
    }
    .metric-box b { font-size: 11px; color: #999; }
    .metric-box span { font-size: 20px; font-weight: 800; color: #1E3932; display: block; }
    
    .stSlider > div > div > div > div { background: #00704A !important; }
</style>
""", unsafe_allow_html=True)

# ---------- MODEL ----------
@st.cache_resource
def load_model():
    return joblib.load('starbucks_decision_tree_model.joblib')

try:
    model = load_model()
    model_ok = True
except:
    model_ok = False

# ---------- HEADER - LIKE REFERENCE IMAGE ----------
st.markdown("""
<div class="logo-container">
    <div class="logo-circle">S</div>
    <div class="logo-text">STARBUCKS</div>
</div>
<h1 class="main-title">Drink Calorie Predictor</h1>
<p class="main-sub">Check if your favourite Starbucks drink is<br>High Calorie or Low / Medium Calorie</p>
<div class="badge-center"><span>● MACHINE LEARNING • DECISION TREE</span></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tabs">
    <span class="tab-active">● Predict Calories</span>
    <span class="tab-inactive">Starbucks Menu</span>
</div>
""", unsafe_allow_html=True)

# ---------- TRY EXAMPLE DRINKS - SAME AS REFERENCE ----------
st.markdown("""
<div class="example-card">
    <div style="font-weight:700; font-size:15px; color:#000;">⚡ Try Example Drinks</div>
    <div style="font-size:12px; color:#888; margin-top:3px; margin-bottom:15px;">One click - values will set automatically</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("☕ Black Coffee", use_container_width=True):
        set_preset(0.1, 0.0, 0.3); st.rerun()
with c2:
    if st.button("🥛 Skinny Latte", use_container_width=True):
        set_preset(0.2, 12.0, 10.0); st.rerun()
with c3:
    if st.button("🍫 Frappuccino", use_container_width=True):
        set_preset(15.0, 54.0, 5.0); st.rerun()

# ---------- SLIDERS - LIKE YOUR SECOND IMAGE ----------
st.write("")
st.markdown("#### Adjust Nutrition Values")
st.caption("Formula used: Fat×9 + Carb×4 + Protein×4 kcal")

fat = st.slider("Fat (g)", 0.0, 30.0, key="fat", step=0.5)
carb = st.slider("Carbs (g)", 0.0, 100.0, key="carb", step=1.0)
protein = st.slider("Protein (g)", 0.0, 30.0, key="protein", step=0.5)

est_cal = int(fat*9 + carb*4 + protein*4)

# Metrics row like image 2
st.write("")
col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.markdown(f"<div class='metric-box'><b>Fat</b><span>{fat:.1f}g</span></div>", unsafe_allow_html=True)
with col_b:
    st.markdown(f"<div class='metric-box'><b>Carbs</b><span>{carb:.1f}g</span></div>", unsafe_allow_html=True)
with col_c:
    st.markdown(f"<div class='metric-box'><b>Protein</b><span>{protein:.1f}g</span></div>", unsafe_allow_html=True)
with col_d:
    st.markdown(f"<div class='metric-box'><b>Est. Kcal</b><span>{est_cal}</span></div>", unsafe_allow_html=True)

st.write("")
b1, b2 = st.columns([1, 1])
with b1:
    if st.button("🔄 Reset All", use_container_width=True, type="secondary"):
        set_preset(2.0, 25.0, 4.0); st.rerun()
with b2:
    predict_clicked = st.button("🔍 Predict Calorie Category →", use_container_width=True, type="primary")

# ---------- PREDICTION RESULT ----------
if predict_clicked:
    if not model_ok:
        st.error("Model file 'starbucks_decision_tree_model.joblib' nahi mil rahi.")
    else:
        df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0]
        
        st.write("")
        if pred == 1:
            st.markdown(f"""
            <div style="background:#FDECEC; border:1px solid #F5C6C6; padding:18px; border-radius:12px;">
                <h3 style="color:#B42318; margin:0;">🚨 High Calorie — {est_cal} kcal</h3>
                <p style="color:#7A271A; font-size:13px; margin:5px 0 0 0;">Ye drink 150 kcal se zyada hai. Low-fat milk try karen.</p>
            </div>
            """, unsafe_allow_html=True)
            conf = prob[1]*100
            tip = f"**Tip:** Non-fat milk + Sugar-free syrup se {int(est_cal*0.4)} kcal kam hoga."
        else:
            st.markdown(f"""
            <div style="background:#E8F5E9; border:1px solid #A5D6A7; padding:18px; border-radius:12px;">
                <h3 style="color:#1E8449; margin:0;">✅ Low / Medium Calorie — {est_cal} kcal</h3>
                <p style="color:#1E8449; font-size:13px; margin:5px 0 0 0;">Perfect choice! Ye 150 kcal se kam hai.</p>
            </div>
            """, unsafe_allow_html=True)
            conf = prob[0]*100
            tip = "**Excellent:** Aap daily goal ke andar hain!"
        
        st.write("")
        m1, m2 = st.columns(2)
        m1.metric("Confidence", f"{conf:.1f}%")
        m2.metric("Health Score", f"{max(20, 100-int(est_cal/2))}/100")
        st.info(tip)

st.markdown("<p style='text-align:center; color:#AAA; font-size:11px; margin-top:50px; border-top:1px solid #EEE; padding-top:15px;'>© 2026 Starbucks Predictor | Crafted by NulHassan | Lahore, Pakistan</p>", unsafe_allow_html=True)
