import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Tracking ID', 'Description', 'Status', 'Created At'])

def save_to_excel():
    st.session_state.df.to_excel("grievances.xlsx", index=False)

st.title("Grievance Portal")

# Grievance Submission
st.header("Submit a Grievance")
description = st.text_area("Enter your grievance:")
if st.button("Submit Grievance"):
    tracking_id = str(uuid.uuid4())
    new_grievance = pd.DataFrame({
        'Tracking ID': [tracking_id],
        'Description': [description],
        'Status': ['Submitted'],
        'Created At': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    })
    st.session_state.df = pd.concat([st.session_state.df, new_grievance], ignore_index=True)
    save_to_excel()
    st.success(f"Grievance submitted successfully. Your tracking ID is: {tracking_id}")

# Grievance Status Check
st.header("Check Grievance Status")
tracking_id_input = st.text_input("Enter your tracking ID:")
if st.button("Check Status"):
    grievance = st.session_state.df[st.session_state.df['Tracking ID'] == tracking_id_input]
    if not grievance.empty:
        st.write(grievance)
    else:
        st.error("Grievance not found. Please check your tracking ID.")

# Display all grievances (for demonstration purposes)
st.header("All Grievances")
st.write(st.session_state.df)

# Download Excel file
if st.button("Download Grievances Excel File"):
    save_to_excel()
    st.success("Excel file saved. You can find it in the same directory as this script.")