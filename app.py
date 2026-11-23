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
    .stApp { background: #FFFFFF; }
    .block-container { max-width: 1050px; padding-top: 0rem; }
    .card { background: #F9F9F9; border: 1px solid #EEE; border-radius: 16px; padding: 24px; }
    .cat-head { font-size: 13px; font-weight: 800; letter-spacing: 1.5px; color: #007042; margin: 22px 0 8px 0; padding-bottom: 6px; border-bottom: 2px solid #007042; }
    .drink-box { background: white; border: 1px solid #EEE; border-radius: 12px; padding: 14px 10px; text-align: center; }
    .stButton > button { background: #007042 !important; color: white !important; border-radius: 10px !important; border: none !important; font-weight: 600 !important; height: 42px !important; font-size: 12px !important; }
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
# 1. TOP - LOGO IN CIRCLE
# ============================================================
st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=160)
    else:
        st.markdown("""
        <div style="width:160px; height:160px; background:#007042; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto; border: 6px solid #E8F5EE;">
            <div style="text-align:center; color:white;">
                <div style="font-size:42px; font-weight:900; line-height:1;">S</div>
                <div style="font-size:11px; letter-spacing:2px; font-weight:700;">STARBUCKS</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; margin-top:12px;">
        <div style="font-size:24px; font-weight:900; line-height:1;">STARBUCKS <span style="font-weight:400;">x NutriSip</span></div>
        <div style="font-size:11px; color:#007042; letter-spacing:2px; font-weight:700; margin-top:4px;">CALORIE INTELLIGENCE PROJECT • 2026</div>
        <h1 style="font-size:38px; font-weight:900; line-height:1.1; margin-top:16px;">Know What<br>You Drink.</h1>
        <p style="color:#666; font-size:14px;">Starbucks Global Menu se drink choose karo, AI batayega High ya Low Calorie.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================================
# 2. PRODUCTS - ONLY HEADINGS
# ============================================================
st.markdown("### Our Products")
st.caption("Select a drink — Detail neechay aa jayegi")

menu = {
    "HOT COFFEE": [("Black Coffee", "5 kcal", 0.1, 0.0, 0.3), ("Caffe Latte", "190 kcal", 7.0, 15.0, 12.0), ("Cappuccino", "140 kcal", 5.0, 12.0, 8.0), ("Caramel Macchiato", "250 kcal", 10.0, 35.0, 7.0), ("White Mocha", "400 kcal", 18.0, 55.0, 10.0)],
    "COLD COFFEE": [("Iced Americano", "10 kcal", 0.1, 1.0, 0.5), ("Cold Coffee", "120 kcal", 4.0, 18.0, 6.0), ("Iced Latte", "130 kcal", 5.0, 12.0, 8.0), ("Cold Brew", "15 kcal", 0.2, 2.0, 0.5), ("Iced Caramel Latte", "220 kcal", 8.0, 32.0, 7.0)],
    "FRAPPUCCINO": [("Mocha Frappuccino", "370 kcal", 15.0, 54.0, 5.0), ("Caramel Frappuccino", "380 kcal", 16.0, 56.0, 5.0), ("Vanilla Bean Frapp", "350 kcal", 14.0, 52.0, 5.0), ("Java Chip Frapp", "420 kcal", 19.0, 58.0, 6.0)],
    "TEA & MATCHA": [("Green Tea", "0 kcal", 0.0, 0.0, 0.0), ("Matcha Latte", "200 kcal", 7.0, 26.0, 8.0), ("Chai Tea Latte", "240 kcal", 8.0, 34.0, 7.0), ("Iced Green Tea", "5 kcal", 0.0, 1.0, 0.0)],
    "JUICE & REFRESHERS": [("Strawberry Acai", "90 kcal", 0.1, 22.0, 0.0), ("Mango Dragonfruit", "100 kcal", 0.2, 24.0, 0.2), ("Pink Drink", "140 kcal", 3.0, 25.0, 1.0), ("Orange Juice", "110 kcal", 0.5, 26.0, 1.0)],
}

for cat, drinks in menu.items():
    st.markdown(f"<div class='cat-head'>{cat}</div>", unsafe_allow_html=True)
    cols = st.columns(len(drinks))
    for i, (name, kcal, f, c, p) in enumerate(drinks):
        with cols[i]:
            is_sel = st.session_state.selected_drink == name
            border = "2px solid #007042" if is_sel else "1px solid #EEE"
            bg = "#F0FFF4" if is_sel else "white"
            badge = "✓ Selected" if is_sel else "Select"
            st.markdown(f"""<div class="drink-box" style="border:{border}; background:{bg};"><b>{name}</b><br><span style="font-size:12px; color:#666;">{kcal}</span></div>""", unsafe_allow_html=True)
            if st.button(badge, key=f"{cat}_{i}", use_container_width=True):
                set_drink(name, f, c, p); st.rerun()

# ============================================================
# 3. PRODUCT DETAIL
# ============================================================
st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
st.markdown("### Product Detail")
st.caption(f"Selected Product: {st.session_state.selected_drink}")

left, right = st.columns([1, 1.2], gap="medium")
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"#### {st.session_state.selected_drink}")
    st.write("Nutrition values neechay se adjust kar sakte ho:")
    fat = st.slider("Fat (g)", 0.0, 30.0, key="fat")
    carb = st.slider("Carbs (g)", 0.0, 100.0, key="carb")
    protein = st.slider("Protein (g)", 0.0, 30.0, key="protein")
    est = int(fat*9 + carb*4 + protein*4)
    st.markdown(f"**Estimated Calories: {est} kcal**")
    st.progress(min(int(est/2000*100), 100))
    st.caption(f"Daily Budget 2000 kcal • {est/2000*100:.1f}% used")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### AI Result")
    if not model_ok:
        st.error("Model file missing.")
    else:
        if st.button("Predict →", use_container_width=True):
            df = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
            pred = model.predict(df)[0]
            prob = model.predict_proba(df)[0]
            if pred == 1:
                st.error(f"High Calorie — {est} kcal")
                st.write(f"Confidence: {prob[1]*100:.1f}% • Your {st.session_state.selected_drink} is over 150 kcal.")
                st.info("Tip: Non-fat milk + Sugar-free syrup use karo.")
            else:
                st.success(f"Low Calorie — {est} kcal")
                st.write(f"Confidence: {prob[0]*100:.1f}% • Your {st.session_state.selected_drink} is safe for daily use.")
                st.info("Tip: Great choice, keep this routine.")
            comp = pd.DataFrame({"Drink": [st.session_state.selected_drink, "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
        else:
            st.write("Product choose kar ke Predict dabao.")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# 4. END - TUMHARA NAAM
# ============================================================
st.markdown("""
<div style="background:#007042; color:white; padding:28px; border-radius:16px; margin-top:30px; text-align:center;">
    <div style="font-size:11px; letter-spacing:2px; color:#C7E8D5;">DEPLOYED & DEVELOPED BY</div>
    <div style="font-size:26px; font-weight:900; margin-top:6px;">NOOR UL HASSAN AWAN</div>
    <div style="font-size:13px; color:#C7E8D5; margin-top:4px;">Lahore, Pakistan 🇵🇰 • Starbucks x NutriSip • 2026</div>
    <div style="font-size:11px; color:#A8D5BC; margin-top:10px;">Decision Tree Model • 94.2% Accuracy • Semester Project</div>
</div>
""", unsafe_allow_html=True)
