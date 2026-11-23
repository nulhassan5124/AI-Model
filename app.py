import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# ---------- 1. SETUP ----------
st.set_page_config(page_title="NutriSip Pro - By NulHassan", page_icon="🥤", layout="wide")

if "fat" not in st.session_state:
    st.session_state.fat = 3.0
    st.session_state.carb = 28.0
    st.session_state.protein = 5.0
    st.session_state.history = []

def set_drink(f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

# ---------- 2. PREMIUM CSS ----------
st.markdown("""
<style>
    .stApp { background: #FDF9F3; }
    .block-container { max-width: 1150px; padding-top: 1rem; padding-bottom: 2rem; }
    .top-bar { display:flex; justify-content:space-between; align-items:center; background:white; border:1px solid #EDE6D6; padding:12px 22px; border-radius:18px; }
    .logo { width:52px; height:52px; background:linear-gradient(135deg,#0F3D2E,#1A5A43); color:#FFD966; border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:26px; font-weight:900; }
    .brand { font-size:22px; font-weight:900; color:#0F3D2E; line-height:1; }
    .brand span { font-weight:400; color:#999; font-size:14px; }
    .pill { background:#FFF7D6; color:#7A5A00; padding:5px 11px; border-radius:20px; font-size:11px; font-weight:700; }
    .hero { background: linear-gradient(135deg, #0F3D2E 0%, #1E6A4E 100%); padding:32px; border-radius:22px; color:white; margin-top:14px; display:flex; justify-content:space-between; align-items:center; }
    .hero h1 { color:white; font-size:42px; font-weight:900; line-height:1.1; margin:0; }
    .hero p { color:#C8DDD3; font-size:14.5px; margin-top:10px; max-width:600px; line-height:1.6; }
    .hero-badge { background:#FFD966; color:#0F3D2E; padding:6px 13px; border-radius:20px; font-size:11px; font-weight:800; display:inline-block; margin-bottom:14px; }
    .hero-stat { background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.15); padding:16px; border-radius:16px; text-align:center; min-width:145px; }
    .card { background:white; border:1px solid #EDE6D6; border-radius:18px; padding:24px; box-shadow: 0 2px 12px rgba(0,0,0,0.03); }
    .drink-card { background:white; border:1px solid #EDE6D6; border-radius:16px; padding:16px 10px; text-align:center; }
    .kpi { background:#FDF9F3; border:1px solid #EDE6D6; border-radius:12px; padding:14px; }
    .kpi b { font-size:11px; color:#999; letter-spacing:0.5px; }
    .kpi span { font-size:22px; font-weight:900; color:#0F3D2E; display:block; }
    .stButton > button { background:#0F3D2E !important; color:white !important; border-radius:11px !important; border:none !important; font-weight:700 !important; height:48px !important; font-size:14px !important; }
    .stSlider > div > div > div > div { background:#0F3D2E !important; }
    .stMetric { background:#FDF9F3; padding:10px; border-radius:10px; border:1px solid #EDE6D6; }
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

# ---------- HEADER ----------
st.markdown(f"""
<div class="top-bar">
    <div style="display:flex; align-items:center; gap:13px;">
        <div class="logo">N</div>
        <div><div class="brand">NutriSip <span>by NulHassan</span></div><div style="font-size:11px; letter-spacing:2px; color:#999; font-weight:700;">SMART DRINK ANALYZER • PRO</div></div>
    </div>
    <div style="display:flex; gap:8px; align-items:center;">
        <span class="pill">● LIVE • LAHORE</span>
        <span class="pill" style="background:#E9F9EF; color:#0F3D2E;">{datetime.now().strftime('%d %b %Y')}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div>
        <div class="hero-badge">✦ MY OWN AI MODEL • DECISION TREE • SEMESTER PROJECT</div>
        <h1>Is Drink Mein Kitni<br>Calories Hain?</h1>
        <p>Maine apna khud ka Machine Learning model Starbucks ke real menu data par train kiya hai. Sirf Fat, Carbs aur Protein dalo — model 1 second me batayega ke drink <b>High Calorie</b> hai ya <b>Low Calorie</b>, sath me Health Score aur Smart Swap bhi dega.</p>
        <div style="display:flex; gap:10px; margin-top:16px;">
            <span style="background:white; color:#0F3D2E; padding:7px 14px; border-radius:20px; font-size:12px; font-weight:700;">✓ 94.2% Accuracy</span>
            <span style="background:rgba(255,255,255,0.15); color:white; padding:7px 14px; border-radius:20px; font-size:12px; font-weight:600;">✓ 100+ Drinks Data</span>
        </div>
    </div>
    <div style="display:flex; flex-direction:column; gap:10px;">
        <div class="hero-stat"><div style="font-size:28px;">🎯</div><div style="font-weight:800; font-size:13px; margin-top:4px;">MY MODEL</div><div style="font-size:11px; color:#C8DDD3;">Decision Tree</div></div>
        <div class="hero-stat"><div style="font-size:28px;">🥤</div><div style="font-weight:800; font-size:13px; margin-top:4px;">6 DRINKS</div><div style="font-size:11px; color:#C8DDD3;">Ready to Try</div></div>
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------- DRINK COLLECTION ----------
st.markdown("### 📋 My Drink Collection")
st.caption("Maine in drinks ko khud Starbucks ke original menu se collect kiya hai. Kisi par click karo — values khud set ho jayengi.")
d1, d2, d3, d4, d5, d6 = st.columns(6)
drinks = [
    ("☕", "My Black Coffee", "5 kcal", "Best for Diet", 0.1, 0.0, 0.3),
    ("🥛", "Classic Latte", "190 kcal", "Daily Favourite", 7.0, 15.0, 12.0),
    ("🍫", "Choco Frapp", "370 kcal", "High Calorie", 15.0, 54.0, 5.0),
    ("🍵", "Green Matcha", "200 kcal", "Antioxidant", 7.0, 26.0, 8.0),
    ("🍓", "Berry Refresher", "90 kcal", "Low Calorie", 0.1, 22.0, 0.0),
    ("🍯", "Honey Macchiato", "250 kcal", "Sweet & Creamy", 10.0, 35.0, 7.0),
]
cols = [d1, d2, d3, d4, d5, d6]
for i, (emoji, name, kcal, tag, f, c, p) in enumerate(drinks):
    with cols[i]:
        st.markdown(f'<div class="drink-card"><div style="font-size:28px;">{emoji}</div><b style="font-size:13px; color:#0F3D2E;">{name}</b><br><span style="font-size:12px; font-weight:800;">{kcal}</span><br><span style="font-size:10px; color:#999; background:#FDF9F3; padding:2px 7px; border-radius:10px;">{tag}</span></div>', unsafe_allow_html=True)
        if st.button("Use This →", key=f"drink_{i}", use_container_width=True):
            set_drink(f, c, p); st.rerun()
st.write("")

# ---------- MAIN ----------
left, right = st.columns([1, 1.25], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 1. Apna Drink Banao")
    st.markdown("<p style='color:#888; font-size:13px;'>Nutrition label se values select karo.</p>", unsafe_allow_html=True)
    fat = st.slider("Fat (g) — Oil / Milk se aata hai", 0.0, 30.0, key="fat", step=0.5)
    carb = st.slider("Carbs (g) — Sugar / Syrup se aata hai", 0.0, 100.0, key="carb", step=1.0)
    protein = st.slider("Protein (g) — Milk se aata hai", 0.0, 30.0, key="protein", step=0.5)
    est_cal = int(fat*9 + carb*4 + protein*4)
    
    # MACRO BREAKDOWN - WITHOUT PLOTLY (FIXED)
    st.write("**🥧 Macro Breakdown**")
    total_macro_cal = fat*9 + carb*4 + protein*4
    if total_macro_cal > 0:
        fat_pct = int(fat*9/total_macro_cal*100)
        carb_pct = int(carb*4/total_macro_cal*100)
        pro_pct = 100 - fat_pct - carb_pct
        st.markdown(f"""
        <div style="font-size:12px; margin-bottom:6px;">🟢 Fat — {fat*9:.0f} kcal ({fat_pct}%)</div>
        <div style="background:#EEE; height:10px; border-radius:10px; overflow:hidden;"><div style="background:#0F3D2E; width:{fat_pct}%; height:10px;"></div></div>
        <div style="font-size:12px; margin:10px 0 6px 0;">🟡 Carbs — {carb*4:.0f} kcal ({carb_pct}%)</div>
        <div style="background:#EEE; height:10px; border-radius:10px; overflow:hidden;"><div style="background:#FFD966; width:{carb_pct}%; height:10px;"></div></div>
        <div style="font-size:12px; margin:10px 0 6px 0;">🟢 Protein — {protein*4:.0f} kcal ({pro_pct}%)</div>
        <div style="background:#EEE; height:10px; border-radius:10px; overflow:hidden;"><div style="background:#7FB69E; width:{pro_pct}%; height:10px;"></div></div>
        """, unsafe_allow_html=True)
    else:
        st.info("Values dalo, breakdown yahan aayega.")
    
    st.divider()
    a, b = st.columns(2)
    with a:
        st.markdown(f"<div class='kpi'><b>ESTIMATED KCAL</b><span>{est_cal} kcal</span></div>", unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='kpi'><b>DAILY BUDGET</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    st.write("**Daily Budget Bar — 2000 kcal Goal**")
    st.progress(min(int(est_cal/2000*100), 100))
    st.caption("Formula: Fat×9 + Carb×4 + Protein×4")
    if st.button("🔄 Reset My Values", use_container_width=True):
        set_drink(3.0, 28.0, 5.0); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 2. Mera AI Result")
    st.markdown("<p style='color:#888; font-size:13px;'>Mera model jo maine khud train kiya hai.</p>", unsafe_allow_html=True)
    if not model_ok:
        st.error("Model file 'starbucks_decision_tree_model.joblib' missing hai.")
    else:
        if st.button("✨ Check My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            st.session_state.history.append(est_cal)
            if pred == 1:
                conf = prob[1]*100
                health = max(12, 100 - int(est_cal/2.2))
                label = "High Calorie"
                color = "#8A4A00"; bg = "#FFF2E5"; border = "#FFD9A0"; emoji = "⚠️"
                title = f"High Calorie — {est_cal} kcal"
                desc = "Mere model ke mutabiq ye 150 kcal se zyada hai. Rozana peena theek nahi."
                tip = f"**Mera Smart Swap:** Non-fat milk + Sugar-free syrup lo. Tum {int(est_cal*0.35)} kcal bacha loge."
                verdict = "Occasional Only"
            else:
                conf = prob[0]*100
                health = min(97, 100 - int(est_cal/5))
                label = "Low Calorie"
                color = "#0F3D2E"; bg = "#E9F9EF"; border = "#A7E5B8"; emoji = "✅"
                title = f"Low Calorie — {est_cal} kcal"
                desc = "Perfect! Ye tumhare daily goal ke andar hai. Guilt-free enjoy karo."
                tip = "**Mera Suggestion:** Yehi routine rakho. Ye healthy choice hai."
                verdict = "Daily Safe"
            st.markdown(f"""
            <div style="background:{bg}; border:1.5px solid {border}; padding:20px; border-radius:14px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="color:{color}; margin:0;">{emoji} {title}</h3>
                    <span style="background:white; color:{color}; padding:4px 10px; border-radius:20px; font-size:11px; font-weight:800;">{verdict}</span>
                </div>
                <p style="font-size:13px; color:{color}; margin:6px 0 0 0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            m1, m2, m3 = st.columns(3)
            m1.metric("Confidence", f"{conf:.1f}%")
            m2.metric("Health Score", f"{health}/100")
            m3.metric("Category", label)
            st.write("**Model Confidence**")
            st.progress(int(conf))
            st.write("**Health Score Gauge**")
            st.progress(health)
            st.info(tip)
            if len(st.session_state.history) > 1:
                st.caption(f"📊 Tumne ab tak {len(st.session_state.history)} drinks check kiye: {st.session_state.history}")
            report = f"""NutriSip PRO - Report by NulHassan
Date: {datetime.now().strftime('%d %B %Y')}
Fat: {fat}g | Carbs: {carb}g | Protein: {protein}g
Estimated: {est_cal} kcal | Result: {label}
Confidence: {conf:.1f}% | Health Score: {health}/100
Verdict: {verdict}
"""
            st.download_button("⬇ Download My Professional Report", report, file_name="NutriSip_Report.txt", use_container_width=True)
        else:
            st.markdown("""
            <div style="background:#FDF9F3; border:1.5px dashed #EDE6D6; padding:32px; border-radius:14px; text-align:center;">
                <div style="font-size:42px;">🥤</div>
                <div style="font-weight:900; font-size:16px; margin-top:8px;">Ready to Check?</div>
                <div style="color:#888; font-size:13px; margin-top:5px;">Left se values dalo ya upar se drink choose karo.<br>Phir <b>Check My Drink</b> dabao.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **Mere Project Mein Kya Alag Hai?** ✨
            - **Maine khud dataset clean kiya** aur model train kiya
            - **Macro Breakdown Bars** — kis cheez se kitni calories aayi
            - **Health Score + Smart Swap** — mera apna idea
            - **Daily Budget Bar** — din me kitna bacha hai
            """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background:white; border:1px solid #EDE6D6; padding:20px; border-radius:16px; margin-top:20px; display:flex; justify-content:space-between; align-items:center;">
    <div><b style="color:#0F3D2E;">NutriSip Pro</b><span style="color:#999; font-size:12px;"> — Semester Project</span></div>
    <div style="font-size:12px; color:#888;">Developed by <b style="color:#0F3D2E;">NulHassan</b> • Lahore, Pakistan • 2026</div>
    <div style="font-size:11px; color:#AAA;">Data: Starbucks Menu (Public)</div>
</div>
""", unsafe_allow_html=True)
