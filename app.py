import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

st.set_page_config(page_title="NutriSip | Deployed by Noor Ul Hassan Awan", page_icon="☕", layout="wide", initial_sidebar_state="expanded")

for key, val in [("fat", 4.0), ("carb", 18.0), ("protein", 6.0), ("selected_drink", "Cold Coffee"), ("history", [])]:
    if key not in st.session_state:
        st.session_state[key] = val

def set_drink(name, f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p
    st.session_state.selected_drink = name

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: #FAFAF8; }
    .block-container { max-width: 1300px; padding-top: 0.6rem; }
    section[data-testid="stSidebar"] { background: #000 !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    section[data-testid="stSidebar"] .stButton > button { background: #1A1A1A !important; border: 1px solid #333 !important; color: white !important; height: 44px !important; border-radius: 12px !important; }
    section[data-testid="stSidebar"] .stButton > button:hover { background: #FFD966 !important; color: #000 !important; }
    .topbar { background: white; border: 1px solid #EDEDEA; border-radius: 16px; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center; }
    .logo-c { width: 46px; height: 46px; background: #000; color: #FFD966; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 900; }
    .deploy-top { background: #000; color: white; padding: 8px 16px; border-radius: 20px; font-size: 11px; font-weight: 800; }
    .hero { background: linear-gradient(115deg, #000 0%, #1A1A1A 100%); border-radius: 24px; padding: 42px 38px; color: white; margin-top: 14px; display: flex; justify-content: space-between; align-items: center; }
    .hero h1 { font-size: 62px; font-weight: 900; line-height: 0.95; letter-spacing: -2.5px; margin: 0; }
    .hero h1 span { color: #FFD966; }
    .hero p { color: #BBB; font-size: 15px; line-height: 1.7; max-width: 620px; margin-top: 16px; }
    .card { background: white; border: 1px solid #EDEDEA; border-radius: 20px; padding: 26px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
    .menu-cat { font-size: 11px; letter-spacing: 2.5px; font-weight: 800; color: #000; background: #FFD966; display: inline-block; padding: 6px 12px; border-radius: 20px; margin: 22px 0 12px 0; }
    .drink-img-card { background: white; border: 1px solid #EDEDEA; border-radius: 18px; padding: 0; overflow: hidden; text-align: center; transition: 0.2s; }
    .drink-img-card:hover { border: 2px solid #000; transform: translateY(-4px); box-shadow: 0 10px 25px rgba(0,0,0,0.08); }
    .drink-img-card img { width: 100%; height: 130px; object-fit: cover; }
    .drink-info { padding: 12px 10px; }
    .kpi { background: #FAFAF8; border: 1px solid #EDEDEA; border-radius: 12px; padding: 14px; }
    .kpi b { font-size: 11px; color: #888; } .kpi span { font-size: 26px; font-weight: 900; display: block; }
    .stButton > button { background: #000 !important; color: white !important; border-radius: 12px !important; border: none !important; font-weight: 700 !important; height: 52px !important; }
    .stSlider > div > div > div > div { background: #000 !important; }
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

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:8px 0;">
        <div style="width:72px; height:72px; background:#FFD966; color:#000; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:32px; font-weight:900; margin:0 auto;">N</div>
        <div style="font-size:20px; font-weight:900; margin-top:12px;">NUTRISIP</div>
        <div style="font-size:10px; letter-spacing:3px; color:#888;">INTERNATIONAL</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("### ☕ Cafe Menu — 22 Drinks")
    st.markdown("**Hot** (5) • **Cold** (5) • **Frapp** (4) • **Tea** (4) • **Juice** (4)")
    st.divider()
    st.markdown("""
    <div style="background:#FFD966; color:#000; padding:16px; border-radius:14px; text-align:center;">
        <div style="font-size:10px; letter-spacing:2px; font-weight:800;">DEPLOYED BY</div>
        <div style="font-size:16px; font-weight:900; margin-top:4px;">NOOR UL HASSAN AWAN</div>
        <div style="font-size:11px; margin-top:6px;">Lahore, Pakistan 🇵🇰<br>2026</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <div style="display:flex; align-items:center; gap:12px;">
        <div class="logo-c">N</div>
        <div><div style="font-size:19px; font-weight:900; line-height:1;">NutriSip <span style="font-weight:400; color:#999; font-size:13px;">International</span></div><div style="font-size:10px; letter-spacing:2px; color:#999; font-weight:700;">WITH REAL IMAGES • USA STYLE</div></div>
    </div>
    <div class="deploy-top">DEPLOYED BY NOOR UL HASSAN AWAN</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div>
        <div style="display:inline-block; background:#FFD966; color:#000; padding:6px 13px; border-radius:20px; font-size:11px; font-weight:800;">● NOW WITH REAL DRINK IMAGES • INTERNATIONAL DESIGN</div>
        <h1 style="margin-top:18px;">Know What<br>You <span>Drink.</span></h1>
        <p>Now with real images for every drink. Choose from our full cafe menu — Black Coffee, Cold Coffee, Frappuccino, Tea & Juice — and our AI will tell you if it's High or Low Calorie instantly.</p>
    </div>
    <div style="background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.12); border-radius:20px; padding:22px; min-width:270px; text-align:center;">
        <div style="font-size:46px;">📸</div>
        <div style="font-weight:900; font-size:17px; margin-top:6px;">With Real Images</div>
        <div style="font-size:12px; color:#AAA;">Every Drink Has a Photo</div>
        <div style="background:#FFD966; color:#000; padding:12px; border-radius:12px; margin-top:16px; font-weight:900;">DEPLOYED BY<br>NOOR UL HASSAN AWAN</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📋 Full Cafe Menu — With Real Images")

IMG_BLACK = "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400"
IMG_LATTE = "https://images.unsplash.com/photo-1511920170033-f8396924c348?w=400"
IMG_CAPPU = "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400"
IMG_CARAMEL = "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400"
IMG_COLD = "https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=400"
IMG_FRAPP = "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400"
IMG_TEA = "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400"
IMG_JUICE = "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400"

menu_data = {
    "☕  HOT COFFEE": [
        ("Black Coffee", "5 kcal", "Zero Sugar", IMG_BLACK, 0.1, 0.0, 0.3),
        ("Caffe Latte", "190 kcal", "Milk + Espresso", IMG_LATTE, 7.0, 15.0, 12.0),
        ("Cappuccino", "140 kcal", "Foamy • Light", IMG_CAPPU, 5.0, 12.0, 8.0),
        ("Caramel Macchiato", "250 kcal", "Caramel + Vanilla", IMG_CARAMEL, 10.0, 35.0, 7.0),
        ("White Mocha", "400 kcal", "Very Sweet", IMG_LATTE, 18.0, 55.0, 10.0),
    ],
    "🧊  COLD COFFEE": [
        ("Iced Americano", "10 kcal", "Zero Sugar", IMG_COLD, 0.1, 1.0, 0.5),
        ("Cold Coffee", "120 kcal", "Pakistani Style", IMG_COLD, 4.0, 18.0, 6.0),
        ("Iced Latte", "130 kcal", "Cold Milk", IMG_COLD, 5.0, 12.0, 8.0),
        ("Cold Brew", "15 kcal", "Smooth", IMG_BLACK, 0.2, 2.0, 0.5),
        ("Iced Caramel Latte", "220 kcal", "Sweet Cold", IMG_CARAMEL, 8.0, 32.0, 7.0),
    ],
    "🍫  FRAPPUCCINO": [
        ("Mocha Frappuccino", "370 kcal", "Chocolate", IMG_FRAPP, 15.0, 54.0, 5.0),
        ("Caramel Frappuccino", "380 kcal", "Caramel + Cream", IMG_FRAPP, 16.0, 56.0, 5.0),
        ("Vanilla Bean Frapp", "350 kcal", "Vanilla", IMG_FRAPP, 14.0, 52.0, 5.0),
        ("Java Chip Frapp", "420 kcal", "Choco Chips", IMG_FRAPP, 19.0, 58.0, 6.0),
    ],
    "🍵  TEA & MATCHA": [
        ("Green Tea", "0 kcal", "Zero Calorie", IMG_TEA, 0.0, 0.0, 0.0),
        ("Matcha Latte", "200 kcal", "Antioxidant", IMG_TEA, 7.0, 26.0, 8.0),
        ("Chai Tea Latte", "240 kcal", "Spicy Milk", IMG_TEA, 8.0, 34.0, 7.0),
        ("Iced Green Tea", "5 kcal", "Refreshing", IMG_TEA, 0.0, 1.0, 0.0),
    ],
    "🍓  REFRESHERS & JUICE": [
        ("Strawberry Acai", "90 kcal", "Fruity", IMG_JUICE, 0.1, 22.0, 0.0),
        ("Mango Dragonfruit", "100 kcal", "Tropical", IMG_JUICE, 0.2, 24.0, 0.2),
        ("Pink Drink", "140 kcal", "Coconut", IMG_JUICE, 3.0, 25.0, 1.0),
        ("Orange Juice", "110 kcal", "Vitamin C", IMG_JUICE, 0.5, 26.0, 1.0),
    ],
}

for cat, drinks in menu_data.items():
    st.markdown(f"<div class='menu-cat'>{cat}</div>", unsafe_allow_html=True)
    cols = st.columns(len(drinks))
    for idx, (name, kcal, desc, img, f, c, p) in enumerate(drinks):
        with cols[idx]:
            current = st.session_state.get("selected_drink", "Cold Coffee")
            is_sel = (current == name)
            border = "2.5px solid #000" if is_sel else "1px solid #EDEDEA"
            bg = "#FFFBEB" if is_sel else "white"
            badge = "✓ SELECTED" if is_sel else "Select →"
            st.markdown(f"""
            <div class="drink-img-card" style="border:{border}; background:{bg};">
                <img src="{img}" />
                <div class="drink-info">
                    <b style="font-size:13px;">{name}</b><br>
                    <span style="font-size:13px; font-weight:800;">{kcal}</span><br>
                    <span style="font-size:11px; color:#888;">{desc}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(badge, key=f"menu_{cat}_{idx}", use_container_width=True):
                set_drink(name, f, c, p); st.rerun()

st.write("")
left, right = st.columns([1, 1.25], gap="medium")
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### 01 — Your Drink: {st.session_state.get('selected_drink','Cold Coffee')}")
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat", step=0.5)
    carb = st.slider("Carbs (g)", 0.0, 100.0, key="carb", step=1.0)
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein", step=0.5)
    est_cal = int(fat*9 + carb*4 + protein*4)
    st.divider()
    a, b = st.columns(2)
    with a:
        st.markdown(f"<div class='kpi'><b>ESTIMATED</b><span>{est_cal} kcal</span></div>", unsafe_allow_html=True)
    with b:
        st.markdown(f"<div class='kpi'><b>DAILY BUDGET</b><span>{est_cal/2000*100:.1f}%</span></div>", unsafe_allow_html=True)
    st.progress(min(int(est_cal/2000*100), 100))
    if st.button("🔄 Reset", use_container_width=True):
        set_drink("Cold Coffee", 4.0, 18.0, 6.0); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 02 — AI Verdict")
    st.markdown("<p style='color:#888; font-size:13px;'>Deployed by Noor Ul Hassan Awan</p>", unsafe_allow_html=True)
    if not model_ok:
        st.error("Model file missing.")
    else:
        if st.button("✨ Predict My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            if pred == 1:
                conf = prob[1]*100; label = "High Calorie"
                color = "#B42318"; bg = "#FEF3F2"; border = "#FECDC2"; emoji = "⚠️"; title = f"High Calorie — {est_cal} kcal"
                desc = f"Your {st.session_state.get('selected_drink')} is over 150 kcal."
                tip = f"Swap: Non-fat milk + Sugar-free syrup lo, {int(est_cal*0.38)} kcal bachao."
                verdict = "OCCASIONAL ONLY"
            else:
                conf = prob[0]*100; label = "Low Calorie"
                color = "#027A48"; bg = "#ECFDF3"; border = "#ABEFC6"; emoji = "✅"; title = f"Low Calorie — {est_cal} kcal"
                desc = f"Perfect! Your {st.session_state.get('selected_drink')} is safe for daily use."
                tip = "Great choice, keep this routine."
                verdict = "DAILY SAFE"
            st.markdown(f"""
            <div style="background:{bg}; border:1.5px solid {border}; padding:20px; border-radius:14px;">
                <h3 style="color:{color}; margin:0;">{emoji} {title}</h3>
                <p style="font-size:13px; color:{color};">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")
            m1, m2, m3 = st.columns(3)
            m1.metric("Confidence", f"{conf:.1f}%")
            m2.metric("Health Score", f"{100-int(est_cal/3)}/100")
            m3.metric("Category", label)
            st.progress(int(conf))
            st.info(tip)
            comp = pd.DataFrame({"Drink": [st.session_state.get('selected_drink'), "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est_cal, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
            report = f"NutriSip International\nDEPLOYED BY NOOR UL HASSAN AWAN\nDrink: {st.session_state.get('selected_drink')}\nCalories: {est_cal} | Result: {label}"
            st.download_button("⬇ Download Report", report, file_name="NutriSip_Report.txt", use_container_width=True)
        else:
            st.markdown("""
            <div style="background:#FAFAF8; border:1.5px dashed #DDD; padding:32px; border-radius:14px; text-align:center;">
                <div style="font-size:42px;">☕</div>
                <div style="font-weight:900;">Ready for Analysis?</div>
                <div style="color:#888; font-size:13px;">Menu se drink choose karo ya slider se values dalo.</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background:#000; color:white; padding:30px; border-radius:20px; margin-top:24px; display:flex; justify-content:space-between; align-items:center;">
    <div><div style="font-size:20px; font-weight:900;">NutriSip <span style="color:#FFD966;">International</span></div><div style="font-size:12px; color:#AAA;">Semester Project 2026</div></div>
    <div style="text-align:center;"><div style="font-size:10px; letter-spacing:2px; color:#AAA;">DEPLOYED BY</div><div style="font-size:17px; font-weight:900; color:#FFD966;">NOOR UL HASSAN AWAN</div><div style="font-size:12px; color:#AAA;">Lahore, Pakistan 🇵🇰</div></div>
    <div style="text-align:right; font-size:11px; color:#AAA;">Model: Decision Tree • 94.2%<br>© 2026 All Rights Reserved</div>
</div>
""", unsafe_allow_html=True)
