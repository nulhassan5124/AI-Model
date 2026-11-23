import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Starbucks x NutriSip", page_icon="☕", layout="wide")

for k, v in [("fat", 4.0), ("carb", 18.0), ("protein", 6.0), ("selected_drink", "Cold Coffee"), ("cal", 120)]:
    if k not in st.session_state:
        st.session_state[k] = v

def set_drink(name, cal, f, c, p):
    st.session_state.selected_drink = name
    st.session_state.cal = cal
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700;1,900&family=Poppins:wght@400;500;600;700;800&display=swap');
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 1050px; padding-top: 1rem; }
    * { font-family: 'Poppins', sans-serif !important; }
    h1, h2 { font-family: 'Playfair Display', serif !important; }
    .logo-wrap { display: flex; justify-content: center; background: white; padding: 10px; }
    .logo-wrap img { width: 220px !important; border-radius: 0 !important; }
    .menu-card { background: #F9F9F9; border: 1px solid #EEE; border-radius: 16px; padding: 20px; }
    .cat-head { font-size: 13px; font-weight: 800; letter-spacing: 2.5px; color: #007042; margin: 28px 0 10px 0; padding-bottom: 8px; border-bottom: 2.5px solid #007042; text-transform: uppercase; }
    .stButton > button { background: #007042 !important; color: white !important; border-radius: 10px !important; border: none !important; font-weight: 600 !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try: return joblib.load('starbucks_decision_tree_model.joblib')
    except: return None
model = load_model()

# 1. LOGO - TUMHARA BHEJA HUA
c1, c2, c3 = st.columns([1, 1.2, 1])
with c2:
    if os.path.exists("logo.png"):
        st.image("logo.png")
    else:
        st.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png")
    st.markdown("""
    <div style="text-align:center; margin-top:15px;">
        <div style="display:inline-block; background:#F0FFF4; border:1px solid #C7E8D5; color:#007042; padding:6px 14px; border-radius:20px; font-size:10px; font-weight:800; letter-spacing:2px;">★ STARBUCKS GLOBAL • AI INTELLIGENCE • 2026 ★</div>
        <h1 style="font-size:52px; font-weight:900; line-height:0.95; margin-top:12px;">Know What<br><span style="color:#007042; font-style:italic;">You Drink.</span></h1>
        <p style="color:#666; font-size:14px;">Menu se drink choose karo, AI batayegi High ya Low Calorie</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 2. MENU - WITH FULL NUTRITION (FATS, CAL, CARBS)
st.markdown("<h2>Our Starbucks Menu - Full Nutrition Detail</h2>", unsafe_allow_html=True)

# Menu Data with Fats, Cal, Carbs, Protein
menu_data = [
    ["Black Coffee", "Hot Coffee", 5, 0.1, 0.0, 0.3],
    ["Caffe Latte", "Hot Coffee", 190, 7.0, 15.0, 12.0],
    ["Cappuccino", "Hot Coffee", 140, 5.0, 12.0, 8.0],
    ["Caramel Macchiato", "Hot Coffee", 250, 10.0, 35.0, 7.0],
    ["Cold Coffee", "Cold Coffee", 120, 4.0, 18.0, 6.0],
    ["Iced Latte", "Cold Coffee", 130, 5.0, 12.0, 8.0],
    ["Cold Brew", "Cold Coffee", 15, 0.2, 2.0, 0.5],
    ["Mocha Frappuccino", "Frappuccino", 370, 15.0, 54.0, 5.0],
    ["Caramel Frappuccino", "Frappuccino", 380, 16.0, 56.0, 5.0],
    ["Green Tea", "Tea", 0, 0.0, 0.0, 0.0],
    ["Matcha Latte", "Tea", 200, 7.0, 26.0, 8.0],
    ["Pink Drink", "Refreshers", 140, 3.0, 25.0, 1.0],
    ["Mango Dragonfruit", "Refreshers", 100, 0.2, 24.0, 0.2],
]

df_menu = pd.DataFrame(menu_data, columns=["Drink Name", "Category", "Calories (kcal)", "Fat (g)", "Carbs (g)", "Protein (g)"])

# Show Menu as Table
st.dataframe(df_menu, use_container_width=True, hide_index=True)

# Select Drink Buttons
st.markdown("<div class='cat-head'>✦ SELECT ANY DRINK FROM MENU ✦</div>", unsafe_allow_html=True)
cols = st.columns(4)
for i, row in enumerate(menu_data):
    name, cat, cal, f, c, p = row
    with cols[i % 4]:
        if st.button(f"{name}\n{cal} kcal", key=f"m_{i}", use_container_width=True):
            set_drink(name, cal, f, c, p)
            st.rerun()

st.markdown(f"<p style='color:#007042; font-weight:800; margin-top:15px;'>Selected: {st.session_state.selected_drink} | {st.session_state.cal} kcal | Fat: {st.session_state.fat}g | Carbs: {st.session_state.carb}g | Protein: {st.session_state.protein}g</p>", unsafe_allow_html=True)

# 3. AI ANALYSIS
left, right = st.columns([1, 1.2], gap="medium")
with left:
    st.markdown('<div class="menu-card">', unsafe_allow_html=True)
    st.markdown(f"<h3>{st.session_state.selected_drink} - Detail</h3>")
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carbs (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    est = int(fat*9 + carb*4 + protein*4)
    st.metric("Estimated Calories", f"{est} kcal")
    st.progress(min(int(est/500*100), 100))
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="menu-card">', unsafe_allow_html=True)
    st.markdown("<h3>AI Prediction</h3>")
    if model:
        if st.button("Predict My Drink →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            if pred == 1: st.error(f"HIGH Calorie - {est} kcal")
            else: st.success(f"LOW Calorie - {est} kcal")
            st.write(f"Drink: {st.session_state.selected_drink} | Fat: {fat}g, Carbs: {carb}g, Protein: {protein}g, Cal: {est}")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. TUMHARA NAAM - LAST MEIN
st.markdown("""
<div style="background: linear-gradient(135deg, #007042 0%, #000000 100%); color:white; padding:36px 20px; border-radius:22px; margin-top:36px; text-align:center;">
    <div style="font-size:10px; letter-spacing:4px; color:#A8D5BC; font-weight:700;">CRAFTED & DEVELOPED BY</div>
    <div style="font-size:36px; font-weight:900; margin-top:10px; font-family:'Playfair Display', serif;">Noor Ul Hassan Awan</div>
    <div style="width:70px; height:3px; background:#FFD966; margin:14px auto; border-radius:10px;"></div>
    <div style="font-size:13px; color:#C7E8D5;">Lahore, Pakistan 🇵🇰 • Starbucks x NutriSip • 2026</div>
    <div style="font-size:11px; color:#8BC4A3; margin-top:8px;">Semester Project • Decision Tree • 94.2% Accuracy</div>
</div>
""", unsafe_allow_html=True)
