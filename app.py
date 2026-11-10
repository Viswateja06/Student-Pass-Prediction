import streamlit as st
st.title("Student Pass Prediction")
study_hours = st.number_input("Study Hours Per Day")
attendance = st.number_input("Attendance Percentage")
previous_score = st.number_input("Previous Exam Score")
assignments = st.number_input("Assignments Completed")

import pickle
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

if st.button("Predict"):
    input_data = [[
        study_hours,
        attendance,
        previous_score,
        assignments
    ]]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")
