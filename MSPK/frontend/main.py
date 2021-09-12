import streamlit as st
import requests

st.title("Simle web app with SQLite, Python and Kubenetes")

employee_id = st.sidebar.selectbox("Pick the EmployeeId to see details", 
                (1,2,3,4,5,6,7,8,9,10))

params = {"EmployeeId": employee_id}
response = requests.get("http://backend:8000/employees", params=params)
employee_info = response.json()

st.write(employee_info)
