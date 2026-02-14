# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("hdfc_model.pkl")

# Page Title
st.set_page_config(page_title="Stock Price Prediction", layout="centered")

st.title("📈 Stock Price Prediction App")
st.write("Enter the stock details below to get prediction.")

# User Inputs
open_price = st.number_input("Open Price", min_value=0.0)
high_price = st.number_input("High Price", min_value=0.0)
low_price = st.number_input("Low Price", min_value=0.0)
volume = st.number_input("Volume", min_value=0.0)

# Prediction Button
if st.button("Predict"):

    # Create DataFrame with same feature names used during training
    input_data = pd.DataFrame({
        "Open": [open_price],
        "High": [high_price],
        "Low": [low_price],
        "Volume": [volume]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Stock Price: {prediction[0]}")

