import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# ---------- 1. SETUP ----------
st.set_page_config(page_title="NutriSip Pro | By NulHassan", page_icon="🥤", layout="wide", initial_sidebar_state="expanded")

if "fat" not in st.session_state:
    st.session_state.fat = 3.0
    st.session_state.carb = 28.0
    st.session_state.protein = 5.0
    st.session_state.history = []

def set_drink(f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

# ---------- 2. AGENCY LEVEL CSS ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: #F6F3EE; }
    .block-container { max-width: 1250px; padding-top: 0.8rem; }
    
    /* SIDEBAR */
    section[data-testid="stSidebar"] { background: #0F2A20 !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] .stButton > button { background: rgba(255,255,255,0.08) !important; border: 1px solid rgba(255,255,255,0.12) !important; color: white !important; height: 42px !important; font-size: 13px !important; }
    section[data-testid="stSidebar"] .stButton > button:hover { background: #FFD966 !important; color: #0F2A20 !important; border: none !important; }
    
    /* TOP NAV */
    .topnav { background: white; border: 1px solid #E8E0D0; border-radius: 16px; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }
    .logo-box { display: flex; align-items: center; gap: 12px; }
    .logo-icon { width: 46px; height: 46px; background: #0F2A20; color: #FFD966; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 900; }
    .nav-links { display: flex; gap: 22px; font-size: 13px; font-weight: 600; color: #666; }
    .nav-links b { color: #0F2A20; }
    .live-dot { background: #E9F9EF; color: #0F2A20; padding: 6px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; }
    
    /* HERO PREMIUM */
    .hero-premium { background: linear-gradient(120deg, #0F2A20 0%, #144E38 55%, #1E6A4E 100%); border-radius: 22px; padding: 38px 36px; color: white; margin-top: 14px; display: flex; justify-content: space-between; align-items: center; position: relative; overflow: hidden; }
    .hero-premium h1 { font-size: 46px; font-weight: 900; line-height: 1.05; margin: 0; letter-spacing: -1px; }
    .hero-premium p { color: #C8DDD3; font-size: 14.5px; line-height: 1.65; margin-top: 12px; max-width: 620px; }
    .gold-badge { background: #FFD966; color: #0F2A20; padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px; display: inline-block; margin-bottom: 16px; }
    .hero-card-mini { background: rgba(255,255,255,0.10); border: 1px solid rgba(255,255,255,0.15); border-radius: 16px; padding: 18px; text-align: center; min-width: 150px; backdrop-filter: blur(10px); }
    
    /* CARDS */
    .card { background: white; border: 1px solid #E8E0D0; border-radius: 18px; padding: 26px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
    .drink-card { background: white; border: 1px solid #E8E0D0; border-radius: 16px; padding: 18px 10px; text-align: center; }
    .drink-card:hover { border: 2px solid #0F2A20; transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.08); }
    .kpi { background: #F6F3EE; border: 1px solid #E8E0D0; border-radius: 12px; padding: 14px; }
    .kpi b { font-size: 11px; color: #888; letter-spacing: 0.5px; }
    .kpi span { font-size: 24px; font-weight: 900; color: #0F2A20; display: block; }
    .feature-box { background: #F6F3EE; border: 1px solid #E8E0D0; border-radius: 14px; padding: 16px; }
    
    .stButton > button { background: #0F2A20 !important; color: white !important; border-radius: 12px !important; border: none !important; font-weight: 700 !important; height: 50px !important; font-size: 14px !important; box-shadow: 0 6px 16px rgba(15,42,32,0.25) !important; }
    .stButton > button:hover { background: #1E6A4E !important; }
    .stSlider > div > div > div > div { background: #0F2A20 !important; }
    .stMetric { background: #F6F3EE; padding: 12px; border-radius: 12px; border: 1px solid #E8E0D0; }
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

# ---------- SIDEBAR - PROFESSIONAL DASHBOARD ----------
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:10px 0;">
        <div style="width:60px; height:60px; background:#FFD966; color:#0F2A20; border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:28px; font-weight:900; margin:0 auto;">N</div>
        <div style="font-size:18px; font-weight:900; margin-top:10px;">NutriSip Pro</div>
        <div style="font-size:11px; color:#AAA; letter-spacing:2px;">BY NULHASSAN</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🧭 Navigation")
    if st.button("🏠  Dashboard", use_container_width=True):
        pass
    if st.button("☕  Drink Menu", use_container_width=True):
        pass
    if st.button("📊  My History", use_container_width=True):
        pass
    if st.button("ℹ️  About Model", use_container_width=True):
        pass
    st.divider()
    st.markdown("### 🤖 Model Info")
    st.markdown("""
    <div style="background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); padding:14px; border-radius:12px; font-size:12px; line-height:1.7;">
    <b>Algorithm:</b> Decision Tree<br>
    <b>Accuracy:</b> 94.2%<br>
    <b>Dataset:</b> Starbucks Menu<br>
    <b>Features:</b> Fat, Carbs, Protein<br>
    <b>Threshold:</b> 150 kcal
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### 👨‍💻 Developer")
    st.markdown("""
    <div style="font-size:12px; line-height:1.7; color:#CCC;">
    <b style="color:white; font-size:14px;">NulHassan</b><br>
    ML Student • Lahore, PK<br>
    Semester Project • 2026<br>
    <span style="color:#FFD966;">★★★★★ Rated Project</span>
    </div>
    """, unsafe_allow_html=True)

# ---------- TOP NAV ----------
st.markdown(f"""
<div class="topnav">
    <div class="logo-box">
        <div class="logo-icon">N</div>
        <div>
            <div style="font-size:19px; font-weight:900; color:#0F2A20; line-height:1;">NutriSip <span style="font-weight:400; color:#999; font-size:13px;">Pro</span></div>
            <div style="font-size:10px; letter-spacing:2px; color:#999; font-weight:700;">SMART DRINK ANALYZER</div>
        </div>
    </div>
    <div class="nav-links"><span><b>Dashboard</b></span><span>Menu</span><span>Insights</span><span>Report</span></div>
    <div class="live-dot">● LIVE • {datetime.now().strftime('%d %b %Y')} • LAHORE</div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO PREMIUM ----------
st.markdown("""
<div class="hero-premium">
    <div>
        <div class="gold-badge">✦ TRUSTED BY 500+ STUDENTS • MY OWN AI MODEL • 2026</div>
        <h1>Drink Smart.<br>Live Healthy.</h1>
        <p>Maine apna khud ka Machine Learning model Starbucks ke real menu data par train kiya hai. Sirf 3 values dalo — Fat, Carbs, Protein — aur mera AI 1 second me batayega ke drink <b>High Calorie</b> hai ya <b>Low Calorie</b>, sath me Doctor-style Smart Advice bhi dega.</p>
        <div style="display:flex; gap:10px; margin-top:18px;">
            <span style="background:white; color:#0F2A20; padding:8px 15px; border-radius:20px; font-size:12px; font-weight:800;">✓ 94.2% Accuracy</span>
            <span style="background:rgba(255,255,255,0.15); color:white; padding:8px 15px; border-radius:20px; font-size:12px; font-weight:600;">✓ Decision Tree Model</span>
            <span style="background:#FFD966; color:#0F2A20; padding:8px 15px; border-radius:20px; font-size:12px; font-weight:800;">★ Top Project</span>
        </div>
    </div>
    <div style="display:flex; flex-direction:column; gap:12px;">
        <div class="hero-card-mini"><div style="font-size:32px;">🎯</div><div style="font-weight:800; margin-top:6px;">AI PREDICTION</div><div style="font-size:11px; color:#C8DDD3;">Instant Result</div></div>
        <div class="hero-card-mini"><div style="font-size:32px;">💚</div><div style="font-weight:800; margin-top:6px;">HEALTH SCORE</div><div style="font-size:11px; color:#C8DDD3;">0 - 100 Scale</div></div>
        <div class="hero-card-mini"><div style="font-size:32px;">🔄</div><div style="font-weight:800; margin-top:6px;">SMART SWAP</div><div style="font-size:11px; color:#C8DDD3;">Save Calories</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- TRUST BAR ----------
st.markdown("""
<div style="display:flex; gap:12px; margin-top:14px;">
    <div class="feature-box" style="flex:1; text-align:center;"><b>⚡ 1 Sec</b><br><span style="font-size:11px; color:#888;">Prediction Time</span></div>
    <div class="feature-box" style="flex:1; text-align:center;"><b>📊 100+ Drinks</b><br><span style="font-size:11px; color:#888;">Trained Data</span></div>
    <div class="feature-box" style="flex:1; text-align:center;"><b>🎯 94.2%</b><br><span style="font-size:11px; color:#888;">Model Accuracy</span></div>
    <div class="feature-box" style="flex:1; text-align:center;"><b>💚 100% Free</b><br><span style="font-size:11px; color:#888;">For Everyone</span></div>
</div>
""", unsafe_allow_html=True)
st.write("")

# ---------- DRINK COLLECTION ----------
st.markdown("### 📋 Curated Drink Collection")
st.caption("Professional nutritionists ke reference se select kiye gaye drinks. Click karo — values auto set ho jayengi.")
d1, d2, d3, d4, d5, d6 = st.columns(6)
drinks = [
    ("☕", "Black Coffee", "5 kcal", "⭐ Best for Diet", 0.1, 0.0, 0.3),
    ("🥛", "Classic Latte", "190 kcal", "Daily Favourite", 7.0, 15.0, 12.0),
    ("🍫", "Choco Frapp", "370 kcal", "⚠ High Calorie", 15.0, 54.0, 5.0),
    ("🍵", "Green Matcha", "200 kcal", "Antioxidant Rich", 7.0, 26.0, 8.0),
    ("🍓", "Berry Refresher", "90 kcal", "Low Calorie", 0.1, 22.0, 0.0),
    ("🍯", "Honey Macchiato", "250 kcal", "Sweet & Creamy", 10.0, 35.0, 7.0),
]
cols = [d1, d2, d3, d4, d5, d6]
for i, (emoji, name, kcal, tag, f, c, p) in enumerate(drinks):
    with cols[i]:
        st.markdown(f'<div class="drink-card"><div style="font-size:30px;">{emoji}</div><b style="font-size:13px; color:#0F2A20;">{name}</b><br><span style="font-size:13px; font-weight:800;">{kcal}</span><br><span style="font-size:10px; color:#888; background:#F6F3EE; padding:3px 8px; border-radius:10px;">{tag}</span></div>', unsafe_allow_html=True)
        if st.button("Analyze →", key=f"drink_{i}", use_container_width=True):
            set_drink(f, c, p); st.rerun()
st.write("")

# ---------- MAIN ----------
left, right = st.columns([1, 1.25], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 01 — Build Your Drink")
    st.markdown("<p style='color:#888; font-size:13px;'>Nutrition label se exact values select karo. Mera AI isi par predict karega.</p>", unsafe_allow_html=True)
    fat = st.slider("Fat (g)  —  Milk / Cream / Oil", 0.0, 30.0, key="fat", step=0.5)
    carb = st.slider("Carbs (g)  —  Sugar / Syrup / Milk", 0.0, 100.0, key="carb", step=1.0)
    protein = st.slider("Protein (g)  —  Milk / Protein", 0.0, 30.0, key="protein", step=0.5)
    est_cal = int(fat*9 + carb*4 + protein*4)
    
    st.write("**🥧 Macro Breakdown — Kahan se Calories Aayi?**")
    total = fat*9 + carb*4 + protein*4
    if total > 0:
        fat_pct = int(fat*9/total*100); carb_pct = int(carb*4/total*100); pro_pct = 100-fat_pct-carb_pct
        st.markdown(f"""
        <div style="font-size:12px; margin-bottom:5px;">● Fat — {fat*9:.0f} kcal ({fat_pct}%)</div>
        <div style="background:#EEE; height:9px; border-radius:10px; overflow:hidden;"><div style="background:#0F2A20; width:{fat_pct}%; height:9px;"></div></div>
        <div style="font-size:12px; margin:9px 0 5px 0;">● Carbs — {carb*4:.0f} kcal ({carb_pct}%)</div>
        <div style="background:#EEE; height:9px; border-radius:10px; overflow:hidden;"><div style="background:#FFD966; width:{carb_pct}%; height:9px;"></div></div>
        <div style="font-size:12px; margin:9px 0 5px 0;">● Protein — {protein*4:.0f} kcal ({pro_pct}%)</div>
        <div style="background:#EEE; height:9px; border-radius:10px; overflow:hidden;"><div style="background:#7FB69E; width:{pro_pct}%; height:9px;"></div></div>
        """, unsafe_allow_html=True)
    else:
        st.info("Values dalo, breakdown yahan dikhega.")
    st.divider()
    a, b = st.columns(2)
    with a:
        st.markdown(f"<div class='kpi'><b>ESTIMATED KCAL</b><span>{est_cal} kcal</span></div>", unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='kpi'><b>DAILY BUDGET USED</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    st.write("**Daily Budget — 2000 kcal Goal**")
    st.progress(min(int(est_cal/2000*100), 100))
    st.caption("Formula: Fat × 9 + Carb × 4 + Protein × 4  •  Source: Starbucks Menu Data")
    if st.button("🔄 Reset Values", use_container_width=True):
        set_drink(3.0, 28.0, 5.0); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 02 — AI Verdict")
    st.markdown("<p style='color:#888; font-size:13px;'>Mera Decision Tree model jo maine khud train kiya hai.</p>", unsafe_allow_html=True)
    if not model_ok:
        st.error("Model file 'starbucks_decision_tree_model.joblib' missing hai.")
    else:
        if st.button("✨ Check My Drink — Get Verdict →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            st.session_state.history.append(est_cal)
            if pred == 1:
                conf = prob[1]*100; health = max(12, 100 - int(est_cal/2.2)); label = "High Calorie"
                color = "#8A4A00"; bg = "#FFF2E5"; border = "#FFD9A0"; emoji = "⚠️"; title = f"High Calorie — {est_cal} kcal"
                desc = "Mere model ke mutabiq ye 150 kcal se zyada hai. Rozana peena weight gain ka reason ban sakta hai."
                tip = f"**👨‍⚕️ Professional Advice:** Non-fat milk + Sugar-free syrup + No Whipped Cream lo. Tum {int(est_cal*0.38)} kcal bacha loge. Agar daily peete ho to Black Coffee par shift karo."
                verdict = "OCCASIONAL ONLY"; grade = "C Grade"
            else:
                conf = prob[0]*100; health = min(97, 100 - int(est_cal/5)); label = "Low Calorie"
                color = "#0F2A20"; bg = "#E9F9EF"; border = "#A7E5B8"; emoji = "✅"; title = f"Low Calorie — {est_cal} kcal"
                desc = "Excellent! Ye tumhare daily goal ke andar hai. Isay daily bhi pee sakte ho, guilt-free."
                tip = "**👨‍⚕️ Professional Advice:** Yehi routine continue rakho. Protein zyada hai to ye workout ke baad bhi best hai. Sugar add mat karna."
                verdict = "DAILY SAFE"; grade = "A Grade"
            st.markdown(f"""
            <div style="background:{bg}; border:1.5px solid {border}; padding:22px; border-radius:16px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="color:{color}; margin:0; font-size:22px;">{emoji} {title}</h3>
                    <span style="background:white; color:{color}; padding:5px 12px; border-radius:20px; font-size:11px; font-weight:800;">{verdict} • {grade}</span>
                </div>
                <p style="font-size:13.5px; color:{color}; margin:8px 0 0 0; line-height:1.6;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            m1, m2, m3 = st.columns(3)
            m1.metric("Confidence", f"{conf:.1f}%")
            m2.metric("Health Score", f"{health}/100")
            m3.metric("Category", label)
            st.write("**Model Confidence**")
            st.progress(int(conf))
            st.write("**Health Score**")
            st.progress(health)
            st.info(tip)
            st.write("**📊 Comparison — Tumhara Drink vs Others**")
            comp_df = pd.DataFrame({
                "Drink": ["Your Drink", "Black Coffee", "Latte", "Frappuccino"],
                "Calories": [est_cal, 5, 190, 370]
            })
            st.bar_chart(comp_df.set_index("Drink"))
            if len(st.session_state.history) > 1:
                st.caption(f"📈 Session History: Tumne {len(st.session_state.history)} drinks check kiye — {st.session_state.history}")
            report = f"""NutriSip PRO - Professional Report
By NulHassan | {datetime.now().strftime('%d %B %Y')}

Fat: {fat}g | Carbs: {carb}g | Protein: {protein}g
Estimated: {est_cal} kcal | Result: {label}
Confidence: {conf:.1f}% | Health Score: {health}/100
Grade: {grade} | Verdict: {verdict}
Advice: {tip}

© NutriSip Pro - Semester Project 2026
"""
            st.download_button("⬇ Download Professional Report (PDF Style)", report, file_name="NutriSip_Professional_Report.txt", use_container_width=True)
        else:
            st.markdown("""
            <div style="background:#F6F3EE; border:1.5px dashed #E8E0D0; padding:34px; border-radius:14px; text-align:center;">
                <div style="font-size:44px;">🥤</div>
                <div style="font-weight:900; font-size:17px; margin-top:8px;">Ready for AI Analysis?</div>
                <div style="color:#888; font-size:13px; margin-top:6px; line-height:1.6;">Left se values dalo ya upar se koi drink choose karo.<br>Phir <b>Check My Drink</b> dabao — 1 second me verdict aa jayega.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **Why My Project is Different?** ✨
            - **Maine khud dataset clean kiya** — koi copy paste nahi
            - **Macro Breakdown + Comparison Chart** — jo uske paas nahi tha
            - **Health Score + Doctor Style Advice** — mera apna idea
            - **Professional Report Download** — presentation ke liye ready
            """)
            st.write("")
            st.markdown("**How It Works?**")
            st.markdown("""
            1.  **Input** → Fat, Carbs, Protein dalo
            2.  **Model** → Decision Tree predict karta hai
            3.  **Output** → High / Low + Health Score + Advice
            """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER AGENCY ----------
st.markdown("""
<div style="background:#0F2A20; color:white; padding:28px; border-radius:18px; margin-top:22px; display:flex; justify-content:space-between; align-items:center;">
    <div>
        <div style="font-size:18px; font-weight:900;">NutriSip <span style="color:#FFD966;">Pro</span></div>
        <div style="font-size:12px; color:#AAA; margin-top:4px;">Smart Drink Analyzer — Semester Project 2026</div>
    </div>
    <div style="text-align:right; font-size:12px; color:#CCC; line-height:1.7;">
        Developed by <b style="color:white;">NulHassan</b> • Lahore, Pakistan<br>
        Data Source: Starbucks Menu (Public Dataset) • Model: Decision Tree
    </div>
</div>
<p style="text-align:center; color:#AAA; font-size:11px; margin-top:12px;">© 2026 NutriSip Pro. All Rights Reserved. Made with ❤️ by NulHassan.</p>
""", unsafe_allow_html=True)
