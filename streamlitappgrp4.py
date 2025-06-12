
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

col10, col11, col12, col13, col14 = st.columns(5)

with col10:
    st.write('')
with col11:
    st.write('')
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')

if(predict_btn):
    inp1 = int(age)
    inp2 = float(experience)
    inp3 = int(job_idx[job_list.index(job)])
    inp4 = int(edu_list.index(education))
    inp5 = int(gen_list.index(gender))
    X = [[inp1, inp2, inp3, inp4, inp5]]
    salary = model.predict(X)
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')

