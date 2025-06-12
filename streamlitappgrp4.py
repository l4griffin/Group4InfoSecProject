
#imports libraries
import streamlit as st
from sklearn.linear_model import LinearRegression
import pandas as pd

#sets the title for the web application
st.title("Group 4: Bio Data Science Project")

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

#gives the user an interface to input their marital status
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])

#gives the user an interface to input their years of experience
st.subheader("Make a Prediction")
years_of_experience = st.slider("Select Years of Experience", 0.0, 15.0, 3.0, step=0.1)

data = pd.read_csv("C:\Users\griff\Downloads\salaryData.csv")

# Create a Linear Regression model 
X = data[['YearsExperience']]
y = data['Salary']
model = LinearRegression()
model.fit(X, y)

# Create a list of jobs
job_list = data['Job'].unique().tolist()

# Create a list of education levels
edu_list = data['Education'].unique().tolist()

# Add user input for job and education
job = st.selectbox("Job", job_list)
education = st.selectbox("Education", edu_list)




col10, col11, col12, col13, col14 = st.columns(5)

with col10:
    st.write('')
with col11:
    st.write('')
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    pass

if(predict_btn):
    inp1 = int(age)
    inp2 = float(years_of_experience)
    inp3 = int(job_list.index(job))
    inp4 = int(edu_list.index(education))
    # Add gender list and index
    gen_list = ["Male", "Female"]
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
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')

