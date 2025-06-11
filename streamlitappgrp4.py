#hello world

import streamlit as st

st.title("Group 4: Bio Data Science Project")
st.write("This is a simple machine learning app created by Group 4.")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male","Female"])
age = st.number_input(" Your Age", 0, 120, 25, 1)
dob = st.date_input("Your Birthday")
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
years_of_experience = st.number_input("Years of Experience", 0, 40)


