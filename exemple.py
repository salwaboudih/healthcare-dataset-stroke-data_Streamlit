import streamlit as st
import numpy as np
import pickle


with open('besthealthcare1.pkl', 'rb') as f:
    model = pickle.load(f)

st.title(" Prédiction de Risque d'AVC")

gender = st.radio("Sexe", ['Male', 'Female'])
age = st.number_input("Âge", min_value=0.0, max_value=120.0, step=1.0)
hypertension = st.radio("Hypertension", ['Oui', 'Non'])
heart_disease = st.radio("Maladie cardiaque", ['Oui', 'Non'])
ever_married = st.radio("Déjà marié(e)", ['Yes', 'No'])
work_type = st.selectbox("Type de travail", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
residence_type = st.radio("Type de résidence", ['Urban', 'Rural'])
avg_glucose_level = st.number_input("Taux moyen de glucose", min_value=0.0)
bmi = st.number_input("IMC (BMI)", min_value=0.0)
smoking_status = st.selectbox("Statut tabagique", ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])



if st.button("Prédire le risque d'AVC"):

    gender = 1 if gender == 'Male' else 0
    hypertension = 1 if hypertension == 'Oui' else 0
    heart_disease = 1 if heart_disease == 'Oui' else 0
    ever_married = 1 if ever_married == 'Yes' else 0

    if work_type == 'Private':
        work_type_encoded = 0
    elif work_type == 'Self-employed':
        work_type_encoded = 1
    elif work_type == 'Govt_job':
        work_type_encoded = 2
    elif work_type == 'children':
        work_type_encoded = 3
    else:   
        work_type_encoded = 4

    residence_type = 1 if residence_type == 'Urban' else 0

    if smoking_status == 'never smoked':
        smoking_status_encoded = 0
    elif smoking_status == 'formerly smoked':
        smoking_status_encoded = 1
    elif smoking_status == 'smokes':
        smoking_status_encoded = 2
    else:  
        smoking_status_encoded = 3

    
    input_data = np.array([[
        gender,
        age,
        hypertension,
        heart_disease,
        ever_married,
        work_type_encoded,
        residence_type,
        avg_glucose_level,
        bmi,
        smoking_status_encoded
    ]])

    # Prédiction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error(" Risque d’AVC détecté")
    else:
        st.success("Aucun risque détecté")
