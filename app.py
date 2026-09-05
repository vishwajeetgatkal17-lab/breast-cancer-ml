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
# PREMIUM DESIGN
# =========================================================

st.markdown("""
<style>

/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 10% 20%,
            rgba(0, 180, 255, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(150, 70, 255, 0.18),
            transparent 32%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(0, 255, 190, 0.10),
            transparent 30%
        ),
        #050914;
}


/* =====================================================
   ANIMATED BACKGROUND GLOW
   ===================================================== */

.stApp::before {
    content: "";
    position: fixed;

    width: 420px;
    height: 420px;

    left: -120px;
    top: 15%;

    border-radius: 50%;

    background: rgba(0, 190, 255, 0.10);

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

    background: rgba(145, 70, 255, 0.12);

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


/* =====================================================
   MAIN CONTENT
   ===================================================== */

.block-container {
    position: relative;

    z-index: 2;

    padding-top: 2rem;
    padding-bottom: 3rem;

    max-width: 1250px;
}


/* =====================================================
   HERO CARD
   ===================================================== */

.hero {
    padding: 42px;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.13),
            rgba(255,255,255,0.035)
        );

    border: 1px solid rgba(255,255,255,0.15);

    backdrop-filter: blur(20px);

    box-shadow:
        0 25px 80px rgba(0,0,0,0.40),
        inset 0 1px 0 rgba(255,255,255,0.10);

    margin-bottom: 25px;
}


.hero-badge {
    display: inline-block;

    padding: 8px 15px;

    margin-bottom: 16px;

    border-radius: 30px;

    background: rgba(0,200,255,0.10);

    border: 1px solid rgba(0,200,255,0.30);

    color: #67e8f9 !important;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 0.5px;
}


.hero h1 {
    color: #ffffff !important;

    font-size: 42px;

    font-weight: 800;

    margin: 0;
}


.hero p {
    color: #cbd5e1 !important;

    font-size: 17px;

    margin-top: 12px;
}


/* =====================================================
   SECTION CARDS
   ===================================================== */

.section {
    margin-top: 32px;

    margin-bottom: 18px;

    padding: 16px 22px;

    border-radius: 17px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(15px);

    color: #ffffff !important;

    font-size: 21px;

    font-weight: 750;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.20);
}


/* =====================================================
   LABELS
   ===================================================== */

label {
    color: #e2e8f0 !important;

    font-weight: 600 !important;
}


/* =====================================================
   NUMBER INPUT
   ===================================================== */

div[data-baseweb="input"] {

    background: rgba(255,255,255,0.065) !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    border-radius: 12px !important;
}


div[data-baseweb="input"]:focus-within {

    border: 1px solid rgba(56,189,248,0.75) !important;

    box-shadow:
        0 0 20px rgba(56,189,248,0.16);
}


div[data-baseweb="input"] input {

    color: #ffffff !important;
}


/* =====================================================
   SELECT BOX
   ===================================================== */

div[data-baseweb="select"] > div {

    background: rgba(255,255,255,0.065) !important;

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

    height: 60px;

    border-radius: 17px;

    border: 1px solid rgba(103,232,249,0.40);

    background:
        linear-gradient(
            135deg,
            #0891b2,
            #2563eb,
            #7c3aed
        );

    color: #ffffff !important;

    font-size: 18px;

    font-weight: 800;

    box-shadow:
        0 12px 40px rgba(37,99,235,0.30);

    transition: all 0.25s ease;
}


div.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 18px 50px rgba(37,99,235,0.45),
        0 0 25px rgba(103,232,249,0.15);
}


/* =====================================================
   RESULT CARD
   ===================================================== */

.result {

    margin-top: 28px;

    padding: 35px;

    border-radius: 24px;

    text-align: center;

    background:
        linear-gradient(
            135deg,
            rgba(16,185,129,0.16),
            rgba(255,255,255,0.045)
        );

    border: 1px solid rgba(52,211,153,0.35);

    backdrop-filter: blur(20px);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35),
        0 0 35px rgba(52,211,153,0.08);
}


.result h2 {

    color: #cbd5e1 !important;

    font-size: 19px;

    margin-bottom: 10px;
}


.result h1 {

    color: #6ee7b7 !important;

    font-size: 40px;

    font-weight: 850;

    margin: 5px 0 10px 0;
}


.result p {

    color: #94a3b8 !important;

    font-size: 14px;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {

    margin-top: 50px;

    padding: 25px;

    border-radius: 18px;

    text-align: center;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.07);

    color: #64748b;

    font-size: 13px;
}


.footer strong {

    color: #cbd5e1;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 768px) {

    .hero {

        padding: 28px 22px;

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

st.html("""
<div class="hero">

    <div class="hero-badge">
        ✨ AI-POWERED MEDICAL PREDICTION
    </div>

    <h1>
        🩺 Breast Cancer Status Prediction
    </h1>

    <p>
        An interactive Machine Learning application for
        predicting breast cancer patient status.
    </p>

</div>
""")


# =========================================================
# INFORMATION MESSAGE
# =========================================================

st.info(
    "Enter the patient information below and click "
    "**Predict Breast Cancer Status**."
)


# =========================================================
# PATIENT INFORMATION
# =========================================================

st.html("""
<div class="section">
    👤 Patient Information
</div>
""")


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
            "Single ",
            "Divorced",
            "Widowed",
            "Separated"
        ]
    )


# =========================================================
# TUMOR INFORMATION
# =========================================================

st.html("""
<div class="section">
    🔬 Tumor Information
</div>
""")


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
        [
            "T1",
            "T2",
            "T3",
            "T4"
        ]
    )


with col3:

    n_stage = st.selectbox(
        "N Stage",
        [
            "N1",
            "N2",
            "N3"
        ]
    )


col1, col2, col3 = st.columns(3)


with col1:

    sixth_stage = st.selectbox(
        "6th Stage",
        [
            "IIA",
            "IIB",
            "IIIA",
            "IIIB",
            "IIIC"
        ]
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

st.html("""
<div class="section">
    🏥 Clinical Information
</div>
""")


col1, col2, col3 = st.columns(3)


with col1:

    a_stage = st.selectbox(
        "A Stage",
        [
            "Regional",
            "Distant"
        ]
    )


with col2:

    estrogen_status = st.selectbox(
        "Estrogen Status",
        [
            "Positive",
            "Negative"
        ]
    )


with col3:

    progesterone_status = st.selectbox(
        "Progesterone Status",
        [
            "Positive",
            "Negative"
        ]
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

input_data = pd.DataFrame(
    {
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
    }
)


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("---")


button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)


with button_col2:

    predict_clicked = st.button(
        "🔍 Predict Breast Cancer Status"
    )


# =========================================================
# PREDICTION RESULT
# =========================================================

if predict_clicked:

    prediction = model.predict(input_data)

    result = prediction[0]

    st.html(f"""
    <div class="result">

        <h2>
            Prediction Result
        </h2>

        <h1>
            🩺 {result}
        </h1>

        <p>
            Result generated by the trained
            Machine Learning model.
        </p>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    <strong>
        🩺 Breast Cancer AI Prediction
    </strong>

    <br><br>

    Built with Python • Scikit-learn • Streamlit

    <br><br>

    ⚠️ This application is for educational and
    demonstration purposes only.

    <br>

    It is not a substitute for professional
    medical diagnosis.

</div>
""")
