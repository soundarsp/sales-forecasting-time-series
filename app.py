import streamlit as st
import pandas as pd
import joblib
import datetime

# Load model
model = joblib.load('app/model.pkl')

st.title("🛒 Sales Forecasting App")

st.sidebar.header("Input Features")

# Example input fields
date = st.sidebar.date_input("Date", datetime.date.today())
store_type = st.sidebar.selectbox("Store Type", ["Type 1", "Type 2", "Type 3"])
location_type = st.sidebar.selectbox("Location Type", ["Urban", "Suburban", "Rural"])
region_code = st.sidebar.selectbox("Region Code", [1, 2, 3, 4])
holiday = st.sidebar.selectbox("Holiday", [0, 1])
discount = st.sidebar.selectbox("Discount", ["Yes", "No"])
num_orders = st.sidebar.slider("Number of Orders", 0, 1000, 100)

# Feature processing (dummy example)
input_df = pd.DataFrame({
    'Store_Type': [store_type],
    'Location_Type': [location_type],
    'Region_Code': [region_code],
    'Holiday': [holiday],
    'Discount': [1 if discount == "Yes" else 0],
    'Num_Orders': [num_orders],
    'Day': [date.day],
    'Month': [date.month],
    'Year': [date.year]
})

# Prediction
if st.button("Predict Sales"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Sales: ₹ {prediction:,.2f}")
