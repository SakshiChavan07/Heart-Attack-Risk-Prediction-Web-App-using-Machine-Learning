# app.py

# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load your trained model
model = pickle.load(open('saved_models/final_model.pkl', 'rb'))

# Streamlit UI
st.set_page_config(page_title="Heart Attack Prediction", page_icon="🫀")
st.title("🫀 Heart Health Risk Predictor")

# Ask user for input
age = st.number_input('Enter your Age:', min_value=1, max_value=120, step=1)
heart_rate = st.slider('Enter your Heart Rate (bpm):', 30, 200, 70)
blood_sugar = st.slider('Enter your Blood Sugar Level (mg/dL):', 50, 300, 100)
cholesterol = st.slider('Enter your Cholesterol Level (mg/dL):', 100, 400, 180)

# When user clicks predict
if st.button('🔍 Predict'):
    user_input = np.array([[age, heart_rate, blood_sugar, cholesterol]])
    prediction = model.predict(user_input)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Attack!")
    else:
        st.success("✅ Low Risk of Heart Attack!")
