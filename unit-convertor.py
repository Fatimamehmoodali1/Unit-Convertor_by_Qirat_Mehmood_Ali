import streamlit as st
import numpy as np

# Custom CSS for Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
        color: #333;
        font-family: Arial, sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #2c3e50;
    }
    .stButton>button {
        background: linear-gradient(45deg, #1f4037, #99f2c8);
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
        color: white;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(45deg, #ff512f, #dd2476);
        color: white;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<h1> 🌟 Stylish Unit Converter 🌟 </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature with a beautiful UI!")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701}
    return value * length_units[to_unit] / length_units[from_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {"Kilogram": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * weight_units[to_unit] / weight_units[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

# Conversion Button
if st.button("🚀 Convert Now"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'> {value} {from_unit} = {result:.4f} {to_unit} </div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>✨ Created with ❤️ by Qirat Mehmood Ali ✨</div>", unsafe_allow_html=True)
