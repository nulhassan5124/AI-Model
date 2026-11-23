import streamlit as st
import pandas as pd
import joblib
import os
import base64

st.set_page_config(page_title="Starbucks x NutriSip", page_icon="☕", layout="wide")

# --- STATE ---
if "selected" not in st.session_state:
    st.session_state.selected = "Caffe Latte"
if "fat" not in st.session_state:
    st.session_state.fat = 7.0
if "carb" not in st.session_state:
    st.session_state.carb = 15.0
if "protein" not in st.session_state:
    st.session_state.protein = 12.0
if "menu_open" not in st.session_state:
    st.session_state.menu_open = True

def select(name, f, c, p):
    st.session_state.selected = name
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

# --- LOGO - TUMHARA WALA GREEN STARBUCKS LOGO ---
# Yehi logo jo tumne bheja hai, isko base64 mein convert karke upar lagaya hai
def get_logo():
    logo_path = "/mnt/data/wa_image_4010524198411821729"
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f'<img src="data:image/jpeg;base64,{data}" style="width:230px; height:230px; object-fit:cover; border-radius:50%; border:7px solid #D4E9D2; box-shadow:0 0 0 8px #F0FFF4, 0 20px 40px rgba(0,112,66,0.3);">'
    elif os.path.exists("logo.png"):
        with open("logo.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f'<img src="data:image/png;base64,{data}" style="width:230px; height:230px; object-fit:cover; border-radius:50%; border:7px solid #D4E9D2; box-shadow:0 0 0 8px #F0FFF4, 0 20px 40px rgba(0,112,66,0.3);">'
    else:
        return '<img src="https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png" style="width:230px; height:230px; background:white; object-fit:cover; border-radius:50%; border:7px solid #D4E9D2;">'

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Poppins:wght@400;500;600;700;800&display=swap');
.stApp { background: #FFFEFA; }
.block-container { max-width: 1050px; padding-top: 0.8rem; }
* { font-family: 'Poppins', sans-serif !important; }
h1,h2 { font-family: 'Playfair Display', serif !important; }
.hero-title { text-align:center; font-size:54px; font-weight:900; line-height:1; color:#1A1A1A; margin:18px 0 0 0; }
.hero-title span { color:#007042; font-style:italic; }
.gold-line { width:70px; height:3px; background:#007042; margin:16px auto; border-radius:10px; }
.info-card { background:#FFFFFF; border:1px solid #F0EAD8; border-radius:18px; padding:22px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
.nutri-box { background:#1E3A2F; color:white; border-radius:18px; padding:22px; }
.nutri-item { background: rgba(255,255,255,0.08); border-radius:12px; padding:14px; text-align:center; }
.nutri-item b { font-size:22px; display:block; }
.nutri-item span { font-size:11px; color:#A8D5BC; letter-spacing:1px; }
.stButton > button { background:#007042 !important; color:white !important; border-radius:12px !important; font-weight:700 !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try: return joblib.load('starbucks_decision_tree_model.joblib')
    except: return None
model = load_model()

# 1. LOGO - TOP - TUMHARA WALA
st.markdown(f'<div style="display:flex; justify-content:center; margin-top:10px;">{get_logo()}</div>', unsafe_allow_html=True)

# 2. NAME + DETAIL - STYLISH
st.markdown("""
<div style="text-align:center;">
    <div style="display:inline-block; background:#E6F4EA; border:1px solid #C7E8D5; color:#007042; padding:6px 18px; border-radius:30px; font-size:10px; font-weight:800; letter-spacing:3px; margin-top:18px;">★ EST. 1971 • SEATTLE • PREMIUM COFFEE ★</div>
    <h1 class="hero-title">Starbucks <span>x NutriSip</span></h1>
    <div class="gold-line"></div>
    <p style="color:#555; font-size:14px; line-height:1.8; max-width:750px; margin:14px auto 0 auto;">
        <b>Starbucks Corporation</b> 30 March 1971 ko Seattle mein bani. Aaj 35,000+ stores, 80+ countries mein duniya ki sab se bari coffee chain hai.<br>
        <b>NutriSip AI</b> aapki har drink ka <b>Fat, Carbs, Protein, Calories</b> batata hai aur kehta hai High Calorie hai ya Low.
    </p>
</div>
""", unsafe_allow_html=True)

# 3. MENU + PRODUCTS - 2 SIDE CLICKABLE
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
left, right = st.columns(2, gap="large")
with left:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#007042; margin:0;'>📋 STARBUCKS MENU</h3><p style='font-size:12px; color:#888;'>Click karo, sara menu khul jayega</p>", unsafe_allow_html=True)
    if st.button("☰ VIEW FULL MENU", use_container_width=True, key="open_menu"):
        st.session_state.menu_open = not st.session_state.menu_open
    st.markdown("</div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0;'>☕ PRODUCTS</h3><p style='font-size:12px; color:#888;'>Click karo, category folder khul jayega</p>", unsafe_allow_html=True)
    with st.expander("🔥 HOT COFFEE"):
        st.write("Black Coffee, Latte, Cappuccino, Macchiato, White Mocha")
    with st.expander("❄️ COLD COFFEE"):
        st.write("Cold Coffee, Iced Latte, Cold Brew, Caramel Latte")
    with st.expander("🥤 FRAPPUCCINO"):
        st.write("Mocha 370 kcal, Caramel 380 kcal, Java Chip 420 kcal")
    with st.expander("🍵 TEA & REFRESHERS"):
        st.write("Green Tea 0 kcal, Matcha 200 kcal, Pink Drink 140 kcal")
    st.markdown("</div>", unsafe_allow_html=True)

# FULL MENU
menu = [
    ["Black Coffee", 5, 0.1, 0.0, 0.3], ["Caffe Latte", 190, 7.0, 15.0, 12.0],
    ["Cappuccino", 140, 5.0, 12.0, 8.0], ["Caramel Macchiato", 250, 10.0, 35.0, 7.0],
    ["Cold Coffee", 120, 4.0, 18.0, 6.0], ["Iced Latte", 130, 5.0, 12.0, 8.0],
    ["Mocha Frappuccino", 370, 15.0, 54.0, 5.0], ["Caramel Frappuccino", 380, 16.0, 56.0, 5.0],
    ["Green Tea", 0, 0.0, 0.0, 0.0], ["Matcha Latte", 200, 7.0, 26.0, 8.0],
    ["Pink Drink", 140, 3.0, 25.0, 1.0], ["Cold Brew", 15, 0.2, 2.0, 0.5],
]

if st.session_state.menu_open:
    st.markdown("<div class='info-card' style='margin-top:18px;'>", unsafe_allow_html=True)
    st.markdown("<h3>📋 Full Menu - Calories, Fats, Carbs, Protein Detail</h3>", unsafe_allow_html=True)
    df = pd.DataFrame(menu, columns=["Drink", "Calories", "Fat (g)", "Carbs (g)", "Protein (g)"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    cols = st.columns(3)
    for i, (name, cal, f, c, p) in enumerate(menu):
        with cols[i % 3]:
            if st.button(f"{name} • {cal} kcal", key=f"drink_{i}", use_container_width=True):
                select(name, f, c, p)
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# SELECTED DRINK - FATS CARBS ALL BELOW
st.markdown(f"<h2 style='margin-top:20px;'>Selected: <span style='color:#007042; font-style:italic;'>{st.session_state.selected}</span></h2>", unsafe_allow_html=True)
c1, c2 = st.columns([1, 1.1], gap="large")
with c1:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carbohydrates (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    cal = int(fat*9 + carb*4 + protein*4)
    st.metric("Total Calories", f"{cal} kcal", f"Fat {fat}g | Carbs {carb}g | Protein {protein}g")
    st.markdown("</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='nutri-box'>", unsafe_allow_html=True)
    n1, n2, n3, n4 = st.columns(4)
    with n1: st.markdown(f"<div class='nutri-item'><b>{cal}</b><span>CALORIES</span></div>", unsafe_allow_html=True)
    with n2: st.markdown(f"<div class='nutri-item'><b>{fat}g</b><span>FATS</span></div>", unsafe_allow_html=True)
    with n3: st.markdown(f"<div class='nutri-item'><b>{carb}g</b><span>CARBS</span></div>", unsafe_allow_html=True)
    with n4: st.markdown(f"<div class='nutri-item'><b>{protein}g</b><span>PROTEIN</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)
    if model and st.button("✨ Predict High or Low?", use_container_width=True):
        dfp = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
        pred = model.predict(dfp)[0]
        st.error(f"🔴 HIGH Calorie - {cal} kcal") if pred==1 else st.success(f"🟢 LOW Calorie - {cal} kcal")
    st.markdown("</div>", unsafe_allow_html=True)

# DEPLOY NAME - LAST MEIN
st.markdown("""
<div style="background:#111; color:white; padding:34px 20px; border-radius:20px; margin-top:32px; text-align:center;">
    <div style="font-size:10px; letter-spacing:4px; color:#4CAF50; font-weight:800;">CRAFTED • DESIGNED • DEPLOYED BY</div>
    <div style="font-family:'Playfair Display', serif; font-size:38px; font-weight:900; margin-top:10px;">Noor Ul Hassan Awan</div>
    <div style="width:60px; height:3px; background:#4CAF50; margin:14px auto;"></div>
    <div style="font-size:13px; color:#BBB;">Lahore, Pakistan 🇵🇰 • Starbucks x NutriSip • 2026</div>
    <div style="font-size:11px; color:#777; margin-top:8px;">Semester Project • Decision Tree • 94.2% Accuracy</div>
</div>
""", unsafe_allow_html=True)
