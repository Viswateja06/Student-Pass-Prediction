
import streamlit as st
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Pass Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #172554, #1e293b);
    color: white;
}

.main .block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

.header {
    text-align: center;
    padding: 25px;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

.header h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 8px;
}

.header p {
    color: #e0e7ff;
    font-size: 16px;
}

.input-card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 15px;
}

div[data-testid="stNumberInput"] label {
    color: #e2e8f0 !important;
    font-weight: 600;
}

div[data-testid="stNumberInput"] input {
    background-color: #334155;
    color: white;
    border-radius: 8px;
}

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    transform: scale(1.02);
    color: white;
}

.result-pass {
    background: linear-gradient(90deg, #065f46, #059669);
    padding: 25px;
    text-align: center;
    border-radius: 15px;
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 25px;
}

.result-fail {
    background: linear-gradient(90deg, #991b1b, #dc2626);
    padding: 25px;
    text-align: center;
    border-radius: 15px;
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 25px;
}

.footer {
    text-align: center;
    color: #94a3b8;
    padding: 25px;
    font-size: 13px;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)


# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    with open("student_model.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🎓 Student AI")
    st.markdown("---")

    st.subheader("📊 About Project")
    st.write(
        "This Machine Learning application predicts "
        "whether a student is likely to PASS or FAIL "
        "based on academic performance."
    )

    st.markdown("---")
    st.subheader("📌 Prediction Inputs")

    st.write("📚 Study Hours")
    st.write("📅 Attendance")
    st.write("📝 Previous Exam Score")
    st.write("📖 Assignments Completed")

    st.markdown("---")
    st.caption("Powered by Machine Learning")


# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>🎓 Student Pass Prediction</h1>
    <p>AI-Powered Academic Performance Analysis System</p>
</div>
""", unsafe_allow_html=True)


# ---------------- INPUT SECTION ----------------
st.subheader("📋 Enter Student Details")
st.write("Provide the student's academic information below.")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    study_hours = st.number_input(
        "📚 Study Hours Per Day",
        min_value=0.0,
        max_value=24.0,
        value=2.0,
        step=0.5
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    previous_score = st.number_input(
        "📝 Previous Exam Score",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    attendance = st.number_input(
        "📅 Attendance Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=1.0
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    assignments = st.number_input(
        "📖 Assignments Completed",
        min_value=0,
        max_value=100,
        value=5,
        step=1
    )
    st.markdown('</div>', unsafe_allow_html=True)


# ---------------- PREDICTION ----------------
st.markdown("---")

if st.button("🚀 Predict Student Result"):

    input_data = [[
        study_hours,
        attendance,
        previous_score,
        assignments
    ]]

    try:
        prediction = model.predict(input_data)

        st.subheader("📊 Prediction Result")

        if prediction[0] == 1:
            st.markdown("""
            <div class="result-pass">
                🎉 STUDENT WILL PASS!
                <p style="font-size:16px;font-weight:normal;">
                    The model predicts a PASS result.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.balloons()

        else:
            st.markdown("""
            <div class="result-fail">
                ⚠️ STUDENT MAY FAIL
                <p style="font-size:16px;font-weight:normal;">
                    The model predicts a FAIL result.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.caption(
            "Note: This is a machine learning prediction, "
            "not a guaranteed academic result."
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Student Pass Prediction System | Built with Python, 
    Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
