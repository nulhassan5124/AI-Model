import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Starbucks x NutriSip", page_icon="☕", layout="wide")

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
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=Poppins:wght@400;600;700;800&display=swap');
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 1100px; padding-top: 0.5rem; }
    * { font-family: 'Poppins', sans-serif !important; }
    h1, h2 { font-family: 'Playfair Display', serif !important; }
    .logo-center { display:flex; justify-content:center; }
    .logo-center img { width: 240px !important; height: 240px !important; border-radius: 50% !important; border: 8px solid #D4E9D2 !important; box-shadow: 0 0 0 8px #F0FFF4, 0 15px 35px rgba(0,112,66,0.25) !important; }
    .detail-box { background: linear-gradient(135deg, #F0FFF4 0%, #FFFFFF 100%); border: 2px solid #007042; border-radius: 18px; padding: 24px; text-align:center; margin-top: 18px; }
    .side-box { background: #F9F9F9; border: 1.5px solid #EEE; border-radius: 16px; padding: 18px; height: 100%; }
    .side-box:hover { border-color: #007042; box-shadow: 0 8px 20px rgba(0,112,66,0.1); }
    .stButton > button { background: #007042 !important; color: white !important; border-radius: 10px !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try: return joblib.load('starbucks_decision_tree_model.joblib')
    except: return None
model = load_model()

# ================= 1. TOP LOGO - 3RD NUMBER WALA =================
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    # Tumhara teesra wala gold wala logo - yehi sabse pyara tha
    if os.path.exists("logo.png"):
        st.markdown('<div class="logo-center">', unsafe_allow_html=True)
        st.image("logo.png")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="width:240px; height:240px; background: radial-gradient(circle at 30% 30%, #1B4332, #081C15); border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; margin:0 auto; border: 8px solid #D4E9D2; box-shadow: 0 0 0 8px #F0FFF4, 0 15px 35px rgba(0,112,66,0.25);">
            <div style="font-size:55px;">☕</div>
            <div style="width:60px; height:2px; background:#D4A574; margin:10px 0;"></div>
            <div style="color:#D4A574; font-size:13px; letter-spacing:4px; font-weight:800;">CAFÉ LUMIÈRE</div>
            <div style="color:#95D5B2; font-size:9px; letter-spacing:3px; margin-top:6px;">PREMIUM COFFEE</div>
        </div>
        """, unsafe_allow_html=True)

# ================= 2. LOGO DETAIL - NAME + KAB BANI =================
st.markdown("""
<div class="detail-box">
    <h1 style="font-size:42px; margin:0; color:#081C15;">STARBUCKS x NutriSip</h1>
    <div style="font-size:12px; letter-spacing:4px; color:#007042; font-weight:800; margin-top:8px;">EST. 1971 • SEATTLE, USA • PREMIUM COFFEE ROASTERS</div>
    <div style="width:80px; height:3px; background:#D4A574; margin:14px auto; border-radius:10px;"></div>
    <p style="font-size:14px; color:#444; line-height:1.8; max-width:750px; margin:0 auto;">
        <b>Starbucks Corporation</b> 1971 mein Seattle, Washington mein bani thi. Aaj ye duniya ki sab se bari coffeehouse chain hai, 35,000+ stores ke saath 80 countries mein.
        <b>NutriSip</b> iska AI version hai jo batata hai ke aap jo drink pee rahe ho wo <b>High Calorie hai ya Low Calorie.</b> 94.2% Accuracy ke saath.
    </p>
    <div style="display:flex; justify-content:center; gap:18px; margin-top:16px; flex-wrap:wrap;">
        <span style="background:white; border:1px solid #C7E8D5; padding:7px 14px; border-radius:20px; font-size:11px; font-weight:700;">☕ FOUNDED: March 30, 1971</span>
        <span style="background:white; border:1px solid #C7E8D5; padding:7px 14px; border-radius:20px; font-size:11px; font-weight:700;">🌍 80+ COUNTRIES</span>
        <span style="background:white; border:1px solid #C7E8D5; padding:7px 14px; border-radius:20px; font-size:11px; font-weight:700;">★ AI POWERED 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= 3. TWO SIDE - MENU | PRODUCTS =================
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
left_col, right_col = st.columns(2, gap="large")

# ---- LEFT SIDE - MENU (FATS, CAL, CARBS) ----
with left_col:
    st.markdown('<div class="side-box">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:22px; color:#007042;'>📋 STARBUCKS MENU</h2>")
    st.markdown("<p style='font-size:12px; color:#888;'>Click any drink to open its nutrition folder</p>")
    
    menu_items = [
        ("Black Coffee", 5, 0.1, 0.0, 0.3),
        ("Caffe Latte", 190, 7.0, 15.0, 12.0),
        ("Cold Coffee", 120, 4.0, 18.0, 6.0),
        ("Iced Latte", 130, 5.0, 12.0, 8.0),
        ("Matcha Latte", 200, 7.0, 26.0, 8.0),
    ]
    
    for name, cal, f, c, p in menu_items:
        with st.expander(f"{name} - {cal} kcal"):
            st.write(f"**Calories:** {cal} kcal")
            st.write(f"**Fat:** {f} g | **Carbs:** {c} g | **Protein:** {p} g")
            st.write(f"**Formula:** {f}*9 + {c}*4 + {p}*4 = {int(f*9 + c*4 + p*4)} kcal")
            if st.button(f"Select {name} →", key=f"menu_{name}", use_container_width=True):
                set_drink(name, f, c, p)
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ---- RIGHT SIDE - PRODUCTS (CATEGORIES) ----
with right_col:
    st.markdown('<div class="side-box">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:22px; color:#081C15;'>☕ PRODUCTS / CATEGORIES</h2>")
    st.markdown("<p style='font-size:12px; color:#888;'>Click category to open folder</p>")

    with st.expander("🔥 HOT COFFEE - 5 Products"):
        st.write("Black Coffee (5 kcal), Latte (190), Cappuccino (140), Macchiato (250), White Mocha (400)")
        st.caption("Fat: 0.1g - 18g | Carbs: 0g - 55g")

    with st.expander("❄️ COLD COFFEE - 5 Products"):
        st.write("Iced Americano (10), Cold Coffee (120), Iced Latte (130), Cold Brew (15), Caramel Latte (220)")
        st.caption("Best for summer, low to medium calories")

    with st.expander("🥤 FRAPPUCCINO - 4 Products"):
        st.write("Mocha (370), Caramel (380), Vanilla (350), Java Chip (420)")
        st.caption("High Calorie - Fat 14g-19g")

    with st.expander("🍵 TEA & MATCHA"):
        st.write("Green Tea (0 kcal), Matcha Latte (200), Chai Latte (240)")
        st.caption("Lowest fat options")

    with st.expander("🧃 JUICE & REFRESHERS"):
        st.write("Strawberry Acai (90), Mango (100), Pink Drink (140)")
        st.caption("Fat < 1g, refreshing")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ================= 4. SELECTED DRINK AI =================
st.divider()
st.markdown(f"<h3>Selected: <span style='color:#007042;'>{st.session_state.selected_drink}</span> - Full Nutrition</h3>", unsafe_allow_html=True)
col1, col2 = st.columns([1,1.2])
with col1:
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carb (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    est = int(fat*9 + carb*4 + protein*4)
    st.metric("Total Calories", f"{est} kcal", f"Fat {fat}g, Carbs {carb}g, Protein {protein}g")
with col2:
    if model and st.button("Predict Now →", use_container_width=True):
        df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
        pred = model.predict(df)[0]
        if pred == 1: st.error(f"HIGH Calorie - {est} kcal")
        else: st.success(f"LOW Calorie - {est} kcal")

# ================= 5. LAST MEIN TUMHARA NAAM =================
st.markdown("""
<div style="background: #081C15; color:white; padding:32px 20px; border-radius:20px; margin-top:30px; text-align:center;">
    <div style="font-size:10px; letter-spacing:4px; color:#95D5B2;">DEVELOPED BY</div>
    <div style="font-size:34px; font-weight:900; margin-top:8px; font-family:'Playfair Display', serif;">Noor Ul Hassan Awan</div>
    <div style="width:60px; height:3px; background:#D4A574; margin:12px auto;"></div>
    <div style="font-size:13px; color:#D8F3DC;">Lahore, Pakistan • 2026 • Starbucks x NutriSip</div>
</div>
""", unsafe_allow_html=True)
