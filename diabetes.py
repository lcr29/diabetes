import streamlit as st
import joblib
import numpy as np

# Load the model and the scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit webpage title
st.image('header_image.png', width=150) 
st.title("Diabetes Prediction")

# Creating input fields for user data
gender = st.selectbox("Select Gender", options=["Male", "Female"])
age = st.number_input("Enter Age", format='%f')
hypertension = st.checkbox("Hypertension")
heart_disease = st.checkbox("Heart Disease")
bmi = st.number_input("Enter BMI", format='%f')
hba1c_level = st.number_input("Enter HbA1c Level", format='%f')
blood_glucose_level = st.number_input("Enter Blood Glucose Level", format='%f')

# Smoking history options
smoking_options = ["No Info", "Current", "Ever", "Former", "Never", "Not Current"]
smoking_history = st.selectbox("Smoking History", options=smoking_options)

# Converting categorical inputs to the format used in the model
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension else 0
heart_disease = 1 if heart_disease else 0
smoking_encoded = [0] * len(smoking_options)
smoking_encoded[smoking_options.index(smoking_history)] = 1

# Prediction button
if st.button("Predict Diabetes"):
    # Prepare the data (only scale the features that were originally scaled)
    unscaled_data = [gender, hypertension, heart_disease] + smoking_encoded
    scaled_data = [age, bmi, hba1c_level, blood_glucose_level]
    scaled_data = scaler.transform([scaled_data])[0]
    
    # Combine scaled and unscaled data
    input_data = np.array([unscaled_data + scaled_data.tolist()])

    # Make a prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 1:
        st.write("The model predicts Diabetes.")
    else:
        st.write("The model predicts No Diabetes.")