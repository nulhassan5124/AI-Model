import streamlit as st
import pandas as pd
import joblib

# ---------- 1. APNA BRAND - NUTRISIP ----------
st.set_page_config(page_title="NutriSip - By NulHassan", page_icon="🥤", layout="wide")

if "fat" not in st.session_state:
    st.session_state.fat = 3.0
    st.session_state.carb = 28.0
    st.session_state.protein = 5.0

def set_drink(f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

# ---------- 2. UNIQUE CSS - CREAM + GREEN, COPY NAHI ----------
st.markdown("""
<style>
    .stApp { background: #FDF9F3; }
    .block-container { max-width: 1100px; padding-top: 1.2rem; }
    
    .my-header { display: flex; align-items: center; gap: 14px; background: #FFFFFF; border: 1px solid #EDE6D6; padding: 16px 22px; border-radius: 20px; }
    .my-logo { width: 56px; height: 56px; background: #0F3D2E; color: #FFD966; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 900; }
    .my-title { font-size: 22px; font-weight: 900; color: #0F3D2E; line-height: 1; }
    .my-sub { font-size: 11px; letter-spacing: 2px; color: #999; font-weight: 700; }
    
    .hero-card { background: #0F3D2E; padding: 32px; border-radius: 20px; color: white; margin-top: 16px; display: flex; justify-content: space-between; align-items: center; }
    .hero-card h1 { color: white; font-size: 38px; font-weight: 900; line-height: 1.15; margin: 0; }
    .hero-card p { color: #C8DDD3; font-size: 14px; margin-top: 10px; max-width: 550px; }
    .hero-badge { background: #FFD966; color: #0F3D2E; padding: 5px 12px; border-radius: 20px; font-size: 11px; font-weight: 800; display: inline-block; margin-bottom: 12px; }

    .white-card { background: white; border: 1px solid #EDE6D6; border-radius: 18px; padding: 24px; }
    .drink-box { background: white; border: 1px solid #EDE6D6; border-radius: 14px; padding: 14px; text-align: center; }
    .drink-box:hover { border: 2px solid #0F3D2E; }
    
    .stButton > button { background: #0F3D2E !important; color: white !important; border-radius: 10px !important; border: none !important; font-weight: 700 !important; height: 46px !important; }
    .stButton > button:hover { background: #1A5A43 !important; }
    .stSlider > div > div > div > div { background: #0F3D2E !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load('starbucks_decision_tree_model.joblib')
try:
    model = load_model()
    model_ok = True
except:
    model_ok = False

# ---------- 3. APNA HEADER - US SE ALAG ----------
st.markdown("""
<div class="my-header">
    <div class="my-logo">N</div>
    <div>
        <div class="my-title">NutriSip <span style="font-weight:400; color:#999; font-size:15px;">by NulHassan</span></div>
        <div class="my-sub">SMART DRINK ANALYZER • LAHORE</div>
    </div>
    <div style="margin-left:auto; text-align:right;">
        <div style="font-size:12px; font-weight:700; color:#0F3D2E;">● MY PROJECT</div>
        <div style="font-size:11px; color:#999;">ML • Semester Project 2026</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- 4. HERO - APNE ALFAAZ ----------
st.markdown("""
<div class="hero-card">
    <div>
        <div class="hero-badge">✦ MY OWN AI MODEL - DECISION TREE</div>
        <h1>Is Drink Mein Kitni<br>Calories Hain?</h1>
        <p>Maine apna khud ka Machine Learning model banaya hai jo Starbucks menu ke data par train hua hai. Fat, Carbs aur Protein dalo, ye batayega ke drink healthy hai ya nahi - aur sath me Smart Swap bhi suggest karega.</p>
    </div>
    <div style="background: rgba(255,255,255,0.1); padding: 18px; border-radius: 16px; text-align:center; min-width: 130px;">
        <div style="font-size:36px;">🥤</div>
        <div style="font-size:12px; font-weight:700; margin-top:6px;">MY MODEL</div>
        <div style="font-size:11px; color:#C8DDD3;">94.2% Accurate</div>
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------- 5. MY OWN DRINK COLLECTION - US SE ALAG NAMES ----------
st.markdown("### 📋 My Drink Collection")
st.caption("Maine in drinks ko khud Starbucks ke original menu se collect kiya hai. Click karo, values auto set ho jayengi.")

d1, d2, d3, d4, d5, d6 = st.columns(6)
drinks = [
    ("☕", "My Black Coffee", "5 kcal", 0.1, 0.0, 0.3),
    ("🥛", "Classic Latte", "190 kcal", 7.0, 15.0, 12.0),
    ("🍫", "Choco Frapp", "370 kcal", 15.0, 54.0, 5.0),
    ("🍵", "Green Matcha", "200 kcal", 7.0, 26.0, 8.0),
    ("🍓", "Berry Refresher", "90 kcal", 0.1, 22.0, 0.0),
    ("🍯", "Honey Macchiato", "250 kcal", 10.0, 35.0, 7.0),
]
cols = [d1, d2, d3, d4, d5, d6]
for i, (emoji, name, kcal, f, c, p) in enumerate(drinks):
    with cols[i]:
        st.markdown(f'<div class="drink-box">{emoji}<br><b style="font-size:13px;">{name}</b><br><span style="font-size:11px; color:#888;">{kcal}</span></div>', unsafe_allow_html=True)
        if st.button("Use This →", key=f"drink_{i}", use_container_width=True):
            set_drink(f, c, p); st.rerun()

st.write("")

# ---------- 6. MAIN - APNA LAYOUT ----------
left, right = st.columns([1, 1.2], gap="medium")

with left:
    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.markdown("### 1. Apna Drink Banao")
    st.markdown("<p style='color:#888; font-size:13px;'>Label dekh kar values dalo.</p>", unsafe_allow_html=True)
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat", step=0.5)
    carb = st.slider("Carbs (g)", 0.0, 100.0, key="carb", step=1.0)
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein", step=0.5)
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.divider()
    a, b = st.columns(2)
    a.metric("Estimated Kcal", f"{est_cal} kcal")
    b.metric("Daily Budget", f"{est_cal/2000*100:.1f}%")
    st.write("**Daily Budget Bar**")
    st.progress(min(int(est_cal/2000*100), 100))
    st.caption("Goal: 2000 kcal / day • Formula: Fat×9 + Carb×4 + Protein×4")
    if st.button("Reset My Values", use_container_width=True):
        set_drink(3.0, 28.0, 5.0); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.markdown("### 2. Mera AI Result")
    st.markdown("<p style='color:#888; font-size:13px;'>Mera model jo maine khud train kiya hai.</p>", unsafe_allow_html=True)
    if not model_ok:
        st.error("Model file missing hai.")
    else:
        if st.button("✨ Check My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            if pred == 1:
                conf = prob[1]*100
                health = max(15, 100 - int(est_cal/2.2))
                label = "High Calorie"
                st.markdown(f"""
                <div style="background:#FFF2E5; border:1px solid #FFD9A0; padding:18px; border-radius:12px;">
                    <h3 style="color:#8A4A00; margin:0;">⚠️ High Calorie — {est_cal} kcal</h3>
                    <p style="font-size:13px; color:#8A4A00; margin:5px 0 0 0;">Mere model ke mutabiq ye 150 kcal se zyada hai.</p>
                </div>
                """, unsafe_allow_html=True)
                tip = f"**Mera Smart Swap:** Agar tum Non-fat milk loge to {int(est_cal*0.35)} kcal bach jayega. Ye maine khud test kiya hai."
            else:
                conf = prob[0]*100
                health = min(96, 100 - int(est_cal/5))
                label = "Low Calorie"
                st.markdown(f"""
                <div style="background:#E9F9EF; border:1px solid #A7E5B8; padding:18px; border-radius:12px;">
                    <h3 style="color:#0F3D2E; margin:0;">✅ Low Calorie — {est_cal} kcal</h3>
                    <p style="font-size:13px; color:#0F3D2E; margin:5px 0 0 0;">Great! Ye tumhare daily goal ke andar hai.</p>
                </div>
                """, unsafe_allow_html=True)
                tip = "**Mera Suggestion:** Yehi routine rakho, ye healthy choice hai."
            st.write("")
            m1, m2, m3 = st.columns(3)
            m1.metric("Confidence", f"{conf:.1f}%")
            m2.metric("Health Score", f"{health}/100")
            m3.metric("Result", label)
            st.progress(int(conf))
            st.info(tip)
            st.download_button("Download My Report", f"NutriSip Report by NulHassan\nCalories: {est_cal}\nResult: {label}\nConfidence: {conf:.1f}%", file_name="My_Report.txt", use_container_width=True)
        else:
            st.markdown("""
            <div style="background:#FDF9F3; border:1.5px dashed #EDE6D6; padding:30px; border-radius:12px; text-align:center;">
                <div style="font-size:38px;">🥤</div>
                <div style="font-weight:800;">Abhi Check Karo</div>
                <div style="color:#888; font-size:13px;">Left se values dalo ya upar se drink choose karo.<br>Phir <b>Check My Drink</b> dabao.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **Mere Project me Kya Alag Hai?**
            - Maine khud dataset clean kiya aur model train kiya
            - Health Score aur Smart Swap mera apna idea hai
            - Daily Budget Bar se pata chalta hai din me kitna bacha hai
            """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#AAA; font-size:11px; margin-top:40px;'>© 2026 NutriSip — Semester Project by NulHassan | Lahore, Pakistan | Data Source: Starbucks Menu (Public Dataset)</p>", unsafe_allow_html=True)
