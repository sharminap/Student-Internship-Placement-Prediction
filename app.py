import streamlit as st
import pickle
import numpy as np

#PAGE SETTINGS 
st.set_page_config(page_title="Placement Predictor 🎓", page_icon="🎓", layout="centered")

# TITLE 
st.markdown("<h1 style='text-align: center; color: #0e76a8;'>🎓 Student Placement Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>📊 Predict placement chances based on academic and skill-based details</h4>", unsafe_allow_html=True)
st.markdown("---")

#LOAD MODEL
with open('best_placement_model.pkl', 'rb') as file:
    model_data = pickle.load(file)

model = model_data['model']
features = model_data['features']

#  FORM 
with st.form("placement_form"):
    st.subheader("📋 Enter Student Details")
    col1, col2 = st.columns(2)

    with col1:
        CGPA = st.number_input("CGPA (0.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.1)
        Internships = st.number_input("Number of Internships", min_value=0, step=1)
        Projects = st.number_input("Number of Projects", min_value=0, step=1)
        Workshops = st.number_input("Workshops/Certifications", min_value=0, step=1)
        SSC_Marks = st.number_input("SSC Marks (%)", min_value=0, max_value=100, step=1)

    with col2:
        AptitudeScore = st.number_input("Aptitude Test Score (0-100)", min_value=0, max_value=100, step=1)
        SoftSkills = st.number_input("Soft Skills Rating (0.0 - 5.0)", min_value=0.0, max_value=5.0, step=0.1)
        Extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
        Training = st.selectbox("Placement Training Attended", ["Yes", "No"])
        HSC_Marks = st.number_input("HSC Marks (%)", min_value=0, max_value=100, step=1)

    submitted = st.form_submit_button("🔍 Predict Placement")

# PREDICTION
if submitted:
    st.markdown("---")
    st.subheader("📊 Prediction Result")

    extra = 1 if Extracurricular == "Yes" else 0
    train = 1 if Training == "Yes" else 0

    input_data = np.array([
        CGPA, Internships, Projects, Workshops,
        AptitudeScore, SoftSkills, extra, train,
        SSC_Marks, HSC_Marks
    ]).reshape(1, -1)

    result = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100

    #PLACEMENT READINESS SCORE 
    score = 0

    if CGPA >= 8.0: score += 15
    elif CGPA >= 6.5: score += 10

    if AptitudeScore >= 70: score += 15
    elif AptitudeScore >= 50: score += 10

    if Internships >= 2: score += 15
    elif Internships >= 1: score += 10

    if Projects >= 3: score += 10
    elif Projects >= 1: score += 5

    if SoftSkills >= 4.0: score += 10
    elif SoftSkills >= 2.5: score += 5

    if Workshops >= 2: score += 10
    elif Workshops >= 1: score += 5

    if train: score += 10
    if extra: score += 5

    readiness_score = min(score, 100)

    st.markdown(f"### 🎯 Placement Readiness Score: **{readiness_score}/100**")
    st.markdown(f"### 📈 Model Confidence Score: **{probability:.2f}%**")

    if result == 1:
        st.success("✅ Likely to be Placed!")
        if readiness_score >= 80:
            st.success("🌟 Excellent profile!")
        elif readiness_score >= 60:
            st.info("✅ Decent profile, can improve further.")
        else:
            st.warning("⚠️ Low readiness, work on improvement areas.")
    else:
        st.error("❌ Not likely to be placed currently.")
        st.warning("🔧 Suggested Improvements:")

        if CGPA < 6.5:
            st.markdown("• 📚 Improve academic CGPA (below 6.5).")
        if AptitudeScore < 50:
            st.markdown("• 🧠 Work on Aptitude (score below 50).")
        if Internships == 0:
            st.markdown("• 💼 Gain internship experience.")
        if Projects == 0:
            st.markdown("• 📝 Work on academic/industry projects.")
        if Workshops == 0:
            st.markdown("• 📜 Attend workshops/certifications.")
        if not train:
            st.markdown("• 🎓 Attend placement training programs.")
        if SoftSkills < 2.5:
            st.markdown("• 🗣️ Improve communication and soft skills.")

    st.markdown("---")
    st.caption("🔒 This tool is for educational use only | Built by Team NASS 💡")
#about section
    
with st.expander("ℹ️ About this App"):
    st.markdown("""
    **Student Placement Predictor** is an AI-powered tool that helps students assess their campus placement chances based on academics, internships, skills, and projects.

    **Features:**
    - Predicts placement outcome and confidence score
    - Calculates Placement Readiness Score (out of 100)
    - Provides personalized suggestions to improve profile

    **Built by:** Team NAAS  
    **Note:** This tool is for educational purposes only.
    """)
