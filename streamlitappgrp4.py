import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
import pandas as pd

st.title("Group 4: Bio Data Science Project")
st.write("This is a simple machine learning app created by Group 4.")

# User inputs
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Your Age", 0, 120, 25, 1)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
years_of_experience = st.slider("Select Years of Experience", 0.0, 15.0, 3.0, step=0.1)

# Load data
data = pd.read_csv(r"C:\Users\griff\Downloads\salaryData.csv")

# Preprocessing
data['Job'] = data['Job Title'].astype('category').cat.codes
data['Education'] = data['Education Level'].astype('category').cat.codes
data['Gender'] = data['Gender'].map({"Male": 0, "Female": 1})

X = data[['Age', 'Years of Experience', 'Job', 'Education', 'Gender']]
y = data['Salary']

# Remove rows where y is null
non_nan_mask = ~y.isnull()
X = X[non_nan_mask]
y = y[non_nan_mask]

# Create and fit pipeline with imputer and linear regression
model = make_pipeline(SimpleImputer(strategy='mean'), LinearRegression())
model.fit(X, y)

# Dropdowns for job and education
job_list = data['Job Title'].astype('category').cat.categories.tolist()
edu_list = data['Education Level'].astype('category').cat.categories.tolist()

job = st.selectbox("Job", job_list)
education = st.selectbox("Education", edu_list)

# Prediction
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if st.button("Predict Salary"):
        inp1 = int(age)
        inp2 = float(years_of_experience)
        inp3 = job_list.index(job)
        inp4 = edu_list.index(education)
        inp5 = 0 if gender == "Male" else 1

        salary = model.predict([[inp1, inp2, inp3, inp4, inp5]])
        st.success(f"Estimated salary: ${int(salary[0]):,}")
