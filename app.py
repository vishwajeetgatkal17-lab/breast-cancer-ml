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
# PREMIUM CSS + LIVE WALLPAPER
# =========================================================

st.markdown("""
<style>

/* =====================================================
   MAIN BACKGROUND
   ===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(0, 170, 255, 0.13),
            transparent 30%
        ),
        radial-gradient(
            circle at 80% 20%,
            rgba(130, 60, 255, 0.13),
            transparent 32%
        ),
        #050914;
}


/* =====================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
   ===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =====================================================
   CONTENT
   ===================================================== */

.block-container {
    position: relative;
    z-index: 10;

    max-width: 1200px;

    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* =====================================================
   LIVE WALLPAPER
   ===================================================== */

.live-wallpaper {
    position: fixed;

    top: 0;
    left: 0;

    width: 100vw;
    height: 100vh;

    overflow: hidden;

    pointer-events: none;

    z-index: 0;
}


/* =====================================================
   GLOWING ORBS
   ===================================================== */

.orb {
    position: absolute;

    border-radius: 50%;

    filter: blur(85px);

    opacity: 0.32;
}


.orb-blue {

    width: 380px;
    height: 380px;

    background: #00b7ff;

    left: -120px;
    top: 10%;

    animation: blueMove 14s ease-in-out infinite alternate;
}


.orb-purple {

    width: 430px;
    height: 430px;

    background: #7c3aed;

    right: -150px;
    top: 5%;

    animation: purpleMove 17s ease-in-out infinite alternate;
}


.orb-cyan {

    width: 320px;
    height: 320px;

    background: #00d9b6;

    left: 40%;
    bottom: -150px;

    animation: cyanMove 13s ease-in-out infinite alternate;
}


@keyframes blueMove {

    0% {
        transform: translate(0, 0) scale(1);
    }

    50% {
        transform: translate(280px, 120px) scale(1.25);
    }

    100% {
        transform: translate(100px, 400px) scale(0.85);
    }
}


@keyframes purpleMove {

    0% {
        transform: translate(0, 0) scale(1);
    }

    50% {
        transform: translate(-250px, 150px) scale(1.3);
    }

    100% {
        transform: translate(-100px, 400px) scale(0.9);
    }
}


@keyframes cyanMove {

    0% {
        transform: translate(0, 0) scale(1);
    }

    50% {
        transform: translate(-250px, -180px) scale(1.3);
    }

    100% {
        transform: translate(250px, -100px) scale(0.8);
    }
}


/* =====================================================
   PARTICLES
   ===================================================== */

.particle {

    position: absolute;

    width: 4px;
    height: 4px;

    border-radius: 50%;

    background: rgba(120, 220, 255, 0.65);

    box-shadow:
        0 0 10px rgba(120, 220, 255, 0.8);

    animation: particleFloat 10s linear infinite;
}


.p1 {
    left: 10%;
    top: 80%;
    animation-delay: 0s;
}

.p2 {
    left: 20%;
    top: 60%;
    animation-delay: 2s;
}

.p3 {
    left: 30%;
    top: 90%;
    animation-delay: 4s;
}

.p4 {
    left: 40%;
    top: 70%;
    animation-delay: 1s;
}

.p5 {
    left: 50%;
    top: 85%;
    animation-delay: 3s;
}

.p6 {
    left: 60%;
    top: 65%;
    animation-delay: 5s;
}

.p7 {
    left: 70%;
    top: 80%;
    animation-delay: 2s;
}

.p8 {
    left: 80%;
    top: 55%;
    animation-delay: 6s;
}

.p9 {
    left: 90%;
    top: 75%;
    animation-delay: 4s;
}

.p10 {
    left: 15%;
    top: 30%;
    animation-delay: 5s;
}

.p11 {
    left: 35%;
    top: 25%;
    animation-delay: 2s;
}

.p12 {
    left: 55%;
    top: 35%;
    animation-delay: 7s;
}

.p13 {
    left: 75%;
    top: 25%;
    animation-delay: 3s;
}

.p14 {
    left: 85%;
    top: 40%;
    animation-delay: 6s;
}


@keyframes particleFloat {

    0% {
        transform: translateY(80px);
        opacity: 0;
    }

    20% {
        opacity: 1;
    }

    80% {
        opacity: 1;
    }

    100% {
        transform: translateY(-350px);
        opacity: 0;
    }
}


/* =====================================================
   HERO
   ===================================================== */

.hero {

    padding: 42px;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.12),
            rgba(255,255,255,0.035)
        );

    border: 1px solid rgba(255,255,255,0.16);

    backdrop-filter: blur(22px);

    box-shadow:
        0 25px 80px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.10);

    margin-bottom: 25px;
}


.hero-badge {

    display: inline-block;

    padding: 8px 16px;

    border-radius: 30px;

    background: rgba(0,200,255,0.10);

    border: 1px solid rgba(0,220,255,0.30);

    color: #67e8f9 !important;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 0.5px;

    margin-bottom: 15px;
}


.hero h1 {

    color: #ffffff !important;

    font-size: 43px;

    font-weight: 850;

    margin: 0;
}


.hero p {

    color: #cbd5e1 !important;

    font-size: 17px;

    margin-top: 12px;
}


/* =====================================================
   SECTION HEADERS
   ===================================================== */

.section {

    margin-top: 32px;

    margin-bottom: 20px;

    padding: 17px 22px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.11);

    backdrop-filter: blur(18px);

    color: #ffffff !important;

    font-size: 21px;

    font-weight: 750;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.22);
}


/* =====================================================
   INPUT LABELS
   ===================================================== */

label {

    color: #e2e8f0 !important;

    font-weight: 600 !important;
}


/* =====================================================
   INPUT BOX
   ===================================================== */

div[data-baseweb="input"] {

    background: rgba(255,255,255,0.065) !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    border-radius: 12px !important;
}


div[data-baseweb="input"]:focus-within {

    border: 1px solid rgba(56,189,248,0.70) !important;

    box-shadow:
        0 0 20px rgba(56,189,248,0.18);
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
        0 12px 40px rgba(37,99,235,0.32);

    transition: all 0.25s ease;
}


div.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 18px 50px rgba(37,99,235,0.50),
        0 0 30px rgba(103,232,249,0.20);
}


/* =====================================================
   RESULT
   ===================================================== */

.result {

    margin-top: 30px;

    padding: 38px;

    border-radius: 25px;

    text-align: center;

    background:
        linear-gradient(
            135deg,
            rgba(16,185,129,0.17),
            rgba(255,255,255,0.045)
        );

    border: 1px solid rgba(52,211,153,0.38);

    backdrop-filter: blur(22px);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35),
        0 0 40px rgba(52,211,153,0.08);
}


.result h2 {

    color: #cbd5e1 !important;

    font-size: 20px;

    margin-bottom: 8px;
}


.result h1 {

    color: #6ee7b7 !important;

    font-size: 43px;

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

    margin-top: 55px;

    padding: 25px;

    border-radius: 20px;

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
# LIVE BACKGROUND
# =========================================================

st.html("""
<div class="live-wallpaper">

    <div class="orb orb-blue"></div>
    <div class="orb orb-purple"></div>
    <div class="orb orb-cyan"></div>

    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
    <div class="particle p6"></div>
    <div class="particle p7"></div>
    <div class="particle p8"></div>
    <div class="particle p9"></div>
    <div class="particle p10"></div>
    <div class="particle p11"></div>
    <div class="particle p12"></div>
    <div class="particle p13"></div>
    <div class="particle p14"></div>

</div>
""")


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
# INFO
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

st.markdown("---")


col1, col2, col3 = st.columns([1, 2, 1])


with col2:

    predict_clicked = st.button(
        "🔍 Predict Breast Cancer Status"
    )


# =========================================================
# RESULT
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
