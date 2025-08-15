import streamlit as st
import pandas as pd
import joblib

# =====================
# Load Model & Encoders
# =====================
model = joblib.load("best_model.pkl")
le_animal = joblib.load("le_animal.pkl")
le_labels = joblib.load("le_labels.pkl")

# Symptom list in correct training order (without 'symptom_' prefix)
all_symptoms = [
    'depression', 'painless lumps', 'loss of appetite', 'swelling in limb',
    'crackling sound', 'blisters on gums', 'difficulty walking',
    'blisters on tongue', 'lameness', 'blisters on mouth', 'chills',
    'swelling in extremities', 'shortness of breath', 'sores on mouth',
    'sores on tongue', 'sores on gums', 'fatigue', 'sweats',
    'chest discomfort', 'sores on hooves', 'swelling in abdomen',
    'swelling in muscle', 'blisters on hooves', 'swelling in neck'
]

# =====================
# Streamlit UI
# =====================
st.title("🐾 Animal Disease Detection")

# Animal input
animal_input = st.selectbox("Select Animal", le_animal.classes_)

# Age and Temperature input
age_input = st.number_input("Age", min_value=0, max_value=50, value=1)
temp_input = st.number_input("Temperature (°F)", min_value=90.0, max_value=110.0, value=101.0, step=0.1)

# Symptom selection
selected_symptoms = st.multiselect("Select up to 3 Symptoms", all_symptoms)

# Restrict to 3 symptoms
if len(selected_symptoms) > 3:
    st.error("You can select a maximum of 3 symptoms.")
    st.stop()

# =====================
# Prediction
# =====================
if st.button("Predict Disease"):
    # Encode animal
    animal_encoded = le_animal.transform([animal_input])[0]

    # Binary symptom vector
    symptom_vector = [1 if s in selected_symptoms else 0 for s in all_symptoms]

    # Create dataframe in the exact same order as training
    input_df = pd.DataFrame(
        [[animal_encoded, age_input, temp_input] + symptom_vector],
        columns=["Animal", "Age", "Temperature"] + [f"symptom_{s}" for s in all_symptoms]
    )

    # Predict
    pred_encoded = model.predict(input_df)[0]
    pred_disease = le_labels.inverse_transform([pred_encoded])[0]

    st.success(f"Predicted Disease: **{pred_disease}**")
