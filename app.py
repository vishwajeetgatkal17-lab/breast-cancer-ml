import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("breast_cancer_model.pkl")

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺"
)

st.title("🩺 Breast Cancer Status Prediction")

st.write("Enter patient information below.")

# Numerical inputs
age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=50
)

tumor_size = st.number_input(
    "Tumor Size",
    min_value=0,
    value=20
)

regional_node_examined = st.number_input(
    "Regional Node Examined",
    min_value=0,
    value=10
)

regional_node_positive = st.number_input(
    "Regional Node Positive",
    min_value=0,
    value=2
)

survival_months = st.number_input(
    "Survival Months",
    min_value=0,
    value=50
)

# Categorical inputs
race = st.selectbox(
    "Race",
    ["White", "Black", "Other"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Married", "Single", "Divorced", "Widowed", "Separated"]
)

t_stage = st.selectbox(
    "T Stage",
    ["T1", "T2", "T3", "T4"]
)

n_stage = st.selectbox(
    "N Stage",
    ["N1", "N2", "N3"]
)

sixth_stage = st.selectbox(
    "6th Stage",
    ["IIA", "IIB", "IIIA", "IIIB", "IIIC"]
)

differentiate = st.selectbox(
    "Differentiate",
    ["Poorly differentiated", "Moderately differentiated",
     "Well differentiated", "Undifferentiated"]
)

grade = st.selectbox(
    "Grade",
    ["1", "2", "3", "4"]
)

a_stage = st.selectbox(
    "A Stage",
    ["Regional", "Distant"]
)

estrogen_status = st.selectbox(
    "Estrogen Status",
    ["Positive", "Negative"]
)

progesterone_status = st.selectbox(
    "Progesterone Status",
    ["Positive", "Negative"]
)

# Create input dataframe
input_data = pd.DataFrame({
    "Age": [age],
    "Race": [race],
    "Marital Status": [marital_status],
    "T Stage": [t_stage],
    "N Stage": [n_stage],
    "6th Stage": [sixth_stage],
    "differentiate": [differentiate],
    "Grade": [grade],
    "A Stage": [a_stage],
    "Tumor Size": [tumor_size],
    "Estrogen Status": [estrogen_status],
    "Progesterone Status": [progesterone_status],
    "Regional Node Examined": [regional_node_examined],
    "Reginol Node Positive": [regional_node_positive],
    "Survival Months": [survival_months]
})

# Prediction
if st.button("🔍 Predict"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Status: {prediction[0]}")
