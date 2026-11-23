import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# ---------- 1. SETUP - SAFE, NO ERROR ----------
st.set_page_config(page_title="NutriSip | Deployed by Noor Ul Hassan Awan", page_icon="☕", layout="wide", initial_sidebar_state="expanded")

# HAR KEY ALAG SE CHECK - AB KABHI KEYERROR NAHI AAYEGA
for key, val in [("fat", 4.0), ("carb", 18.0), ("protein", 6.0), ("selected_drink", "Cold Coffee"), ("history", [])]:
    if key not in st.session_state:
        st.session_state[key] = val

def set_drink(name, f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p
    st.session_state.selected_drink = name

# ---------- 2. INTERNATIONAL AGENCY CSS ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: #FAFAF8; }
    .block-container { max-width: 1300px; padding-top: 0.6rem; }

    /* SIDEBAR */
    section[data-testid="stSidebar"] { background: #000000 !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] .stButton > button { background: #1A1A1A !important; border: 1px solid #333 !important; color: white !important; height: 44px !important; font-size: 13px !important; border-radius: 12px !important; }
    section[data-testid="stSidebar"] .stButton > button:hover { background: #FFD966 !important; color: #000 !important; border: none !important; }

    /* TOP BAR */
    .topbar { background: white; border: 1px solid #EDEDEA; border-radius: 16px; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center; }
    .logo-c { width: 46px; height: 46px; background: #000; color: #FFD966; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 900; }
    .nav { display: flex; gap: 26px; font-size: 13px; font-weight: 600; color: #777; }
    .nav b { color: #000; border-bottom: 2px solid #000; padding-bottom: 3px; }
    .deploy-top { background: #000; color: white; padding: 8px 16px; border-radius: 20px; font-size: 11px; font-weight: 800; letter-spacing: 0.5px; }

    /* HERO */
    .hero { background: linear-gradient(115deg, #000000 0%, #1A1A1A 55%, #2A2A2A 100%); border-radius: 24px; padding: 42px 38px; color: white; margin-top: 14px; display: flex; justify-content: space-between; align-items: center; }
    .hero h1 { font-size: 62px; font-weight: 900; line-height: 0.95; letter-spacing: -2.5px; margin: 0; }
    .hero h1 span { color: #FFD966; }
    .hero p { color: #BBB; font-size: 15px; line-height: 1.7; max-width: 620px; margin-top: 16px; }
    .hero-right { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12); border-radius: 20px; padding: 22px; min-width: 270px; text-align: center; }

    /* CARDS */
    .card { background: white; border: 1px solid #EDEDEA; border-radius: 20px; padding: 26px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
    .menu-cat { font-size: 11px; letter-spacing: 2.5px; font-weight: 800; color: #000; background: #FFD966; display: inline-block; padding: 6px 12px; border-radius: 20px; margin: 22px 0 12px 0; }
    .kpi { background: #FAFAF8; border: 1px solid #EDEDEA; border-radius: 12px; padding: 14px; }
    .kpi b { font-size: 11px; color: #888; letter-spacing: 0.5px; }
    .kpi span { font-size: 26px; font-weight: 900; display: block; }

    .stButton > button { background: #000 !important; color: white !important; border-radius: 12px !important; border: none !important; font-weight: 700 !important; height: 52px !important; font-size: 14px !important; }
    .stButton > button:hover { background: #222 !important; }
    .stSlider > div > div > div > div { background: #000 !important; }
    .stMetric { background: #FAFAF8; padding: 12px; border-radius: 12px; border: 1px solid #EDEDEA; }
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

# ---------- SIDEBAR - DEPLOY INFO ----------
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:8px 0;">
        <div style="width:72px; height:72px; background:#FFD966; color:#000; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:32px; font-weight:900; margin:0 auto;">N</div>
        <div style="font-size:20px; font-weight:900; margin-top:12px;">NUTRISIP</div>
        <div style="font-size:10px; letter-spacing:3px; color:#888;">INTERNATIONAL</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### ☕ Cafe Menu")
    st.markdown("""
    **Hot Coffee** — 5 Drinks<br>
    **Cold Coffee** — 5 Drinks<br>
    **Frappuccino** — 4 Drinks<br>
    **Tea & Matcha** — 4 Drinks<br>
    **Refreshers** — 4 Drinks<br>
    <br>
    **Total: 22 Drinks**
    """)
    st.divider()
    st.markdown("### 🤖 AI Engine")
    st.markdown("""
    <div style="background:#1A1A1A; padding:14px; border-radius:12px; font-size:12px; line-height:1.9;">
    Model: Decision Tree<br>
    Accuracy: 94.2%<br>
    Data: Starbucks Global<br>
    Threshold: 150 kcal
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("""
    <div style="background:#FFD966; color:#000; padding:16px; border-radius:14px; text-align:center;">
        <div style="font-size:10px; letter-spacing:2px; font-weight:800;">DEPLOYED BY</div>
        <div style="font-size:16px; font-weight:900; margin-top:4px; line-height:1.2;">NOOR UL HASSAN<br>AWAN</div>
        <div style="font-size:11px; margin-top:6px;">Lahore, Pakistan 🇵🇰<br>2026</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- TOP BAR ----------
st.markdown("""
<div class="topbar">
    <div style="display:flex; align-items:center; gap:12px;">
        <div class="logo-c">N</div>
        <div><div style="font-size:19px; font-weight:900; line-height:1;">NutriSip <span style="font-weight:400; color:#999; font-size:13px;">International</span></div><div style="font-size:10px; letter-spacing:2px; color:#999; font-weight:700;">CALORIE INTELLIGENCE • USA STYLE</div></div>
    </div>
    <div class="nav"><span><b>Home</b></span><span>Menu</span><span>Insights</span><span>Report</span></div>
    <div class="deploy-top">DEPLOYED BY NOOR UL HASSAN AWAN</div>
</div>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div>
        <div style="display:inline-block; background:#FFD966; color:#000; padding:6px 13px; border-radius:20px; font-size:11px; font-weight:800; letter-spacing:0.5px;">● INTERNATIONAL PROJECT • DESIGNED IN PAKISTAN • FOR THE WORLD</div>
        <h1 style="margin-top:18px;">Know What<br>You <span>Drink.</span></h1>
        <p>Experience the world's smartest drink analyzer. Built with Machine Learning on the global Starbucks menu. Choose any drink from our full cafe menu — our AI will instantly tell you if it's <b style="color:white;">High Calorie</b> or <b style="color:white;">Low Calorie</b>, with Health Score & Professional Advice.</p>
        <div style="display:flex; gap:10px; margin-top:18px;">
            <span style="background:white; color:#000; padding:9px 16px; border-radius:20px; font-size:12px; font-weight:800;">✓ 94.2% Accuracy</span>
            <span style="background:rgba(255,255,255,0.15); color:white; padding:9px 16px; border-radius:20px; font-size:12px; font-weight:600;">✓ 22 Drinks Menu</span>
            <span style="background:#FFD966; color:#000; padding:9px 16px; border-radius:20px; font-size:12px; font-weight:800;">★ Top Rated Project</span>
        </div>
    </div>
    <div class="hero-right">
        <div style="font-size:46px;">☕</div>
        <div style="font-weight:900; font-size:17px; margin-top:6px;">22 Drinks Live</div>
        <div style="font-size:12px; color:#AAA;">Hot • Cold • Frapp • Tea • Juice</div>
        <div style="background:#FFD966; color:#000; padding:12px; border-radius:12px; margin-top:16px; font-weight:900; font-size:12px; line-height:1.4;">DEPLOYED BY<br><span style="font-size:14px;">NOOR UL HASSAN AWAN</span></div>
        <div style="font-size:11px; color:#999; margin-top:8px;">Lahore • Pakistan • 2026</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- FULL CAFE MENU ----------
st.markdown("### 📋 Full Cafe Menu — Choose Your Drink")
st.caption("International cafe menu — Click any drink, values will auto-fill below.")

menu_data = {
    "☕  HOT COFFEE": [
        ("Black Coffee", "5 kcal", "Zero Sugar • Best for Diet", 0.1, 0.0, 0.3),
        ("Caffe Latte", "190 kcal", "Milk + Espresso", 7.0, 15.0, 12.0),
        ("Cappuccino", "140 kcal", "Foamy • Light", 5.0, 12.0, 8.0),
        ("Caramel Macchiato", "250 kcal", "Caramel + Vanilla", 10.0, 35.0, 7.0),
        ("White Mocha", "400 kcal", "Very Sweet • Creamy", 18.0, 55.0, 10.0),
    ],
    "🧊  COLD COFFEE — MOST POPULAR IN PAKISTAN": [
        ("Iced Americano", "10 kcal", "Zero Sugar • Strong", 0.1, 1.0, 0.5),
        ("Cold Coffee", "120 kcal", "Pakistani Style • Milk + Ice", 4.0, 18.0, 6.0),
        ("Iced Latte", "130 kcal", "Cold Milk + Espresso", 5.0, 12.0, 8.0),
        ("Cold Brew", "15 kcal", "Smooth • No Sugar", 0.2, 2.0, 0.5),
        ("Iced Caramel Latte", "220 kcal", "Sweet Cold • Caramel", 8.0, 32.0, 7.0),
    ],
    "🍫  FRAPPUCCINO & BLENDED": [
        ("Mocha Frappuccino", "370 kcal", "Chocolate + Coffee", 15.0, 54.0, 5.0),
        ("Caramel Frappuccino", "380 kcal", "Caramel + Cream", 16.0, 56.0, 5.0),
        ("Vanilla Bean Frapp", "350 kcal", "Vanilla • Creamy", 14.0, 52.0, 5.0),
        ("Java Chip Frapp", "420 kcal", "Choco Chips", 19.0, 58.0, 6.0),
    ],
    "🍵  TEA & MATCHA": [
        ("Green Tea", "0 kcal", "Zero Calorie • Healthy", 0.0, 0.0, 0.0),
        ("Matcha Latte", "200 kcal", "Antioxidant • Milk", 7.0, 26.0, 8.0),
        ("Chai Tea Latte", "240 kcal", "Spicy • Sweet Milk", 8.0, 34.0, 7.0),
        ("Iced Green Tea", "5 kcal", "Refreshing • Zero Sugar", 0.0, 1.0, 0.0),
    ],
    "🍓  REFRESHERS & FRESH JUICE": [
        ("Strawberry Acai", "90 kcal", "Fruity • Low Cal", 0.1, 22.0, 0.0),
        ("Mango Dragonfruit", "100 kcal", "Tropical • Fresh", 0.2, 24.0, 0.2),
        ("Pink Drink", "140 kcal", "Coconut + Strawberry", 3.0, 25.0, 1.0),
        ("Fresh Orange Juice", "110 kcal", "Vitamin C • Fresh", 0.5, 26.0, 1.0),
    ],
}

for cat, drinks in menu_data.items():
    st.markdown(f"<div class='menu-cat'>{cat}</div>", unsafe_allow_html=True)
    cols = st.columns(len(drinks))
    for idx, (name, kcal, desc, f, c, p) in enumerate(drinks):
        with cols[idx]:
            current = st.session_state.get("selected_drink", "Cold Coffee")
            is_sel = (current == name)
            border = "2.5px solid #000" if is_sel else "1px solid #EDEDEA"
            bg = "#FFFBEB" if is_sel else "white"
            badge = "✓ SELECTED" if is_sel else "Select →"
            st.markdown(f'<div style="background:{bg}; border:{border}; border-radius:14px; padding:15px; text-align:center; min-height:110px;"><b style="font-size:13px;">{name}</b><br><span style="font-size:13px; font-weight:800;">{kcal}</span><br><span style="font-size:11px; color:#888;">{desc}</span></div>', unsafe_allow_html=True)
            if st.button(badge, key=f"menu_{cat}_{idx}", use_container_width=True):
                set_drink(name, f, c, p); st.rerun()

st.write("")

# ---------- MAIN ----------
left, right = st.columns([1, 1.25], gap="medium")
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### 01 — Your Drink: {st.session_state.get('selected_drink','Cold Coffee')}")
    st.markdown("<p style='color:#888; font-size:13px;'>Adjust from label or choose from menu above.</p>", unsafe_allow_html=True)
    fat = st.slider("Fat (g) — Milk / Cream", 0.0, 30.0, key="fat", step=0.5)
    carb = st.slider("Carbs (g) — Sugar / Syrup", 0.0, 100.0, key="carb", step=1.0)
    protein = st.slider("Protein (g) — Milk", 0.0, 30.0, key="protein", step=0.5)
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.write("**🥧 Macro Breakdown**")
    total = fat*9 + carb*4 + protein*4
    if total > 0:
        fat_pct = int(fat*9/total*100); carb_pct = int(carb*4/total*100); pro_pct = 100-fat_pct-carb_pct
        st.markdown(f"""
        <div style="font-size:12px;">● Fat — {fat*9:.0f} kcal ({fat_pct}%)</div>
        <div style="background:#EEE; height:8px; border-radius:10px; overflow:hidden; margin:4px 0 8px 0;"><div style="background:#000; width:{fat_pct}%; height:8px;"></div></div>
        <div style="font-size:12px;">● Carbs — {carb*4:.0f} kcal ({carb_pct}%)</div>
        <div style="background:#EEE; height:8px; border-radius:10px; overflow:hidden; margin:4px 0 8px 0;"><div style="background:#FFD966; width:{carb_pct}%; height:8px;"></div></div>
        <div style="font-size:12px;">● Protein — {protein*4:.0f} kcal ({pro_pct}%)</div>
        <div style="background:#EEE; height:8px; border-radius:10px; overflow:hidden; margin:4px 0 8px 0;"><div style="background:#4CAF50; width:{pro_pct}%; height:8px;"></div></div>
        """, unsafe_allow_html=True)
    st.divider()
    a, b = st.columns(2)
    with a:
        st.markdown(f"<div class='kpi'><b>ESTIMATED</b><span>{est_cal} kcal</span></div>", unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='kpi'><b>DAILY BUDGET</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    st.write("**Daily Budget — 2000 kcal Goal**")
    st.progress(min(int(est_cal/2000*100), 100))
    if st.button("🔄 Reset", use_container_width=True):
        set_drink("Cold Coffee", 4.0, 18.0, 6.0); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 02 — AI Verdict")
    st.markdown("<p style='color:#888; font-size:13px;'>Decision Tree Model • Trained & Deployed by Noor Ul Hassan Awan</p>", unsafe_allow_html=True)
    if not model_ok:
        st.error("Model file missing hai.")
    else:
        if st.button("✨ Predict My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            st.session_state.history.append((st.session_state.get('selected_drink'), est_cal))
            if pred == 1:
                conf = prob[1]*100; health = max(12, 100 - int(est_cal/2.2)); label = "High Calorie"
                color = "#B42318"; bg = "#FEF3F2"; border = "#FECDC2"; emoji = "⚠️"; title = f"High Calorie — {est_cal} kcal"
                desc = f"Your {st.session_state.get('selected_drink')} is over 150 kcal. Not ideal for daily use."
                tip = f"**Professional Swap:** Non-fat milk + Sugar-free syrup + No Whip. You will save {int(est_cal*0.38)} kcal. Daily ke liye Black Coffee ya Cold Brew best hai."
                verdict = "OCCASIONAL ONLY"; grade = "C Grade"
            else:
                conf = prob[0]*100; health = min(97, 100 - int(est_cal/5)); label = "Low Calorie"
                color = "#027A48"; bg = "#ECFDF3"; border = "#ABEFC6"; emoji = "✅"; title = f"Low Calorie — {est_cal} kcal"
                desc = f"Perfect! Your {st.session_state.get('selected_drink')} is under 150 kcal. Safe for daily use."
                tip = "**Professional Advice:** Great choice. Keep this routine. Protein zyada hai to workout ke baad bhi best hai."
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
            st.write(f"**Compare — {st.session_state.get('selected_drink')} vs Others**")
            comp = pd.DataFrame({"Drink": [st.session_state.get('selected_drink'), "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est_cal, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
            report = f"NutriSip International\nDEPLOYED BY NOOR UL HASSAN AWAN\nDate: {datetime.now().strftime('%d %B %Y')}\nDrink: {st.session_state.get('selected_drink')}\nCalories: {est_cal} | Result: {label} | Confidence: {conf:.1f}% | Health: {health}/100"
            st.download_button("⬇ Download Professional Report", report, file_name="NutriSip_Report.txt", use_container_width=True)
        else:
            st.markdown("""
            <div style="background:#FAFAF8; border:1.5px dashed #DDD; padding:32px; border-radius:14px; text-align:center;">
                <div style="font-size:42px;">☕</div>
                <div style="font-weight:900; font-size:16px;">Ready for Analysis?</div>
                <div style="color:#888; font-size:13px; margin-top:6px;">Menu se drink choose karo ya slider se values dalo.<br>Phir <b>Predict My Drink</b> dabao.</div>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            st.markdown("""
            **Why This is International Standard?**
            - 22 Drinks Full Cafe Menu — Hot, Cold, Frapp, Tea, Juice
            - Macro Breakdown + Comparison Chart
            - Health Score + Professional Advice
            - Clean Black / White / Gold Design — 100% Original
            """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div style="background:#000; color:white; padding:30px; border-radius:20px; margin-top:24px; display:flex; justify-content:space-between; align-items:center;">
    <div><div style="font-size:20px; font-weight:900;">NutriSip <span style="color:#FFD966;">International</span></div><div style="font-size:12px; color:#AAA; margin-top:4px;">Calorie Intelligence • Semester Project 2026</div></div>
    <div style="text-align:center;"><div style="font-size:10px; letter-spacing:2px; color:#AAA;">DEPLOYED BY</div><div style="font-size:17px; font-weight:900; color:#FFD966; margin-top:4px;">NOOR UL HASSAN AWAN</div><div style="font-size:12px; color:#AAA;">Lahore, Pakistan 🇵🇰</div></div>
    <div style="text-align:right; font-size:11px; color:#AAA; line-height:1.8;">Model: Decision Tree • 94.2%<br>Data: Starbucks Global Menu<br>© 2026 All Rights Reserved</div>
</div>
<p style="text-align:center; color:#999; font-size:11px; margin-top:12px;">Designed in Pakistan • Built for the World • Deployed by Noor Ul Hassan Awan</p>
""", unsafe_allow_html=True)
