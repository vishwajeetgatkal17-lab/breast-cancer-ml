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
# PREMIUM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   MAIN APP
   ===================================================== */

.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(59,130,246,0.12), transparent 30%),
        radial-gradient(circle at 85% 30%, rgba(168,85,247,0.10), transparent 30%),
        radial-gradient(circle at 50% 90%, rgba(6,182,212,0.08), transparent 30%),
        #020617;
    color: #e2e8f0;
}

/* Remove top spacing */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* =====================================================
   LIVE WALLPAPER
   ===================================================== */

.live-wallpaper {
    position: fixed;
    inset: 0;
    z-index: -1;
    overflow: hidden;
    pointer-events: none;
}

/* Glowing orbs */

.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.25;
    animation: floatOrb 14s infinite alternate ease-in-out;
}

.orb-blue {
    width: 280px;
    height: 280px;
    background: #2563eb;
    top: 5%;
    left: 5%;
}

.orb-purple {
    width: 320px;
    height: 320px;
    background: #9333ea;
    top: 35%;
    right: 5%;
    animation-delay: 3s;
}

.orb-cyan {
    width: 260px;
    height: 260px;
    background: #06b6d4;
    bottom: 5%;
    left: 40%;
    animation-delay: 6s;
}

@keyframes floatOrb {

    0% {
        transform: translate(0px, 0px) scale(1);
    }

    50% {
        transform: translate(60px, -40px) scale(1.1);
    }

    100% {
        transform: translate(-40px, 50px) scale(0.95);
    }

}

/* =====================================================
   PARTICLES
   ===================================================== */

.particle {
    position: absolute;
    width: 4px;
    height: 4px;
    background: #67e8f9;
    border-radius: 50%;
    opacity: 0.45;
    animation: particleMove 10s infinite linear;
}

@keyframes particleMove {

    0% {
        transform: translateY(100vh);
        opacity: 0;
    }

    20% {
        opacity: 0.5;
    }

    80% {
        opacity: 0.5;
    }

    100% {
        transform: translateY(-20vh);
        opacity: 0;
    }

}

.p1 { left: 5%; animation-duration: 12s; }
.p2 { left: 12%; animation-duration: 9s; animation-delay: 2s; }
.p3 { left: 20%; animation-duration: 14s; animation-delay: 1s; }
.p4 { left: 28%; animation-duration: 11s; animation-delay: 4s; }
.p5 { left: 36%; animation-duration: 15s; animation-delay: 3s; }
.p6 { left: 44%; animation-duration: 10s; animation-delay: 5s; }
.p7 { left: 52%; animation-duration: 13s; animation-delay: 2s; }
.p8 { left: 60%; animation-duration: 16s; animation-delay: 6s; }
.p9 { left: 68%; animation-duration: 11s; animation-delay: 3s; }
.p10 { left: 75%; animation-duration: 14s; animation-delay: 1s; }
.p11 { left: 82%; animation-duration: 10s; animation-delay: 5s; }
.p12 { left: 88%; animation-duration: 13s; animation-delay: 2s; }
.p13 { left: 94%; animation-duration: 15s; animation-delay: 4s; }
.p14 { left: 48%; animation-duration: 12s; animation-delay: 7s; }

/* =====================================================
   HERO
   ===================================================== */

.hero {
    text-align: center;
    padding: 50px 25px;
    margin-bottom: 35px;

    background: rgba(15,23,42,0.62);

    border: 1px solid rgba(148,163,184,0.15);

    border-radius: 28px;

    backdrop-filter: blur(18px);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.35),
        inset 0 1px rgba(255,255,255,0.04);
}

.hero-badge {

    display: inline-block;

    padding: 8px 18px;

    border-radius: 30px;

    background: rgba(56,189,248,0.10);

    border: 1px solid rgba(56,189,248,0.25);

    color: #67e8f9;

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 1.5px;

    margin-bottom: 18px;

}

.hero h1 {

    font-size: 42px;

    font-weight: 800;

    margin-bottom: 12px;

    background: linear-gradient(
        90deg,
        #67e8f9,
        #60a5fa,
        #c084fc
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}

.hero p {

    color: #94a3b8;

    font-size: 16px;

    max-width: 700px;

    margin: auto;

    line-height: 1.7;

}

/* =====================================================
   SECTION CARDS
   ===================================================== */

.section {

    background: rgba(15,23,42,0.65);

    border: 1px solid rgba(148,163,184,0.12);

    border-radius: 22px;

    padding: 25px;

    margin-bottom: 25px;

    backdrop-filter: blur(16px);

    box-shadow:
        0 15px 45px rgba(0,0,0,0.25);

}

.section-title {

    color: #e2e8f0;

    font-size: 21px;

    font-weight: 700;

    margin-bottom: 5px;

}

.section-subtitle {

    color: #64748b;

    font-size: 13px;

    margin-bottom: 20px;

}

/* =====================================================
   INPUTS
   ===================================================== */

label {

    color: #cbd5e1 !important;

    font-weight: 600 !important;

}

.stSelectbox > div > div,
.stNumberInput > div > div > input {

    background: rgba(15,23,42,0.75) !important;

    color: #e2e8f0 !important;

    border-radius: 12px !important;

}

.stNumberInput input {

    color: #e2e8f0 !important;

}

/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {

    width: 100%;

    height: 58px;

    border-radius: 16px;

    border: none;

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed,
        #0891b2
    );

    color: white;

    font-size: 17px;

    font-weight: 800;

    letter-spacing: 0.5px;

    box-shadow:
        0 10px 30px rgba(37,99,235,0.25);

    transition: all 0.3s ease;

}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 15px 40px rgba(59,130,246,0.4);

}

/* =====================================================
   RESULT
   ===================================================== */

.result {

    text-align: center;

    margin-top: 30px;

    padding: 35px;

    border-radius: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(37,99,235,0.14),
            rgba(124,58,237,0.14)
        );

    border: 1px solid rgba(96,165,250,0.25);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.30);

}

.result h2 {

    color: #94a3b8;

    font-size: 15px;

    text-transform: uppercase;

    letter-spacing: 2px;

}

.result h1 {

    color: #67e8f9;

    font-size: 36px;

    font-weight: 800;

}

.result p {

    color: #64748b;

}

/* =====================================================
   FOOTER
   ===================================================== */

.footer {

    text-align: center;

    margin-top: 60px;

    padding: 35px 20px;

    border-top: 1px solid rgba(148,163,184,0.10);

    background: rgba(2,6,23,0.35);

    border-radius: 20px;

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

    margin-top: 8px;

    color: #94a3b8;

    font-size: 15px;

    font-weight: 600;

}

.footer-tech {

    margin-top: 14px;

    color: #64748b;

    font-size: 13px;

}

.footer-line {

    width: 70px;

    height: 2px;

    margin: 18px auto;

    background: #38bdf8;

    border-radius: 10px;

    box-shadow: 0 0 12px #38bdf8;

}

.footer-disclaimer {

    color: #64748b;

    font-size: 12px;

    line-height: 1.7;

}

</style>
""")

# =========================================================
# LIVE WALLPAPER HTML
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
        predicting breast cancer patient status using
        clinical and tumor-related information.
    </p>

</div>
""")

# =========================================================
# PATIENT INFORMATION
# =========================================================

st.html("""
<div class="section">

    <div class="section-title">
        👤 Patient Information
    </div>

    <div class="section-subtitle">
        Enter basic patient demographic information.
    </div>

</div>
""")

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

st.html("""
<div class="section">

    <div class="section-title">
        🧬 Tumor Information
    </div>

    <div class="section-subtitle">
        Enter tumor characteristics and cancer stage information.
    </div>

</div>
""")

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

st.html("""
<div class="section">

    <div class="section-title">
        🧪 Clinical Information
    </div>

    <div class="section-subtitle">
        Enter clinical and lymph node information.
    </div>

</div>
""")

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
# PREDICT BUTTON
# =========================================================

st.write("")

predict_clicked = st.button(
    "🔮  PREDICT PATIENT STATUS"
)

# =========================================================
# PREDICTION
# =========================================================

if predict_clicked:

    try:

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

    except Exception as e:

        st.error(
            f"Prediction error: {e}"
        )

# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">

    <div class="footer-name">
        ✨ Made by
        <span>Vishwajeet Gatkal</span>
    </div>

    <div class="footer-role">
        AI & DS Engineer • Machine Learning Enthusiast
    </div>

    <div class="footer-tech">
        Python&nbsp;&nbsp;•&nbsp;&nbsp;
        Machine Learning&nbsp;&nbsp;•&nbsp;&nbsp;
        Scikit-learn&nbsp;&nbsp;•&nbsp;&nbsp;
        Streamlit
    </div>

    <div class="footer-line"></div>

    <div class="footer-disclaimer">

        🩺 Educational AI/ML Project

        <br>

        ⚠️ Not intended for professional medical diagnosis.

    </div>

</div>
""")
