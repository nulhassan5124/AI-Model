import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="NutriSip | Noor Ul Hassan Awan", page_icon="☕", layout="wide")

# SAFE STATE
for k, v in [("fat", 4.0), ("carb", 18.0), ("protein", 6.0), ("selected_drink", "Cold Coffee")]:
    if k not in st.session_state:
        st.session_state[k] = v

def set_drink(name, f, c, p):
    st.session_state.fat = f
    st.session_state.carb = c
    st.session_state.protein = p
    st.session_state.selected_drink = name

# CLEAN PROFESSIONAL CSS
st.markdown("""
<style>
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 1150px; padding-top: 1rem; }
    .top { display:flex; justify-content:space-between; align-items:center; padding-bottom: 16px; border-bottom: 1px solid #EEE; }
    .card { background: #F9F9F9; border: 1px solid #EEE; border-radius: 16px; padding: 22px; }
    .cat { font-size: 12px; font-weight: 800; letter-spacing: 1px; margin: 22px 0 10px 0; }
    .drink { background: white; border: 1px solid #EEE; border-radius: 14px; overflow: hidden; text-align: center; }
    .drink img { width: 100%; height: 120px; object-fit: cover; }
    .drink b { font-size: 13px; }
    .stButton > button { background: #000 !important; color: white !important; border-radius: 10px !important; border: none !important; font-weight: 600 !important; height: 46px !important; }
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

# TOP BAR
st.markdown("""
<div class="top">
    <div style="display:flex; align-items:center; gap:10px;">
        <div style="width:42px; height:42px; background:#000; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:20px;">N</div>
        <div><div style="font-size:19px; font-weight:900;">NutriSip</div><div style="font-size:11px; color:#888;">CALORIE INTELLIGENCE</div></div>
    </div>
    <div style="background:#000; color:white; padding:7px 14px; border-radius:20px; font-size:11px; font-weight:700;">DEPLOYED BY NOOR UL HASSAN AWAN</div>
</div>
""", unsafe_allow_html=True)

# HERO - SIMPLE
st.markdown("""
<div style="padding: 28px 0 10px 0;">
    <div style="font-size:11px; letter-spacing:2px; font-weight:700; color:#888;">INTERNATIONAL PROJECT • 2026</div>
    <h1 style="font-size:48px; font-weight:900; line-height:1; margin:10px 0;">Know What<br>You Drink.</h1>
    <p style="color:#666; font-size:15px; max-width:600px;">Choose a drink from the menu below. Our AI will tell you if it is High Calorie or Low Calorie.</p>
</div>
""", unsafe_allow_html=True)

# MENU WITH IMAGES
IMG_BLACK = "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400"
IMG_LATTE = "https://images.unsplash.com/photo-1511920170033-f8396924c348?w=400"
IMG_CAPPU = "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400"
IMG_CARAMEL = "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400"
IMG_COLD = "https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=400"
IMG_FRAPP = "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=400"
IMG_TEA = "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400"
IMG_JUICE = "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=400"

menu = {
    "HOT COFFEE": [
        ("Black Coffee", "5 kcal", IMG_BLACK, 0.1, 0.0, 0.3),
        ("Caffe Latte", "190 kcal", IMG_LATTE, 7.0, 15.0, 12.0),
        ("Cappuccino", "140 kcal", IMG_CAPPU, 5.0, 12.0, 8.0),
        ("Caramel Macchiato", "250 kcal", IMG_CARAMEL, 10.0, 35.0, 7.0),
        ("White Mocha", "400 kcal", IMG_LATTE, 18.0, 55.0, 10.0),
    ],
    "COLD COFFEE": [
        ("Iced Americano", "10 kcal", IMG_COLD, 0.1, 1.0, 0.5),
        ("Cold Coffee", "120 kcal", IMG_COLD, 4.0, 18.0, 6.0),
        ("Iced Latte", "130 kcal", IMG_COLD, 5.0, 12.0, 8.0),
        ("Cold Brew", "15 kcal", IMG_BLACK, 0.2, 2.0, 0.5),
        ("Iced Caramel Latte", "220 kcal", IMG_CARAMEL, 8.0, 32.0, 7.0),
    ],
    "FRAPPUCCINO": [
        ("Mocha Frappuccino", "370 kcal", IMG_FRAPP, 15.0, 54.0, 5.0),
        ("Caramel Frappuccino", "380 kcal", IMG_FRAPP, 16.0, 56.0, 5.0),
        ("Vanilla Bean Frapp", "350 kcal", IMG_FRAPP, 14.0, 52.0, 5.0),
        ("Java Chip Frapp", "420 kcal", IMG_FRAPP, 19.0, 58.0, 6.0),
    ],
    "TEA & MATCHA": [
        ("Green Tea", "0 kcal", IMG_TEA, 0.0, 0.0, 0.0),
        ("Matcha Latte", "200 kcal", IMG_TEA, 7.0, 26.0, 8.0),
        ("Chai Tea Latte", "240 kcal", IMG_TEA, 8.0, 34.0, 7.0),
        ("Iced Green Tea", "5 kcal", IMG_TEA, 0.0, 1.0, 0.0),
    ],
    "JUICE & REFRESHERS": [
        ("Strawberry Acai", "90 kcal", IMG_JUICE, 0.1, 22.0, 0.0),
        ("Mango Dragonfruit", "100 kcal", IMG_JUICE, 0.2, 24.0, 0.2),
        ("Pink Drink", "140 kcal", IMG_JUICE, 3.0, 25.0, 1.0),
        ("Orange Juice", "110 kcal", IMG_JUICE, 0.5, 26.0, 1.0),
    ],
}

for cat, drinks in menu.items():
    st.markdown(f"<div class='cat'>{cat}</div>", unsafe_allow_html=True)
    cols = st.columns(len(drinks))
    for i, (name, kcal, img, f, c, p) in enumerate(drinks):
        with cols[i]:
            is_sel = st.session_state.selected_drink == name
            border = "2px solid #000" if is_sel else "1px solid #EEE"
            badge = "✓ Selected" if is_sel else "Select"
            st.markdown(f"""
            <div class="drink" style="border:{border};">
                <img src="{img}">
                <div style="padding:10px;"><b>{name}</b><br><span style="font-size:12px; font-weight:700;">{kcal}</span></div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(badge, key=f"{cat}_{i}", use_container_width=True):
                set_drink(name, f, c, p); st.rerun()

st.write("")
left, right = st.columns([1, 1.2], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### Your Drink: {st.session_state.selected_drink}")
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
    st.markdown("### AI Result")
    if not model_ok:
        st.error("Model file missing.")
    else:
        if st.button("Predict →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            if pred == 1:
                st.error(f"⚠️ High Calorie — {est} kcal")
                st.write(f"Confidence: {prob[1]*100:.1f}% • Your {st.session_state.selected_drink} is over 150 kcal.")
                st.info("Tip: Non-fat milk + Sugar-free syrup use karo.")
            else:
                st.success(f"✅ Low Calorie — {est} kcal")
                st.write(f"Confidence: {prob[0]*100:.1f}% • Your {st.session_state.selected_drink} is safe for daily use.")
                st.info("Tip: Great choice, keep this routine.")
            comp = pd.DataFrame({"Drink": [st.session_state.selected_drink, "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
        else:
            st.write("Menu se drink choose karo aur Predict dabao.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background:#000; color:white; padding:22px; border-radius:16px; margin-top:24px; display:flex; justify-content:space-between; align-items:center;">
    <div><b>NutriSip</b><br><span style="font-size:12px; color:#AAA;">Semester Project 2026</span></div>
    <div style="text-align:center;"><div style="font-size:10px; color:#AAA;">DEPLOYED BY</div><b>NOOR UL HASSAN AWAN</b><br><span style="font-size:12px; color:#AAA;">Lahore, Pakistan</span></div>
    <div style="font-size:11px; color:#AAA; text-align:right;">Decision Tree • 94.2% Accuracy</div>
</div>
""", unsafe_allow_html=True)
