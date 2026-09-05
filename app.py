import streamlit as st
import pandas as pd
import joblib

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

# ==================================================
# LOAD MODEL
# ==================================================

model = joblib.load("breast_cancer_model.pkl")

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

/* ---------- HERO ---------- */

.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #f5f7ff, #eef2ff);
    border: 1px solid #e0e4ff;
    margin-bottom: 25px;
}

.hero h1 {
    margin-bottom: 5px;
    font-size: 38px;
    color: #111827 !important;
}

.hero p {
    font-size: 17px;
    margin-top: 5px;
    color: #374151 !important;
}

/* ---------- SECTION HEADINGS ---------- */

.section {
    font-size: 22px;
    font-weight: 700;
    color: #111827;
    margin-top: 25px;
    margin-bottom: 12px;
}

/* ---------- INPUT LABELS ---------- */

label {
    color: #111827 !important;
}

/* ---------- BUTTON ---------- */

div.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
}

/* ---------- RESULT CARD ---------- */

.result {
    padding: 25px;
    border-radius: 15px;
    margin-top: 25px;
    text-align: center;
    border: 1px solid #dcdcdc;
    background-color: #f8fafc;
}

.result h2 {
    margin-bottom: 5px;
    color: #111827 !important;
}

.result h1 {
    color: #111827 !important;
    font-size: 32px;
}

.result p {
    color: #374151 !important;
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    margin-top: 40px;
    padding: 15px;
    color: #6b7280;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="hero">
    <h1>🩺 Breast Cancer Status Prediction</h1>
    <p>
        Machine Learning based prediction system for breast cancer patient status.
    </p>
</div>
""", unsafe_allow_html=True)

st.info(
    "ℹ️ Enter the patient information below and click **Predict**."
)


# ==================================================
# PATIENT INFORMATION
# ==================================================

st.markdown(
    '<div class="section">👤 Patient Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=50
    )

with col2:
    race = st.selectbox(
        "Race",
        ["White", "Black", "Other"]
    )

with col3:
    marital_status = st.selectbox(
        "Marital Status",
        ["Married", "Single ", "Divorced", "Widowed", "Separated"]
    )


# ==================================================
# TUMOR INFORMATION
# ==================================================

st.markdown(
    '<div class="section">🔬 Tumor Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    tumor_size = st.number_input(
        "Tumor Size",
        min_value=0,
        value=20
    )

with col2:
    t_stage = st.selectbox(
        "T Stage",
        ["T1", "T2", "T3", "T4"]
    )

with col3:
    n_stage = st.selectbox(
        "N Stage",
        ["N1", "N2", "N3"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    sixth_stage = st.selectbox(
        "6th Stage",
        ["IIA", "IIB", "IIIA", "IIIB", "IIIC"]
    )

with col2:
    differentiate = st.selectbox(
        "Differentiation",
        [
            "Poorly differentiated",
            "Moderately differentiated",
            "Well differentiated",
            "Undifferentiated"
        ]
    )

with col3:
    grade = st.selectbox(
        "Grade",
        [
            "1",
            "2",
            "3",
            " anaplastic; Grade IV"
        ]
    )


# ==================================================
# CLINICAL INFORMATION
# ==================================================

st.markdown(
    '<div class="section">🏥 Clinical Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    a_stage = st.selectbox(
        "A Stage",
        ["Regional", "Distant"]
    )

with col2:
    estrogen_status = st.selectbox(
        "Estrogen Status",
        ["Positive", "Negative"]
    )

with col3:
    progesterone_status = st.selectbox(
        "Progesterone Status",
        ["Positive", "Negative"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    regional_node_examined = st.number_input(
        "Regional Node Examined",
        min_value=0,
        value=10
    )

with col2:
    regional_node_positive = st.number_input(
        "Regional Node Positive",
        min_value=0,
        value=2
    )

with col3:
    survival_months = st.number_input(
        "Survival Months",
        min_value=0,
        value=50
    )


# ==================================================
# CREATE INPUT DATA
# ==================================================

input_data = pd.DataFrame({
    "Age": [age],
    "Race": [race],
    "Marital Status": [marital_status],
    "T Stage ": [t_stage],
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


# ==================================================
# PREDICTION
# ==================================================

st.markdown("---")

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])

with predict_col2:

    if st.button("🔍 Predict Breast Cancer Status"):

        prediction = model.predict(input_data)

        result = prediction[0]

        st.markdown(
            f"""
            <div class="result">
                <h2>Prediction Result</h2>
                <h1>🩺 {result}</h1>
                <p>
                    Predicted patient status based on the trained
                    Machine Learning model.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div class="footer">
    <p>Built with Python • Scikit-learn • Streamlit</p>
    <p>Breast Cancer ML Prediction Project</p>
</div>
""", unsafe_allow_html=True)
