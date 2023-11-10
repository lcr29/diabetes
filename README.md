# Diabetes Prediction App
# Overview
This Diabetes Prediction application is designed to predict the likelihood of a person having diabetes based on various health parameters. It's built using Streamlit and integrates a machine learning model for predictions.

# Features
Predict diabetes likelihood based on personal health data.
Easy-to-use interface with input fields for gender, age, BMI, HbA1c level, and blood glucose level.
Options to specify hypertension and heart disease presence.
Smoking history input for a more comprehensive health profile.
Instant predictions with a simple click.

# How to Use
Input Personal Health Data: Fill in the fields with your gender, age, BMI, HbA1c level, blood glucose level, and other health-related information.
Select Health Conditions: Indicate if you have hypertension or heart disease.
Choose Smoking History: Select your smoking history from the provided options.
Get Prediction: Click the "Predict Diabetes" button to receive an instant prediction based on the input data.

# Technical Details
The app loads a pre-trained diabetes_model.pkl for predictions and a scaler.pkl for data scaling.
It handles both categorical and numerical inputs, encoding them appropriately for the model.
The prediction output is binary, indicating either the likelihood of diabetes or its absence.

# Disclaimer
This app is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.
