import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Breast Cancer AI",
    page_icon="🩺",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("breast_cancer_model.pkl")

# =========================================================
# SIMPLE PREMIUM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #020617;
}

.block-container {
    max-width: 1150px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Hero */

.hero {
    text-align: center;
    padding: 45px 20px;
    margin-bottom: 35px;
    border-radius: 25px;
    background: linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.85)
    );
    border: 1px solid rgba(96,165,250,0.20);
}

.badge {
    display: inline-block;
    padding: 7px 16px;
    border-radius: 20px;
    background: rgba(34,211,238,0.10);
    color: #67e8f9;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin-top: 18px;
    color: #e2e8f0;
}

.hero-text {
    color: #94a3b8;
    font-size: 16px;
    max-width: 700px;
    margin: auto;
    line-height: 1.6;
}

/* Section */

.section {
    padding: 22px;
    margin-top: 25px;
    margin-bottom: 15px;
    border-radius: 20px;
    background: rgba(15,23,42,0.85);
    border: 1px solid rgba(148,163,184,0.12);
}

.section-title {
    color: #e2e8f0;
    font-size: 21px;
    font-weight: 700;
}

.section-text {
    color: #64748b;
    font-size: 13px;
    margin-top: 5px;
}

/* Button */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    font-size: 17px;
    font-weight: 700;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #1d4ed8,
        #6d28d9
    );
}

/* Result */

.result {
    text-align: center;
    padding: 30px;
    margin-top: 30px;
    border-radius: 22px;
    background: rgba(14,116,144,0.12);
    border: 1px solid rgba(34,211,238,0.25);
}

.result-title {
    color: #94a3b8;
    font-size: 14px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.result-value {
    color: #67e8f9;
    font-size: 35px;
    font-weight: 800;
}

/* Footer */

.footer {
    text-align: center;
    margin-top: 60px;
    padding: 30px;
    border-top: 1px solid rgba(148,163,184,0.12);
}

.footer-name {
    color: #e2e8f0;
    font-size: 22px;
    font-weight: 700;
}

.footer-name span {
    color: #67e8f9;
}

.footer-role {
    color: #94a3b8;
    margin-top: 8px;
    font-size: 15px;
}

.footer-tech {
    color: #64748b;
    margin-top: 12px;
    font-size: 13px;
}

.footer-line {
    width: 70px;
    height: 2px;
    background: #38bdf8;
    margin: 18px auto;
}

.footer-disclaimer {
    color: #64748b;
    font-size: 12px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="badge">
        ✨ AI-POWERED MEDICAL PREDICTION
    </div>

    <div class="hero-title">
        🩺 Breast Cancer Status Prediction
    </div>

    <div class="hero-text">
        An interactive Machine Learning application for
        predicting breast cancer patient status using
        clinical and tumor-related information.
    </div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# PATIENT INFORMATION
# =========================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        👤 Patient Information
    </div>

    <div class="section-text">
        Enter basic patient demographic information.
    </div>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=50
    )

with col2:
    race = st.selectbox(
        "Race",
        [
            "White",
            "Black",
            "Other"
        ]
    )

with col3:
    marital_status = st.selectbox(
        "Marital Status",
        [
            "Married",
            "Divorced",
            "Single ",
            "Widowed",
            "Separated"
        ]
    )

# =========================================================
# TUMOR INFORMATION
# =========================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        🧬 Tumor Information
    </div>

    <div class="section-text">
        Enter tumor characteristics and cancer stage information.
    </div>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    t_stage = st.selectbox(
        "T Stage",
        [
            "T1",
            "T2",
            "T3",
            "T4"
        ]
    )

with col2:
    n_stage = st.selectbox(
        "N Stage",
        [
            "N1",
            "N2",
            "N3"
        ]
    )

with col3:
    sixth_stage = st.selectbox(
        "6th Stage",
        [
            "IIA",
            "IIIA",
            "IIIC",
            "IIB",
            "IIIB"
        ]
    )

col1, col2, col3 = st.columns(3)

with col1:
    differentiate = st.selectbox(
        "Differentiation",
        [
            "Poorly differentiated",
            "Moderately differentiated",
            "Well differentiated",
            "Undifferentiated"
        ]
    )

with col2:
    grade = st.selectbox(
        "Grade",
        [
            "3",
            "2",
            "1",
            " anaplastic; Grade IV"
        ]
    )

with col3:
    a_stage = st.selectbox(
        "A Stage",
        [
            "Regional",
            "Distant"
        ]
    )

col1, col2 = st.columns(2)

with col1:
    tumor_size = st.number_input(
        "Tumor Size",
        min_value=1,
        max_value=200,
        value=20
    )

with col2:
    survival_months = st.number_input(
        "Survival Months",
        min_value=0,
        max_value=500,
        value=50
    )

# =========================================================
# CLINICAL INFORMATION
# =========================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        🧪 Clinical Information
    </div>

    <div class="section-text">
        Enter clinical and lymph node information.
    </div>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    estrogen_status = st.selectbox(
        "Estrogen Status",
        [
            "Positive",
            "Negative"
        ]
    )

with col2:
    progesterone_status = st.selectbox(
        "Progesterone Status",
        [
            "Positive",
            "Negative"
        ]
    )

with col3:
    regional_node_examined = st.number_input(
        "Regional Node Examined",
        min_value=0,
        max_value=100,
        value=10
    )

col1, col2 = st.columns(2)

with col1:
    regional_node_positive = st.number_input(
        "Regional Node Positive",
        min_value=0,
        max_value=100,
        value=2
    )

# =========================================================
# INPUT DATA
# =========================================================

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

    "Regional Node Examined": [
        regional_node_examined
    ],

    "Reginol Node Positive": [
        regional_node_positive
    ],

    "Survival Months": [
        survival_months
    ]

})

# =========================================================
# PREDICT
# =========================================================

st.write("")

predict_clicked = st.button(
    "🔮  PREDICT PATIENT STATUS"
)

# =========================================================
# RESULT
# =========================================================

if predict_clicked:

    try:

        prediction = model.predict(input_data)

        result = prediction[0]

        st.markdown(f"""
        <div class="result">

            <div class="result-title">
                Prediction Result
            </div>

            <div class="result-value">
                🩺 {result}
            </div>

        </div>
        """, unsafe_allow_html=True)

    except Exception as e:

        st.error(
            f"Prediction error: {e}"
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <div class="footer-name">
        ✨ Made by
        <span>Vishwajeet Gatkal</span>
    </div>

    <div class="footer-role">
        AI & DS Engineer • Machine Learning Enthusiast
    </div>

    <div class="footer-tech">
        Python • Machine Learning • Scikit-learn • Streamlit
    </div>

    <div class="footer-line"></div>

    <div class="footer-disclaimer">
        🩺 Educational AI/ML Project
        <br>
        ⚠️ Not intended for professional medical diagnosis.
    </div>

</div>
""", unsafe_allow_html=True)
