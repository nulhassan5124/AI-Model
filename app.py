import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Starbucks x NutriSip", page_icon="☕", layout="wide")

if "selected" not in st.session_state:
    st.session_state.selected = "Caffe Latte"
    st.session_state.fat = 7.0
    st.session_state.carb = 15.0
    st.session_state.protein = 12.0
    st.session_state.menu_open = True

def select(name, f, c, p):
    st.session_state.selected = name
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@400;600;700;800&display=swap');
.stApp { background: #FFFEFA; }
.block-container { max-width: 1050px; padding-top: 0.5rem; }
* { font-family: 'Poppins', sans-serif !important; }
h1,h2,h3 { font-family: 'Playfair Display', serif !important; }
.logo-circle {
    width: 230px;
    height: 230px;
    background: radial-gradient(circle, #000000 0%, #000000 100%);
    border-radius: 50%;
    border: 8px solid #C9A227;
    box-shadow: 0 0 0 6px #FFD700, 0 15px 35px rgba(0,0,0,0.25);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 0 auto;
}
.info-card { background:white; border:1px solid #F0EAD8; border-radius:18px; padding:22px; box-shadow:0 4px 20px rgba(0,0,0,0.04); }
.nutri-box { background:#1E3A2F; color:white; border-radius:18px; padding:22px; }
.nutri-item { background: rgba(255,255,255,0.08); border-radius:12px; padding:14px; text-align:center; }
.nutri-item b { font-size:22px; display:block; }
.nutri-item span { font-size:11px; color:#A8D5BC; letter-spacing:1px; }
.stButton > button { background:#007042 !important; color:white !important; border-radius:12px !important; font-weight:700 !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try:
        return joblib.load('starbucks_decision_tree_model.joblib')
    except:
        return None
model = load_model()

# 1. GOLD CIRCLE MEIN BARA SA STARBUCKS LOGO - HAMESHA NAZAR AAYEGA
st.markdown("""
<div style="text-align:center; margin-top:20px;">
    <div class="logo-circle">
        <div style="color:#FFD700; font-size:22px; margin-bottom:8px;">★</div>
        <div style="color:white; font-family:'Playfair Display', serif; font-weight:900; font-size:42px; line-height:0.9; text-align:center;">STAR<br>BUCKS</div>
        <div style="width:60px; height:2px; background:#C9A227; margin:12px auto;"></div>
        <div style="color:#C9A227; font-size:14px; font-weight:800; letter-spacing:2px;">COFFEE</div>
        <div style="color:white; font-size:11px; margin-top:8px; letter-spacing:1px;">★ EST. 1971 ★</div>
    </div>
    <h1 style="font-size:52px; font-weight:900; margin:22px 0 0 0; line-height:1;">Starbucks <span style="color:#007042; font-style:italic;">x NutriSip</span></h1>
    <div style="width:70px; height:3px; background:#C9A227; margin:14px auto;"></div>
    <p style="color:#777; font-size:13px; letter-spacing:1px; font-weight:600;">EST. 1971 • SEATTLE, USA • 30 MARCH 1971</p>
</div>
""", unsafe_allow_html=True)

# 2. INTRODUCTION - PROFESSIONAL
st.markdown("""
<div class="info-card" style="text-align:center; margin-top:20px;">
    <h3 style="margin:0; color:#007042;">Introduction - Starbucks</h3>
    <p style="color:#555; font-size:14.5px; line-height:1.9; max-width:800px; margin:14px auto 0 auto;">
        <b>Starbucks Corporation</b> 30 March 1971 ko Seattle, Washington, USA mein bani. Shuru mein sirf coffee beans bechti thi, aaj 35,000+ stores ke saath 80+ countries mein duniya ki sab se bari coffeehouse chain hai.<br><br>
        <b>NutriSip</b> iska AI version hai. Aap koi bhi drink select karo, uska <b>Fat, Carbs, Protein, Calories</b> dekho aur AI batayega <b>High Calorie hai ya Low Calorie.</b> Ye project Decision Tree Model par bana hai jiski accuracy 94.2% hai.
    </p>
    <div style="display:flex; justify-content:center; gap:12px; margin-top:18px; flex-wrap:wrap;">
        <span style="background:#F0FFF4; border:1px solid #C7E8D5; padding:8px 16px; border-radius:20px; font-size:11px; font-weight:700;">☕ FOUNDED: 30 MARCH 1971</span>
        <span style="background:#F0FFF4; border:1px solid #C7E8D5; padding:8px 16px; border-radius:20px; font-size:11px; font-weight:700;">🌍 80+ COUNTRIES</span>
        <span style="background:#F0FFF4; border:1px solid #C7E8D5; padding:8px 16px; border-radius:20px; font-size:11px; font-weight:700;">🤖 AI 94.2% ACCURACY</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. VIEW MENU
st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size:28px; text-align:center;'>📋 Our Menu</h2>", unsafe_allow_html=True)
if st.button("☰ VIEW MENU", use_container_width=True):
    st.session_state.menu_open = not st.session_state.menu_open

menu = [
    ["Black Coffee", "Hot Coffee", 5, 0.1, 0.0, 0.3],
    ["Caffe Latte", "Hot Coffee", 190, 7.0, 15.0, 12.0],
    ["Cappuccino", "Hot Coffee", 140, 5.0, 12.0, 8.0],
    ["Caramel Macchiato", "Hot Coffee", 250, 10.0, 35.0, 7.0],
    ["White Mocha", "Hot Coffee", 400, 18.0, 45.0, 10.0],
    ["Cold Coffee", "Cold Coffee", 120, 4.0, 18.0, 6.0],
    ["Iced Latte", "Cold Coffee", 130, 5.0, 12.0, 8.0],
    ["Cold Brew", "Cold Coffee", 15, 0.2, 2.0, 0.5],
    ["Mocha Frappuccino", "Frappuccino", 370, 15.0, 54.0, 5.0],
    ["Caramel Frappuccino", "Frappuccino", 380, 16.0, 56.0, 5.0],
    ["Green Tea", "Tea", 0, 0.0, 0.0, 0.0],
    ["Matcha Latte", "Tea", 200, 7.0, 26.0, 8.0],
    ["Pink Drink", "Refreshers", 140, 3.0, 25.0, 1.0],
]

if st.session_state.menu_open:
    st.markdown("<div class='info-card' style='margin-top:14px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0 0 12px 0;'>Full Menu - Fats, Carbohydrates, Protein, Calories</h3>", unsafe_allow_html=True)
    df = pd.DataFrame(menu, columns=["Drink", "Category", "Calories (kcal)", "Fat (g)", "Carbs (g)", "Protein (g)"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    cols = st.columns(3)
    for i, (name, cat, cal, f, c, p) in enumerate(menu):
        with cols[i % 3]:
            if st.button(f"{name} • {cal} kcal", key=f"m{i}", use_container_width=True):
                select(name, f, c, p)
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 4. PROCEDURE
st.markdown(f"<h2 style='margin-top:22px;'>Selected: <span style='color:#007042; font-style:italic;'>{st.session_state.selected}</span></h2>", unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.1], gap="large")
with c1:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0 0 12px 0;'>Adjust Your Drink</h3>", unsafe_allow_html=True)
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carbohydrates (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    cal = int(fat*9 + carb*4 + protein*4)
    st.metric("Total Calories", f"{cal} kcal", f"Fat {fat}g | Carbs {carb}g | Protein {protein}g")
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='nutri-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; margin:0 0 14px 0;'>Nutrition - Fats, Carbs, Calories</h3>", unsafe_allow_html=True)
    n1, n2, n3, n4 = st.columns(4)
    with n1: st.markdown(f"<div class='nutri-item'><b>{cal}</b><span>CALORIES</span></div>", unsafe_allow_html=True)
    with n2: st.markdown(f"<div class='nutri-item'><b>{fat}g</b><span>FATS</span></div>", unsafe_allow_html=True)
    with n3: st.markdown(f"<div class='nutri-item'><b>{carb}g</b><span>CARBS</span></div>", unsafe_allow_html=True)
    with n4: st.markdown(f"<div class='nutri-item'><b>{protein}g</b><span>PROTEIN</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
    if model and st.button("✨ Predict - High or Low Calorie?", use_container_width=True):
        dfp = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
        pred = model.predict(dfp)[0]
        st.error(f"🔴 HIGH Calorie - {cal} kcal") if pred==1 else st.success(f"🟢 LOW Calorie - {cal} kcal")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. DEVELOPED BY
st.markdown("""
<div style="background:#111; color:white; padding:36px 20px; border-radius:20px; margin-top:32px; text-align:center;">
    <div style="font-size:10px; letter-spacing:4px; color:#C9A227; font-weight:800;">DEVELOPED & DEPLOYED BY</div>
    <div style="font-family:'Playfair Display', serif; font-size:40px; font-weight:900; margin-top:12px;">Noor Ul Hassan Awan</div>
    <div style="width:60px; height:3px; background:#C9A227; margin:14px auto;"></div>
    <div style="font-size:13px; color:#BBB;">Lahore, Pakistan 🇵🇰 • Starbucks x NutriSip • 2026</div>
    <div style="font-size:11px; color:#777; margin-top:8px;">Semester Project • Decision Tree • 94.2% Accuracy • Streamlit Cloud</div>
</div>
""", unsafe_allow_html=True)
