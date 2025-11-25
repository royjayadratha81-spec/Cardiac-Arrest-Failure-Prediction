import streamlit as st
import joblib as jb
import numpy as np 
# Load the trained model and scaler
model = jb.load('heart_disease_model.pkl')
scaler = jb.load('scaler.pkl')
st.title("Heart Disease Prediction")
st.image("https://www.pdcenterlv.com/wp-content/uploads/2019/07/heart-intro-photo-1.jpg")
caption = "Human Heart Anatomy"
st.caption(caption) 
width = st.slider("Select the width of the image", 100, 800, 400)
st.write("Please enter the following details to predict the presence of heart disease:")
age = st.slider("Age", 1,120,60)
anaemia = st.selectbox("Anaemia", [0,1])
creatinine = st.number_input("Creatinine Phosphokinase", 0, 8000)
diabetes = st.radio("Diabetes", [0,1], format_func=lambda X: "Yes" if X else "No")
ef = st.number_input("Ejection Fraction", 0, 100)
hbp = st.radio("High Blood Pressure", [0,1], format_func=lambda X: "Yes" if X else "No")
platelets = st.number_input("Platelets", 0.0, 1000000.0)
serum_creatinine = st.number_input("Serum Creatinine", 0.0, 10.0)
serum_sodium = st.number_input("Serum Sodium", 0, 200)
sex = st.selectbox("Sex (1=Male, 0=Female)", [0,1])
smoking = st.selectbox("Smoking", [0,1])
time = st.number_input("Follow-up time (in days)", 0, 300)

if st.button("Heart Failure"):
    heart_input = [[age, anaemia, creatinine, diabetes, ef, hbp, platelets, 
                    serum_creatinine, serum_sodium, sex, smoking, time]]
    scaled = scaler.transform(heart_input)
    result = model.predict(scaled)
    if result[0] == 1:
        st.success("High Risk of Heart Failure")
    else:
        st.suceess("Low Risk of Heart Failure")
