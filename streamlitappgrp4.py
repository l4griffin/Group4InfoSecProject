
#imports streamlit library
import streamlit as st
#sets the title for the web application
st.title("Group 4: Bio Data Science Project"
# sets the subtiitle for the web application        
st.write("This is a simple machine learning app created by Group 4.")
# gives the user an interface to input their first name
first_name = st.text_input("First Name")
#gives the user an interface to input their last name
last_name = st.text_input("Last Name")
#gives the user an interface to input their gender
gender = st.selectbox("Gender", ["Male","Female"])
#gives the user an interface to input their age
age = st.number_input(" Your Age", 0, 120, 25, 1)
#gives the user an interface to input their date of birth
dob = st.date_input("Your Birthday")
#gives the user an interface to input their marital status
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
#gives the user an interface to input their years of experience
years_of_experience = st.number_input("Years of Experience", 0, 40)


