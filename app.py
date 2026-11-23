import streamlit as st
import pandas as pd
import joblib
import os

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
    st.session_state.menu_open = False

def select(name, f, c, p):
    st.session_state.selected = name
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p

# --- STYLISH DESIGN - CLEAN ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700;1,900&family=Poppins:wght@300;400;500;600;700;800&display=swap');
.stApp { background: #FFFEFA; }
.block-container { max-width: 1000px; padding-top: 0.8rem; padding-bottom: 2rem; }
* { font-family: 'Poppins', sans-serif !important; }
h1,h2,h3 { font-family: 'Playfair Display', serif !important; letter-spacing: -0.5px; }

/* LOGO - PERFECT CIRCLE */
.logo-box { display:flex; justify-content:center; margin-top:10px; }
.logo-box img { width: 230px !important; height: 230px !important; object-fit: cover !important; border-radius: 50% !important; border: 7px solid #E8DCC6 !important; box-shadow: 0 0 0 7px #FFF8E7, 0 20px 40px rgba(0,0,0,0.18) !important; }

/* TITLE - STYLISH */
.hero-title { text-align:center; font-family:'Playfair Display', serif; font-size:54px; font-weight:900; line-height:1.0; color:#1A1A1A; margin:18px 0 0 0; }
.hero-title span { color:#007042; font-style:italic; }
.hero-sub { text-align:center; color:#777; font-size:14px; letter-spacing:0.5px; margin-top:10px; }
.gold-line { width:70px; height:3px; background:#C9A227; margin:16px auto; border-radius:10px; }

/* INFO CARDS */
.info-card { background:#FFFFFF; border:1px solid #F0EAD8; border-radius:18px; padding:22px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); }
.nutri-box { background:#1E3A2F; color:white; border-radius:18px; padding:22px; }
.nutri-item { background: rgba(255,255,255,0.08); border-radius:12px; padding:14px; text-align:center; }
.nutri-item b { font-size:22px; display:block; }
.nutri-item span { font-size:11px; color:#A8D5BC; letter-spacing:1px; }

/* BUTTONS */
.stButton > button { background:#007042 !important; color:white !important; border:none !important; border-radius:12px !important; padding:10px 18px !important; font-weight:700 !important; letter-spacing:0.3px !important; }
.stButton > button:hover { background:#005A36 !important; transform: translateY(-1px); }
.menu-btn button { background:#1A1A1A !important; font-size:16px !important; padding:14px !important; border-radius:14px !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try: return joblib.load('starbucks_decision_tree_model.joblib')
    except: return None
model = load_model()

# ============ 1. LOGO - TOP ============
st.markdown('<div class="logo-box">', unsafe_allow_html=True)
if os.path.exists("logo.png"):
    st.image("logo.png")
else:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1200px-Starbucks_Corporation_Logo_2011.svg.png")
st.markdown('</div>', unsafe_allow_html=True)

# ============ 2. NAME + DETAIL - STYLISH WRITING ============
st.markdown("""
<div style="text-align:center;">
    <div style="display:inline-block; background:#FFF8E7; border:1px solid #E8DCC6; color:#8A6D00; padding:6px 16px; border-radius:30px; font-size:10px; font-weight:800; letter-spacing:3px; margin-top:18px;">★ EST. 1971 • SEATTLE • PREMIUM COFFEE ★</div>
    <h1 class="hero-title">Starbucks <span>x NutriSip</span></h1>
    <div class="gold-line"></div>
    <p class="hero-sub">Know What You Drink — Har sip se pehle, uski poori kahani jaano.</p>
    <p style="color:#555; font-size:14px; line-height:1.8; max-width:720px; margin:14px auto 0 auto;">
        <b>Starbucks</b> 30 March 1971 ko Seattle, USA mein bani. Aaj 80+ countries, 35,000+ stores ke saath duniya ki No.1 coffee brand hai.<br>
        <b>NutriSip</b> iska AI partner hai — jo batata hai ke aapki coffee <b>High Calorie hai ya Low Calorie.</b> 94.2% Accuracy ke saath.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)

# ============ 3. MENU BUTTON - CLICK KARO TO SARA MENU KHUL JAYE ============
st.markdown("<div class='menu-btn'>", unsafe_allow_html=True)
if st.button("☰  VIEW FULL MENU  •  Click Here To Open", use_container_width=True):
    st.session_state.menu_open = not st.session_state.menu_open
st.markdown("</div>", unsafe_allow_html=True)

# FULL MENU DATA - FATS, CAL, CARBS, PROTEIN
menu = [
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
]

if st.session_state.menu_open:
    st.markdown("<div class='info-card' style='margin-top:14px;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0 0 12px 0;'>📋 Full Starbucks Menu — Sab Kuch Detail Ke Saath</h3>")
    df = pd.DataFrame(menu, columns=["Drink", "Category", "Calories", "Fat (g)", "Carbs (g)", "Protein (g)"])
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("<p style='font-size:12px; color:#888; margin-top:8px;'>Neeche kisi bhi drink pe click karo, uski full detail neeche khul jayegi.</p>")
    cols = st.columns(3)
    for i, (name, cat, cal, f, c, p) in enumerate(menu):
        with cols[i % 3]:
            if st.button(f"{name} • {cal} kcal", key=f"menu_{i}", use_container_width=True):
                select(name, f, c, p)
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align:center; color:#999; font-size:12px; margin-top:8px;'>↑ Upar wale button pe click karo, poora menu yahan khul jayega ↑</p>", unsafe_allow_html=True)

# ============ 4. SELECTED DRINK - FATS, CARBS SAB KUCH NEECHE ============
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown(f"<h2 style='font-size:28px;'>Selected Drink: <span style='color:#007042; font-style:italic;'>{st.session_state.selected}</span></h2>", unsafe_allow_html=True)

c1, c2 = st.columns([1, 1.1], gap="large")
with c1:
    st.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin:0 0 14px 0;'>Adjust Your Drink</h3>")
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carbohydrates (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    cal = int(fat*9 + carb*4 + protein*4)
    st.markdown(f"<div style='background:#FFF8E7; padding:12px; border-radius:12px; text-align:center; margin-top:10px;'><b style='font-size:24px;'>{cal} kcal</b><br><span style='font-size:11px; color:#888;'>ESTIMATED CALORIES</span></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='nutri-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:white; margin:0 0 14px 0;'>Full Nutrition Breakdown</h3>")
    n1, n2, n3, n4 = st.columns(4)
    with n1: st.markdown(f"<div class='nutri-item'><b>{cal}</b><span>CALORIES</span></div>", unsafe_allow_html=True)
    with n2: st.markdown(f"<div class='nutri-item'><b>{fat}g</b><span>FATS</span></div>", unsafe_allow_html=True)
    with n3: st.markdown(f"<div class='nutri-item'><b>{carb}g</b><span>CARBS</span></div>", unsafe_allow_html=True)
    with n4: st.markdown(f"<div class='nutri-item'><b>{protein}g</b><span>PROTEIN</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
    if model:
        if st.button("✨ Predict - High or Low Calorie?", use_container_width=True):
            dfp = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(dfp)[0]
            if pred == 1: st.error(f"🔴 HIGH Calorie — {cal} kcal")
            else: st.success(f"🟢 LOW Calorie — {cal} kcal")
    else:
        st.info(f"Demo Result: {'HIGH Calorie' if cal > 200 else 'LOW Calorie'} — {cal} kcal")
    st.markdown("</div>", unsafe_allow_html=True)

# ============ 5. LAST MEIN TUMHARA NAAM - DEPLOY NAME ============
st.markdown("""
<div style="background:#111111; color:white; padding:34px 20px; border-radius:20px; margin-top:32px; text-align:center;">
    <div style="font-size:10px; letter-spacing:4px; color:#C9A227; font-weight:800;">CRAFTED • DESIGNED • DEPLOYED BY</div>
    <div style="font-family:'Playfair Display', serif; font-size:38px; font-weight:900; margin-top:10px;">Noor Ul Hassan Awan</div>
    <div style="width:60px; height:3px; background:#C9A227; margin:14px auto; border-radius:10px;"></div>
    <div style="font-size:13px; color:#BBB;">Lahore, Pakistan 🇵🇰 • Starbucks x NutriSip • 2026</div>
    <div style="font-size:11px; color:#777; margin-top:8px;">Semester Project • Decision Tree • 94.2% Accuracy • Streamlit</div>
</div>
""", unsafe_allow_html=True)
