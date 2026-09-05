import streamlit as st
import pandas as pd
import joblib

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Breast Caimport streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Breast Cancer AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("breast_cancer_model.pkl")

# =========================================================
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   GLOBAL
   ===================================================== */

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(0, 170, 255, 0.15), transparent 28%),
        radial-gradient(circle at 90% 15%, rgba(150, 80, 255, 0.16), transparent 30%),
        radial-gradient(circle at 50% 90%, rgba(0, 255, 190, 0.10), transparent 30%),
        #050914;
    color: #f8fafc;
}

/* Animated glow wallpaper */

.stApp::before {
    content: "";
    position: fixed;
    width: 420px;
    height: 420px;
    left: -120px;
    top: 15%;
    border-radius: 50%;
    background: rgba(0, 183, 255, 0.10);
    filter: blur(90px);
    animation: floatOne 9s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 500px;
    height: 500px;
    right: -150px;
    bottom: 5%;
    border-radius: 50%;
    background: rgba(143, 77, 255, 0.11);
    filter: blur(100px);
    animation: floatTwo 11s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}

@keyframes floatOne {
    from {
        transform: translate(0px, 0px) scale(1);
    }
    to {
        transform: translate(180px, 80px) scale(1.25);
    }
}

@keyframes floatTwo {
    from {
        transform: translate(0px, 0px) scale(1);
    }
    to {
        transform: translate(-160px, -100px) scale(1.3);
    }
}

/* Main content */

.block-container {
    position: relative;
    z-index: 2;
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* =====================================================
   HERO
   ===================================================== */

.hero {
    padding: 38px 42px;
    border-radius: 26px;
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.12),
        rgba(255,255,255,0.04)
    );
    border: 1px solid rgba(255,255,255,0.14);
    backdrop-filter: blur(18px);
    box-shadow:
        0 20px 70px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.10);
    margin-bottom: 25px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 42px;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
}

.hero p {
    color: #cbd5e1 !important;
    font-size: 17px;
    margin-top: 10px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    margin-bottom: 14px;
    border-radius: 30px;
    background: rgba(0, 200, 255, 0.10);
    border: 1px solid rgba(0, 200, 255, 0.25);
    color: #67e8f9;
    font-size: 13px;
    font-weight: 700;
}

/* =====================================================
   INFO BOX
   ===================================================== */

div[data-testid="stAlert"] {
    background: rgba(15, 35, 65, 0.75);
    border: 1px solid rgba(56, 189, 248, 0.20);
    border-radius: 15px;
}

/* =====================================================
   SECTION HEADINGS
   ===================================================== */

.section {
    margin-top: 32px;
    margin-bottom: 15px;
    padding: 15px 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    color: #ffffff !important;
    font-size: 21px;
    font-weight: 750;
    box-shadow: 0 8px 30px rgba(0,0,0,0.18);
}

/* =====================================================
   LABELS
   ===================================================== */

label {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

/* =====================================================
   INPUTS
   ===================================================== */

div[data-baseweb="input"] {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
}

div[data-baseweb="input"]:focus-within {
    border: 1px solid rgba(56,189,248,0.70) !important;
    box-shadow: 0 0 18px rgba(56,189,248,0.16);
}

div[data-baseweb="input"] input {
    color: #ffffff !important;
}

/* Select boxes */

div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
}

div[data-baseweb="select"] * {
    color: #ffffff !important;
}

/* =====================================================
   PREDICT BUTTON
   ===================================================== */

div.stButton {
    display: flex;
    justify-content: center;
}

div.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 16px;
    border: 1px solid rgba(103,232,249,0.35);
    background: linear-gradient(
        135deg,
        #0891b2,
        #2563eb,
        #7c3aed
    );
    color: #ffffff !important;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 0.3px;
    box-shadow:
        0 10px 35px rgba(37,99,235,0.30),
        inset 0 1px 0 rgba(255,255,255,0.20);
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow:
        0 15px 45px rgba(37,99,235,0.45),
        0 0 25px rgba(103,232,249,0.15);
    border-color: rgba(255,255,255,0.45);
}

/* =====================================================
   RESULT CARD
   ===================================================== */

.result {
    margin-top: 28px;
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    background: linear-gradient(
        135deg,
        rgba(16,185,129,0.13),
        rgba(255,255,255,0.05)
    );
    border: 1px solid rgba(52,211,153,0.30);
    backdrop-filter: blur(18px);
    box-shadow:
        0 15px 50px rgba(0,0,0,0.30),
        0 0 30px rgba(52,211,153,0.08);
}

.result h2 {
    color: #cbd5e1 !important;
    font-size: 18px;
}

.result h1 {
    color: #6ee7b7 !important;
    font-size: 38px;
    font-weight: 850;
    margin: 8px 0;
}

.result p {
    color: #94a3b8 !important;
}

/* =====================================================
   DIVIDER
   ===================================================== */

hr {
    border-color: rgba(255,255,255,0.10) !important;
    margin-top: 35px;
    margin-bottom: 35px;
}

/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    margin-top: 45px;
    padding: 22px;
    color: #64748b;
    font-size: 13px;
}

.footer strong {
    color: #94a3b8;
}

/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 768px) {

    .hero {
        padding: 28px 24px;
    }

    .hero h1 {
        font-size: 30px;
    }

    .hero p {
        font-size: 15px;
    }

    .section {
        font-size: 19px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        ✨ AI-POWERED MEDICAL PREDICTION
    </div>

    <h1>🩺 Breast Cancer Status Prediction</h1>

    <p>
        An interactive Machine Learning application for predicting
        breast cancer patient status.
    </p>

</div>
""", unsafe_allow_html=True)


st.info(
    "Enter the patient information below and click **Predict Breast Cancer Status**."
)


# =========================================================
# PATIENT INFORMATION
# =========================================================

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


# =========================================================
# TUMOR INFORMATION
# =========================================================

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


# =========================================================
# CLINICAL INFORMATION
# =========================================================

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


# =========================================================
# INPUT DATAFRAME
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

    "Regional Node Examined": [regional_node_examined],

    "Reginol Node Positive": [regional_node_positive],

    "Survival Months": [survival_months]
})


# =========================================================
# PREDICTION
# =========================================================

st.markdown("---")

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])

with predict_col2:

    if st.button("🔍  Predict Breast Cancer Status"):

        prediction = model.predict(input_data)

        result = prediction[0]

        st.markdown(
            f"""
            <div class="result">

                <h2>Prediction Result</h2>

                <h1>🩺 {result}</h1>

                <p>
                    Result generated by the trained Machine Learning model.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <strong>🩺 Breast Cancer AI Prediction</strong><br><br>

    Built with Python • Scikit-learn • Streamlit

    <br><br>

    <span>
        ⚠️ This application is for educational and demonstration purposes only.
        It is not a substitute for professional medical diagnosis.
    </span>

</div>
""", unsafe_allow_html=True)ncer Prediction",
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
