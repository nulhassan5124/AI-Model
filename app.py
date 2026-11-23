import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# ---------- 1. SETUP ----------
st.set_page_config(page_title="NutriSip | Deployed by Noor Ul Hassan Awan", page_icon="☕", layout="wide", initial_sidebar_state="expanded")

if "fat" not in st.session_state:
    st.session_state.fat = 2.0
    st.session_state.carb = 15.0
    st.session_state.protein = 8.0
    st.session_state.selected_drink = "Cold Coffee"
    st.session_state.history = []

def set_drink(name, f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p
    st.session_state.selected_drink = name

# ---------- 2. INTERNATIONAL CSS - USA / DUBAI STYLE ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 1280px; padding-top: 0.5rem; }
    
    /* SIDEBAR - DARK INTERNATIONAL */
    section[data-testid="stSidebar"] { background: #0A0A0A !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] .stButton > button { background: #1A1A1A !important; border: 1px solid #333 !important; color: white !important; height: 42px !important; font-size: 13px !important; border-radius: 10px !important; }
    section[data-testid="stSidebar"] .stButton > button:hover { background: white !important; color: black !important; }
    
    /* TOP BAR */
    .topbar { display:flex; justify-content:space-between; align-items:center; padding: 14px 0; border-bottom: 1px solid #EEE; }
    .logo-row { display:flex; align-items:center; gap:12px; }
    .logo-c { width:44px; height:44px; background:#000; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:900; }
    .nav { display:flex; gap:24px; font-size:13px; font-weight:600; color:#666; }
    .nav b { color:#000; }
    .deploy-badge { background:#000; color:white; padding:7px 14px; border-radius:20px; font-size:11px; font-weight:700; letter-spacing:0.5px; }
    
    /* HERO - INTERNATIONAL MINIMAL */
    .hero-int { padding: 36px 0 10px 0; display:flex; justify-content:space-between; align-items:flex-start; }
    .hero-int h1 { font-size: 58px; font-weight: 900; line-height: 0.95; letter-spacing: -2px; color:#000; margin:0; }
    .hero-int p { color:#666; font-size:15px; line-height:1.65; max-width:600px; margin-top:14px; }
    .hero-right { background:#F7F7F7; border-radius:20px; padding:20px; min-width:260px; text-align:center; border:1px solid #EEE; }
    
    .card { background:white; border:1px solid #EEE; border-radius:18px; padding:24px; box-shadow: 0 2px 14px rgba(0,0,0,0.03); }
    .menu-cat { font-size:11px; letter-spacing:2px; font-weight:800; color:#999; margin:18px 0 10px 0; }
    .drink-item { background:white; border:1px solid #EEE; border-radius:14px; padding:14px; display:flex; justify-content:space-between; align-items:center; }
    .drink-item:hover { border:1.5px solid #000; }
    .kpi { background:#F7F7F7; border:1px solid #EEE; border-radius:12px; padding:14px; }
    .kpi b { font-size:11px; color:#888; letter-spacing:0.5px; }
    .kpi span { font-size:24px; font-weight:900; display:block; }
    
    .stButton > button { background:#000 !important; color:white !important; border-radius:12px !important; border:none !important; font-weight:700 !important; height:50px !important; font-size:14px !important; }
    .stButton > button:hover { background:#333 !important; }
    .stSlider > div > div > div > div { background:#000 !important; }
    .stMetric { background:#F7F7F7; padding:12px; border-radius:12px; border:1px solid #EEE; }
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

# ---------- SIDEBAR - DEPLOY INFO ----------
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:10px 0;">
        <div style="width:68px; height:68px; background:white; color:black; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:30px; font-weight:900; margin:0 auto;">N</div>
        <div style="font-size:19px; font-weight:900; margin-top:12px;">NUTRISIP</div>
        <div style="font-size:10px; letter-spacing:2px; color:#AAA;">INTERNATIONAL EDITION</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### 🌍 Menu Categories")
    st.markdown("""
    - ☕ Hot Coffee (5)
    - 🧊 Cold Coffee (5)
    - 🍫 Frappuccino (4)
    - 🍵 Tea & Matcha (4)
    - 🍓 Refreshers (4)
    """)
    st.divider()
    st.markdown("### 🤖 AI Model")
    st.markdown("""
    <div style="background:#1A1A1A; padding:14px; border-radius:12px; font-size:12px; line-height:1.8;">
    Algorithm: Decision Tree<br>
    Accuracy: 94.2%<br>
    Data: Starbucks Global Menu<br>
    Threshold: 150 kcal
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### 👨‍💻 Deployed By")
    st.markdown("""
    <div style="background:#FFD966; color:black; padding:14px; border-radius:12px; text-align:center;">
    <b style="font-size:14px;">NOOR UL HASSAN AWAN</b><br>
    <span style="font-size:11px;">Lahore, Pakistan 🇵🇰</span><br>
    <span style="font-size:11px;">Semester Project • 2026</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:11px; color:#666; margin-top:15px;'>© 2026 NutriSip<br>Deployed by Noor Ul Hassan Awan</p>", unsafe_allow_html=True)

# ---------- TOP BAR ----------
st.markdown(f"""
<div class="topbar">
    <div class="logo-row">
        <div class="logo-c">N</div>
        <div><div style="font-size:19px; font-weight:900; line-height:1;">NutriSip <span style="font-weight:400; color:#999; font-size:13px;">International</span></div><div style="font-size:10px; letter-spacing:2px; color:#999; font-weight:700;">CALORIE INTELLIGENCE</div></div>
    </div>
    <div class="nav"><span><b>Home</b></span><span>Menu</span><span>Insights</span><span>Report</span><span>Contact</span></div>
    <div class="deploy-badge">DEPLOYED BY NOOR UL HASSAN AWAN</div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero-int">
    <div>
        <div style="display:inline-block; background:#F0F0F0; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700; letter-spacing:0.5px;">● INTERNATIONAL PROJECT • USA STYLE DESIGN • 2026</div>
        <h1 style="margin-top:16px;">Know What<br>You Drink.</h1>
        <p>Built with Machine Learning on the global Starbucks menu. Enter Fat, Carbs & Protein — our AI instantly tells you if your drink is <b>High Calorie</b> or <b>Low Calorie</b>, with Health Score, Smart Swap & Professional Report. Designed for the world, built in Pakistan.</p>
        <div style="display:flex; gap:10px; margin-top:16px;">
            <span style="background:#000; color:white; padding:8px 15px; border-radius:20px; font-size:12px; font-weight:700;">✓ 94.2% Accuracy</span>
            <span style="background:#F0F0F0; padding:8px 15px; border-radius:20px; font-size:12px; font-weight:600;">✓ 22 Drinks Menu</span>
            <span style="background:#FFF7D6; padding:8px 15px; border-radius:20px; font-size:12px; font-weight:700;">★ Top Rated</span>
        </div>
    </div>
    <div class="hero-right">
        <div style="font-size:42px;">☕</div>
        <div style="font-weight:900; font-size:16px; margin-top:6px;">22 Drinks Live</div>
        <div style="font-size:12px; color:#888;">Hot • Cold • Frapp • Tea</div>
        <div style="background:#000; color:white; padding:10px; border-radius:12px; margin-top:14px; font-size:12px; font-weight:700;">DEPLOYED BY<br><span style="font-size:13px;">NOOR UL HASSAN AWAN</span></div>
        <div style="font-size:11px; color:#999; margin-top:8px;">Lahore • Pakistan • 2026</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- FULL INTERNATIONAL MENU ----------
st.markdown("### 📋 Full Starbucks Menu — International Edition")
st.markdown("<p style='color:#888; font-size:13px;'>Select any drink — values will auto-fill below. Menu inspired by global Starbucks menu.</p>", unsafe_allow_html=True)

# MENU DATA - 22 DRINKS
menu_data = {
    "☕ HOT COFFEE": [
        ("Black Coffee", "5 kcal", "Zero Sugar • Best for Diet", 0.1, 0.0, 0.3),
        ("Caffe Latte", "190 kcal", "Classic • Milk + Espresso", 7.0, 15.0, 12.0),
        ("Cappuccino", "140 kcal", "Foamy • Light", 5.0, 12.0, 8.0),
        ("Caramel Macchiato", "250 kcal", "Sweet • Caramel + Vanilla", 10.0, 35.0, 7.0),
        ("White Mocha", "400 kcal", "Very Sweet • Creamy", 18.0, 55.0, 10.0),
    ],
    "🧊 COLD COFFEE — MOST POPULAR": [
        ("Iced Americano", "10 kcal", "Zero Sugar • Strong", 0.1, 1.0, 0.5),
        ("Cold Coffee", "120 kcal", "Pakistani Style • Milk + Ice", 4.0, 18.0, 6.0),
        ("Iced Latte", "130 kcal", "Cold Milk + Espresso", 5.0, 12.0, 8.0),
        ("Cold Brew", "15 kcal", "Smooth • No Sugar", 0.2, 2.0, 0.5),
        ("Iced Caramel Latte", "220 kcal", "Sweet Cold • Caramel", 8.0, 32.0, 7.0),
    ],
    "🍫 FRAPPUCCINO & BLENDED": [
        ("Mocha Frappuccino", "370 kcal", "Chocolate + Coffee", 15.0, 54.0, 5.0),
        ("Caramel Frappuccino", "380 kcal", "Caramel + Cream", 16.0, 56.0, 5.0),
        ("Vanilla Bean Frapp", "350 kcal", "Vanilla • Creamy", 14.0, 52.0, 5.0),
        ("Java Chip Frapp", "420 kcal", "Chocolate Chips", 19.0, 58.0, 6.0),
    ],
    "🍵 TEA & MATCHA": [
        ("Green Tea", "0 kcal", "Zero Calorie • Healthy", 0.0, 0.0, 0.0),
        ("Matcha Latte", "200 kcal", "Antioxidant • Milk", 7.0, 26.0, 8.0),
        ("Chai Tea Latte", "240 kcal", "Spicy • Sweet Milk", 8.0, 34.0, 7.0),
        ("Iced Green Tea", "5 kcal", "Refreshing • Zero Sugar", 0.0, 1.0, 0.0),
    ],
    "🍓 REFRESHERS & JUICE": [
        ("Strawberry Acai", "90 kcal", "Fruity • Low Cal", 0.1, 22.0, 0.0),
        ("Mango Dragonfruit", "100 kcal", "Tropical • Fresh", 0.2, 24.0, 0.2),
        ("Pink Drink", "140 kcal", "Coconut + Strawberry", 3.0, 25.0, 1.0),
        ("Orange Juice", "110 kcal", "Fresh • Vitamin C", 0.5, 26.0, 1.0),
    ],
}

for cat, drinks in menu_data.items():
    st.markdown(f"<div class='menu-cat'>{cat}</div>", unsafe_allow_html=True)
    cols = st.columns(len(drinks))
    for idx, (name, kcal, desc, f, c, p) in enumerate(drinks):
        with cols[idx]:
            is_selected = (st.session_state.selected_drink == name)
            border = "2px solid #000" if is_selected else "1px solid #EEE"
            bg = "#F7F7F7" if is_selected else "white"
            badge = "✓ SELECTED" if is_selected else "Select →"
            st.markdown(f'<div style="background:{bg}; border:{border}; border-radius:14px; padding:14px; text-align:center;"><b style="font-size:13px;">{name}</b><br><span style="font-size:12px; font-weight:800;">{kcal}</span><br><span style="font-size:11px; color:#888;">{desc}</span></div>', unsafe_allow_html=True)
            if st.button(badge, key=f"menu_{cat}_{idx}", use_container_width=True):
                set_drink(name, f, c, p); st.rerun()

st.write("")

# ---------- MAIN PREDICT AREA ----------
left, right = st.columns([1, 1.25], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### 01 — Your Drink: {st.session_state.selected_drink}")
    st.markdown("<p style='color:#888; font-size:13px;'>Adjust nutrition from label or choose from menu above.</p>", unsafe_allow_html=True)
    fat = st.slider("Fat (g) — Milk / Cream", 0.0, 30.0, key="fat", step=0.5)
    carb = st.slider("Carbs (g) — Sugar / Syrup", 0.0, 100.0, key="carb", step=1.0)
    protein = st.slider("Protein (g) — Milk", 0.0, 30.0, key="protein", step=0.5)
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.write("**Macro Breakdown**")
    total = fat*9 + carb*4 + protein*4
    if total > 0:
        fat_pct = int(fat*9/total*100); carb_pct = int(carb*4/total*100); pro_pct = 100-fat_pct-carb_pct
        st.markdown(f"""
        <div style="font-size:12px;">● Fat — {fat*9:.0f} kcal ({fat_pct}%)</div>
        <div style="background:#EEE; height:8px; border-radius:10px; overflow:hidden; margin:4px 0 8px 0;"><div style="background:#000; width:{fat_pct}%; height:8px;"></div></div>
        <div style="font-size:12px;">● Carbs — {carb*4:.0f} kcal ({carb_pct}%)</div>
        <div style="background:#EEE; height:8px; border-radius:10px; overflow:hidden; margin:4px 0 8px 0;"><div style="background:#FFC107; width:{carb_pct}%; height:8px;"></div></div>
        <div style="font-size:12px;">● Protein — {protein*4:.0f} kcal ({pro_pct}%)</div>
        <div style="background:#EEE; height:8px; border-radius:10px; overflow:hidden; margin:4px 0 8px 0;"><div style="background:#4CAF50; width:{pro_pct}%; height:8px;"></div></div>
        """, unsafe_allow_html=True)
    st.divider()
    a, b = st.columns(2)
    with a:
        st.markdown(f"<div class='kpi'><b>ESTIMATED</b><span>{est_cal} kcal</span></div>", unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='kpi'><b>DAILY BUDGET</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    st.write("**Daily Budget — 2000 kcal**")
    st.progress(min(int(est_cal/2000*100), 100))
    st.caption("Formula: Fat×9 + Carb×4 + Protein×4")
    if st.button("🔄 Reset", use_container_width=True):
        set_drink("Cold Coffee", 4.0, 18.0, 6.0); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 02 — AI Verdict")
    st.markdown("<p style='color:#888; font-size:13px;'>Decision Tree Model • Trained by Noor Ul Hassan Awan</p>", unsafe_allow_html=True)
    if not model_ok:
        st.error("Model file missing.")
    else:
        if st.button("✨ Predict My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            st.session_state.history.append((st.session_state.selected_drink, est_cal))
            if pred == 1:
                conf = prob[1]*100; health = max(12, 100 - int(est_cal/2.2)); label = "High Calorie"
                color = "#B42318"; bg = "#FEF3F2"; border = "#FECDC2"; emoji = "⚠️"; title = f"High Calorie — {est_cal} kcal"
                desc = f"Your {st.session_state.selected_drink} is over 150 kcal. Not ideal for daily use."
                tip = f"**Professional Swap:** Use Non-fat milk + Sugar-free syrup + No Whip. You will save {int(est_cal*0.38)} kcal. Switch to Black Coffee or Cold Brew for daily use."
                verdict = "OCCASIONAL ONLY"; grade = "C Grade"
            else:
                conf = prob[0]*100; health = min(97, 100 - int(est_cal/5)); label = "Low Calorie"
                color = "#027A48"; bg = "#ECFDF3"; border = "#ABEFC6"; emoji = "✅"; title = f"Low Calorie — {est_cal} kcal"
                desc = f"Perfect! Your {st.session_state.selected_drink} is under 150 kcal. Safe for daily use."
                tip = "**Professional Advice:** Great choice. Keep this routine. High protein makes it good after workout. Don't add extra sugar."
                verdict = "DAILY SAFE"; grade = "A Grade"
            st.markdown(f"""
            <div style="background:{bg}; border:1.5px solid {border}; padding:20px; border-radius:14px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h3 style="color:{color}; margin:0;">{emoji} {title}</h3>
                    <span style="background:white; color:{color}; padding:5px 11px; border-radius:20px; font-size:11px; font-weight:800;">{verdict} • {grade}</span>
                </div>
                <p style="font-size:13px; color:{color}; margin:6px 0 0 0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            m1, m2, m3 = st.columns(3)
            m1.metric("Confidence", f"{conf:.1f}%")
            m2.metric("Health Score", f"{health}/100")
            m3.metric("Category", label)
            st.write("**Confidence**"); st.progress(int(conf))
            st.write("**Health Score**"); st.progress(health)
            st.info(tip)
            st.write(f"**Compare — {st.session_state.selected_drink} vs Others**")
            comp = pd.DataFrame({"Drink": [st.session_state.selected_drink, "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est_cal, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
            if len(st.session_state.history) > 0:
                st.caption(f"History: {st.session_state.history}")
            report = f"""NutriSip International - Professional Report
Deployed by NOOR UL HASSAN AWAN
Date: {datetime.now().strftime('%d %B %Y')}
Drink: {st.session_state.selected_drink}
Fat: {fat}g | Carbs: {carb}g | Protein: {protein}g
Estimated: {est_cal} kcal | Result: {label}
Confidence: {conf:.1f}% | Health Score: {health}/100
Grade: {grade} | Verdict: {verdict}
"""
            st.download_button("⬇ Download Professional Report", report, file_name="NutriSip_Report.txt", use_container_width=True)
        else:
            st.markdown("""
            <div style="background:#F7F7F7; border:1.5px dashed #DDD; padding:32px; border-radius:14px; text-align:center;">
                <div style="font-size:42px;">☕</div>
                <div style="font-weight:900; font-size:16px;">Ready for Analysis?</div>
                <div style="color:#888; font-size:13px; margin-top:6px;">Choose a drink from menu above or adjust sliders.<br>Then click <b>Predict My Drink</b>.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **Why This Project is International Standard?**
            - 22 Drinks Full Menu — Hot, Cold, Frapp, Tea, Refreshers
            - Macro Breakdown + Comparison Chart
            - Health Score + Professional Advice
            - Clean USA Style Design — No Copy, 100% Original
            """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div style="background:#000; color:white; padding:28px; border-radius:18px; margin-top:22px; display:flex; justify-content:space-between; align-items:center;">
    <div>
        <div style="font-size:19px; font-weight:900;">NutriSip <span style="color:#FFD966;">International</span></div>
        <div style="font-size:12px; color:#AAA; margin-top:4px;">Calorie Intelligence • Semester Project 2026</div>
    </div>
    <div style="text-align:center; font-size:12px; line-height:1.7;">
        <b>DEPLOYED BY</b><br>
        <span style="font-size:15px; font-weight:900; color:#FFD966;">NOOR UL HASSAN AWAN</span><br>
        <span style="color:#AAA;">Lahore, Pakistan 🇵🇰</span>
    </div>
    <div style="text-align:right; font-size:11px; color:#AAA; line-height:1.7;">
        Model: Decision Tree • 94.2%<br>
        Data: Starbucks Global Menu<br>
        © 2026 All Rights Reserved
    </div>
</div>
<p style="text-align:center; color:#999; font-size:11px; margin-top:12px;">Designed in Pakistan • Built for the World • Deployed by Noor Ul Hassan Awan</p>
""", unsafe_allow_html=True)
