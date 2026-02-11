import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(page_title="LapWorth", layout="wide")

# ---------------- Background + Theme CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.atulhost.com/wp-content/uploads/2024/07/best-laptop-brands.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .block-container {
        padding-top: 0rem;
    }

    h1 {
        text-align: center;
        color: black;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }

    label {
        color: black !important;
        font-weight: 600;
    }

    div[data-baseweb="select"] > div,
    input {
        background-color: rgba(20,20,20,0.85) !important;
        color: white !important;
        border-radius: 10px;
    }

    span {
        color: white !important;
    }

    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(90deg,#1f4037,#99f2c8);
        color: black;
        border: none;
    }

    div.stAlert {
        background-color: rgba(0,0,0,0.75);
        color: white;
        border-radius: 12px;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- Load Model ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- Title ----------------
st.markdown("<h1>LapWorth</h1>", unsafe_allow_html=True)

# ---------------- Layout ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    company = st.selectbox("Brand", ["Apple","Dell","HP","Lenovo","Asus","Acer"])
    cpu = st.selectbox("CPU Brand", ["Intel Core i3","Intel Core i5","Intel Core i7"])
    gpu = st.selectbox("GPU Brand", ["Intel","Nvidia","AMD"])
    screen_size = st.number_input("Screen Size (inches)",10.0,18.0,15.6)

with col2:
    type_name = st.selectbox("Type", ["Ultrabook","Notebook","Gaming"])
    ips = st.selectbox("IPS Display", ["No","Yes"])
    touchscreen = st.selectbox("Touchscreen", ["No","Yes"])

with col3:
    os = st.selectbox("OS", ["Windows","Mac OS X","No OS/Android/Other"])
    weight = st.number_input("Weight (kg)",0.5,5.0,1.5)
    ram = st.selectbox("Ram (GB)", [4,8,16,32])

with col4:
    hdd = st.selectbox("HDD (GB)", [0,500,1000,2000])
    ssd = st.selectbox("SSD (GB)", [0,128,256,512,1024])
    resolution = st.selectbox("Screen Resolution", ["1920x1080","1366x768"])

# ---------------- Prediction ----------------
if st.button("Predict Price"):
    X_res,Y_res = map(int,resolution.split("x"))
    ppi = ((X_res**2 + Y_res**2)**0.5)/screen_size

    input_df = pd.DataFrame([{
        "Company":company,
        "TypeName":type_name,
        "Ram":ram,
        "Weight":weight,
        "TouchScreen":1 if touchscreen=="Yes" else 0,
        "IPS Panel":1 if ips=="Yes" else 0,
        "ppi":ppi,
        "Cpu_brand":cpu,
        "HDD":hdd,
        "SSD":ssd,
        "Gpu_Brand":gpu,
        "OS":os
    }])

    price = np.exp(model.predict(input_df)[0])
    st.success(f"💰 Predicted Price: ₹ {int(price)}")
