import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set page configuration
st.set_page_config(page_title="Starbucks Calorie Predictor", page_icon="☕", layout="centered")

st.title("☕ Starbucks Drink Calorie Predictor")
st.write("Predict whether your favorite Starbucks drink is **High Calorie (>150 kcal)** or **Low/Med Calorie (<=150 kcal)** based on its nutritional values.")

# Load the saved model
@st.cache_resource
def load_model():
    return joblib.load('starbucks_decision_tree_model.joblib')

try:
    model = load_model()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading the model. Please ensure 'starbucks_decision_tree_model.joblib' is in the same directory. Details: {e}")

# Create Input form for user
st.subheader("Enter Nutrition Details:")

fat = st.slider("Fat (g)", min_value=0.0, max_value=30.0, value=2.0, step=0.5)
carb = st.slider("Carbohydrates (g)", min_value=0.0, max_value=100.0, value=25.0, step=1.0)
protein = st.slider("Protein (g)", min_value=0.0, max_value=30.0, value=4.0, step=0.5)

# Prediction logic
if st.button("Predict Calorie Category", type="primary"):
    # Prepare the input data matching the feature order: ['Fat (g)', 'Carb. (g)', 'Protein']
    input_data = pd.DataFrame([[fat, carb, protein]], columns=['Fat (g)', 'Carb. (g)', 'Protein'])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    st.markdown("--- ")
    if prediction == 1:
        st.error(f"🚨 **Prediction: High Calorie (>150 Calories)**")
        st.write(f"Confidence: {probabilities[1]*100:.1f}%")
    else:
        st.success(f"✅ **Prediction: Low/Med Calorie (<=150 Calories)**")
        st.write(f"Confidence: {probabilities[0]*100:.1f}%")