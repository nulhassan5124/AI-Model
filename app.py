import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="NutriSip x Starbucks | Noor Ul Hassan Awan", page_icon="☕", layout="wide")

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
    .block-container { max-width: 1100px; padding-top: 1rem; }
    .card { background: #F9F9F9; border: 1px solid #EEE; border-radius: 16px; padding: 24px; }
    .cat-head { font-size: 13px; font-weight: 800; letter-spacing: 1.5px; color: #007042; margin: 24px 0 8px 0; padding-bottom: 6px; border-bottom: 2px solid #007042; }
    .drink-box { background: white; border: 1px solid #EEE; border-radius: 12px; padding: 14px 10px; text-align: center; }
    .stButton > button { background: #007042 !important; color: white !important; border-radius: 10px !important; border: none !important; font-weight: 600 !important; height: 42px !important; }
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

# TOP WITH STARBUCKS LOGO
col1, col2 = st.columns([3, 1])
with col1:
    if os.path.exists("logo.png"):
        c1, c2 = st.columns([0.15, 0.85])
        with c1:
            st.image("logo.png", width=75)
        with c2:
            st.markdown("""
            <div style="margin-top:10px;">
                <div style="font-size:22px; font-weight:900; line-height:1;">STARBUCKS <span style="font-weight:400;">x NutriSip</span></div>
                <div style="font-size:11px; color:#007042; letter-spacing:2px; font-weight:700;">CALORIE INTELLIGENCE PROJECT</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="display:flex; align-items:center; gap:10px;">
            <div style="width:55px; height:55px; background:#007042; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:900; font-size:22px;">S</div>
            <div><div style="font-size:22px; font-weight:900;">STARBUCKS x NutriSip</div><div style="font-size:11px; color:#007042; letter-spacing:2px;">CALORIE INTELLIGENCE</div></div>
        </div>
        """, unsafe_allow_html=True)
with col2:
    st.markdown("""<div style="background:#007042; color:white; padding:8px 14px; border-radius:20px; font-size:11px; font-weight:700; text-align:center; margin-top:12px;">DEPLOYED BY NOOR UL HASSAN AWAN</div>""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<div style="padding: 10px 0 6px 0;">
    <div style="font-size:11px; letter-spacing:2px; font-weight:700; color:#007042;">STARBUCKS GLOBAL MENU • AI PROJECT • 2026</div>
    <h1 style="font-size:52px; font-weight:900; line-height:1; margin:12px 0;">Know What<br>You Drink.</h1>
    <p style="color:#666; font-size:15px; max-width:600px;">Powered by Starbucks Global Menu Dataset. Select a drink and our Decision Tree AI will tell you if it's High or Low Calorie.</p>
</div>
""", unsafe_allow_html=True)

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
    st.markdown("### AI Result — Starbucks Model")
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
            else:
                st.success(f"Low Calorie — {est} kcal")
                st.write(f"Confidence: {prob[0]*100:.1f}% • Your {st.session_state.selected_drink} is safe.")
            comp = pd.DataFrame({"Drink": [st.session_state.selected_drink, "Black Coffee", "Cold Coffee", "Frappuccino"], "Calories": [est, 5, 120, 370]})
            st.bar_chart(comp.set_index("Drink"))
        else:
            st.write("Menu se drink choose karo aur Predict dabao.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background:#007042; color:white; padding:22px; border-radius:16px; margin-top:24px; display:flex; justify-content:space-between; align-items:center;">
    <div><b>STARBUCKS x NutriSip</b><br><span style="font-size:12px; color:#C7E8D5;">AI Calorie Intelligence • 2026</span></div>
    <div style="text-align:center;"><div style="font-size:10px; color:#C7E8D5;">DEPLOYED BY</div><b>NOOR UL HASSAN AWAN</b><br><span style="font-size:12px; color:#C7E8D5;">Lahore, Pakistan</span></div>
    <div style="font-size:11px; color:#C7E8D5; text-align:right;">Decision Tree • 94.2% Accuracy</div>
</div>
""", unsafe_allow_html=True)
