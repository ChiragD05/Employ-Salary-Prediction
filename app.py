import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load("salary_prediction_model.pkl")

# Streamlit page setup
st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")
st.title("💼 Salary Prediction App")
st.markdown("Predict your estimated salary based on job and personal details.")

# Sidebar inputs
st.sidebar.header("Enter Details")

# Dropdowns and input fields
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

years_exp = st.sidebar.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=3.0, step=0.5)

edu_level = st.sidebar.selectbox("Education Level", [
    'bachelors', 'doctorate', 'high school', 'masters'
])

job_role = st.sidebar.selectbox("Job Role", [
    'AI Specialist', 'Accountant', 'Administrative Assistant', 'Auditor', 'Backend Developer',
    'Budget Analyst', 'Business Analyst', 'Business Development Representative',
    'Chief Executive Officer', 'Chief Financial Officer', 'Chief Information Officer',
    'Chief Operating Officer', 'Customer Service Representative', 'Customer Success Manager',
    'Cybersecurity Analyst', 'Data Analyst', 'Data Engineer', 'Data Scientist',
    'Database Administrator', 'DevOps Engineers', 'Digital Marketing Specialist', 'Director',
    'Executive Assistant', 'Financial Analyst', 'Financial Controller', 'Frontend Developer',
    'Graphic Designer', 'HR Specialist', 'Human Resources Business Partner',
    'Human Resources Manager', 'IT Specialist', 'Infrastructure Engineer',
    'Learning and Development Specialist', 'Legal Counsel', 'Machine Learning Engineer',
    'Marketing Manager', 'Marketing Specialist', 'Mobile Application Developer',
    'Network Engineer', 'Office Manager', 'Paralegal', 'Product Manager', 'Product Owner',
    'Project Manager', 'Quality Assurance Engineer', 'Sales Manager', 'Sales Representative',
    'Scrum Master', 'Senior Accountant', 'Senior Project Manager', 'Senior Software Engineer',
    'Social Media Manager', 'Software Architect', 'Software Engineer', 'System Administrator',
    'Talent Acquisition Specialist', 'Technical Writer', 'Tester', 'UX/UI Designer', 'Vice Presidents'
])

job_level = st.sidebar.selectbox("Job Level", [
    'Entry-Level', 'Executive-Level', 'Management-Level', 'Mid-Level', 'Senior-Level'
])

job_location = st.sidebar.selectbox("Job Location", [
    'Atlanta, GA', 'Austin, TX', 'Boston, MA', 'Chicago, IL', 'Dallas, TX',
    'Denver, CO', 'Los Angeles, CA', 'New York, NY', 'San Francisco, CA', 'Seattle, WA'
])

# Prepare input DataFrame
input_df = pd.DataFrame({
    'Gender': [gender],
    'Years_Exp': [years_exp],
    'Edu_Level': [edu_level],
    'Job_Role': [job_role],
    'Job_Level': [job_level],
    'Job_Location': [job_location]
})

st.write("### 📝 Entered Details")
st.dataframe(input_df)

# Predict salary
if st.button("💰 Predict Salary"):
    prediction = model.predict(input_df)
    st.success(f"✅ Estimated Salary: ${prediction[0]:,.2f}")

