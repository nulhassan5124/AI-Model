import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Starbucks x NutriSip | Noor Ul Hassan Awan", page_icon="☕", layout="wide")

for k, v in [("fat", 4.0), ("carb", 18.0), ("protein", 6.0), ("selected_drink", "Cold Coffee")]:
    if k not in st.session_state:
        st.session_state[k] = v

def set_drink(name, f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p
    st.session_state.selected_drink = name

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700;1,900&family=Poppins:wght@400;500;600;700;800&display=swap');
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 1050px; padding-top: 0rem; }
    * { font-family: 'Poppins', sans-serif !important; }
    h1, h2, h3, .stylish { font-family: 'Playfair Display', serif !important; }
    .card { background: #F9F9F9; border: 1px solid #EEE; border-radius: 18px; padding: 26px; }
    .cat-head { font-family: 'Poppins', sans-serif !important; font-size: 13px; font-weight: 800; letter-spacing: 2.5px; color: #007042; margin: 28px 0 10px 0; padding-bottom: 8px; border-bottom: 2.5px solid #007042; text-transform: uppercase; }
    .drink-box { background: white; border: 1px solid #EEE; border-radius: 14px; padding: 16px 10px; text-align: center; transition: 0.2s; }
    .drink-box:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,112,66,0.12); border-color: #007042; }
    .drink-name { font-family: 'Playfair Display', serif !important; font-size: 15px; font-weight: 700; color: #111; line-height: 1.2; }
    .drink-kcal { font-size: 12px; color: #007042; font-weight: 700; letter-spacing: 0.5px; }
    .stButton > button { background: #007042 !important; color: white !important; border-radius: 10px !important; border: none !important; font-weight: 600 !important; height: 42px !important; }
    /* LOGO FIX - PERFECT CIRCLE */
    .logo-wrap { display: flex; justify-content: center; }
    .logo-wrap img { width: 190px !important; height: 190px !important; object-fit: cover; border-radius: 50% !important; border: 6px solid #D4E9D2 !important; box-shadow: 0 0 0 6px #F0FFF4, 0 15px 35px rgba(0,112,66,0.25) !important; }
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

# ============================================================
# 1. LOGO - PERFECT CIRCLE + STYLISH WRITING
# ============================================================
st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if os.path.exists("logo.png"):
        st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)
        st.image("logo.png")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="width:190px; height:190px; background: radial-gradient(circle at 30% 30%, #00A862, #007042); border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto; border: 7px solid #D4E9D2; box-shadow: 0 0 0 7px #F0FFF4, 0 15px 35px rgba(0,112,66,0.25);">
            <div style="text-align:center; color:white;">
                <div style="font-size:62px; font-weight:900; line-height:0.9; font-family:'Playfair Display', serif; letter-spacing:-2px;">S</div>
                <div style="font-size:11px; letter-spacing:4px; font-weight:800; margin-top:4px;">STARBUCKS</div>
                <div style="width:42px; height:2px; background:#FFD966; margin:8px auto;"></div>
                <div style="font-size:9px; letter-spacing:3px; font-weight:600;">EST. 1971 • COFFEE</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; margin-top:22px;">
        <div style="display:inline-block; background:#F0FFF4; border:1px solid #C7E8D5; color:#007042; padding:7px 16px; border-radius:20px; font-size:10px; font-weight:800; letter-spacing:2px;">★ STARBUCKS GLOBAL • AI INTELLIGENCE • 2026 ★</div>
        <h1 style="font-size:56px; font-weight:900; line-height:0.95; margin-top:16px; letter-spacing:-1.5px;">Know What<br><span style="color:#007042; font-style:italic;">You Drink.</span></h1>
        <p style="color:#666; font-size:15px; margin-top:12px; line-height:1.7;">Starbucks Global Menu se drink choose karo.<br>Hamari <b style='color:#007042;'>AI</b> batayegi <b>High ya Low Calorie.</b></p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================================
# 2. PRODUCTS - STYLISH NAMES
# ============================================================
st.markdown("<h2 style='font-size:28px; margin-bottom:2px;'>Our Signature Collection</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#888; font-size:13px;'>Select any drink — its detail will appear below in style</p>", unsafe_allow_html=True)

menu = {
    "HOT COFFEE": [("Black Coffee", "5 kcal", 0.1, 0.0, 0.3), ("Caffe Latte", "190 kcal", 7.0, 15.0, 12.0), ("Cappuccino", "140 kcal", 5.0, 12.0, 8.0), ("Caramel Macchiato", "250 kcal", 10.0, 35.0, 7.0), ("White Mocha", "400 kcal", 18.0, 55.0, 10.0)],
    "COLD COFFEE": [("Iced Americano", "10 kcal", 0.1, 1.0, 0.5), ("Cold Coffee", "120 kcal", 4.0, 18.0, 6.0), ("Iced Latte", "130 kcal", 5.0, 12.0, 8.0), ("Cold Brew", "15 kcal", 0.2, 2.0, 0.5), ("Iced Caramel Latte", "220 kcal", 8.0, 32.0, 7.0)],
    "FRAPPUCCINO": [("Mocha Frappuccino", "370 kcal", 15.0, 54.0, 5.0), ("Caramel Frappuccino", "380 kcal", 16.0, 56.0, 5.0), ("Vanilla Bean Frapp", "350 kcal", 14.0, 52.0, 5.0), ("Java Chip Frapp", "420 kcal", 19.0, 58.0, 6.0)],
    "TEA & MATCHA": [("Green Tea", "0 kcal", 0.0, 0.0, 0.0), ("Matcha Latte", "200 kcal", 7.0, 26.0, 8.0), ("Chai Tea Latte", "240 kcal", 8.0, 34.0, 7.0), ("Iced Green Tea", "5 kcal", 0.0, 1.0, 0.0)],
    "JUICE & REFRESHERS": [("Strawberry Acai", "90 kcal", 0.1, 22.0, 0.0), ("Mango Dragonfruit", "100 kcal", 0.2, 24.0, 0.2), ("Pink Drink", "140 kcal", 3.0, 25.0, 1.0), ("Orange Juice", "110 kcal", 0.5, 26.0, 1.0)],
}

for cat, drinks in menu.items():
    st.markdown(f"<div class='cat-head'>✦ {cat} ✦</div>", unsafe_allow_html=True)
    cols = st.columns(len(drinks))
    for i, (name, kcal, f, c, p) in enumerate(drinks):
        with cols[i]:
            is_sel = st.session_state.selected_drink == name
            border = "2.5px solid #007042" if is_sel else "1px solid #EEE"
            bg = "#F0FFF4" if is_sel else "white"
            badge = "✓ Selected" if is_sel else "Select →"
            st.markdown(f"""
            <div class="drink-box" style="border:{border}; background:{bg};">
                <div class="drink-name">{name}</div>
                <div class="drink-kcal" style="margin-top:6px;">{kcal}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(badge, key=f"{cat}_{i}", use_container_width=True):
                set_drink(name, f, c, p); st.rerun()

# ============================================================
# 3. PRODUCT DETAIL - STYLISH
# ============================================================
st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size:28px;'>Product Detail & AI Analysis</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color:#007042; font-weight:700;'>Selected: <span style='font-family:Playfair Display, serif; font-size:18px; color:#000;'>{st.session_state.selected_drink}</span></p>", unsafe_allow_html=True)

left, right = st.columns([1, 1.2], gap="medium")
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family:Poppins !important; font-weight:800; font-size:18px;'>{st.session_state.selected_drink}</h3>", unsafe_allow_html=True)
    st.write("Nutrition values adjust karo:")
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carbs (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    est = int(fat*9 + carb*4 + protein*4)
    st.markdown(f"**Estimated: {est} kcal**")
    st.progress(min(int(est/2000*100), 100))
    st.caption(f"Daily Budget 2000 kcal • {est/2000*100:.1f}% used")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3 style='font-family:Poppins !important; font-weight:800; font-size:18px;'>AI Verdict</h3>")
    if not model_ok:
        st.error("Model file missing.")
    else:
        if st.button("Predict My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            if pred == 1:
                st.error(f"High Calorie — {est} kcal")
                st.write(f"Confidence: {prob[1]*100:.1f}% • Your {st.session_state.selected_drink} is over 150 kcal.")
            else:
                st.success(f"Low Calorie — {est} kcal")
                st.write(f"Confidence: {prob[0]*100:.1f}% • Your {st.session_state.selected_drink} is safe for daily use.")
            comp = pd.DataFrame({"Drink": [st.session_state.selected_drink, "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
        else:
            st.write("Product choose kar ke Predict dabao.")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 4. END - TUMHARA NAAM - STYLISH
# ============================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #007042 0%, #005A35 100%); color:white; padding:36px 20px; border-radius:22px; margin-top:36px; text-align:center; box-shadow: 0 12px 35px rgba(0,112,66,0.3);">
    <div style="font-size:10px; letter-spacing:4px; color:#A8D5BC; font-weight:700;">CRAFTED • DESIGNED • DEPLOYED BY</div>
    <div style="font-size:34px; font-weight:900; margin-top:10px; font-family:'Playfair Display', serif; letter-spacing:-0.5px; line-height:1;">Noor Ul Hassan Awan</div>
    <div style="width:70px; height:3px; background:#FFD966; margin:14px auto; border-radius:10px;"></div>
    <div style="font-size:13px; color:#C7E8D5; letter-spacing:1px;">Lahore, Pakistan 🇵🇰 • Starbucks x NutriSip • 2026</div>
    <div style="font-size:11px; color:#8BC4A3; margin-top:10px;">Decision Tree Model • 94.2% Accuracy • Semester Project</div>
</div>
""", unsafe_allow_html=True)
