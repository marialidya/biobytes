import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Biodata Pasien",
    page_icon="🫀",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# File where data will be stored
csv_file = "patient_data.csv"

# Check if the CSV file already exists, otherwise create it with headers
try:
    df_existing = pd.read_csv(csv_file)
except FileNotFoundError:
    df_existing = pd.DataFrame(columns=["Patient ID", "Age", "Gender", "Systolic BP",
    "Diastolic BP", "Total Cholesterol (mg/dL)", "HDL Cholesterol (mg/dL)", "Input Time", "Input By"])
    df_existing.to_csv(csv_file, index=False)  # Create an empty file with headers
    
# Title of the app
st.title("Biodata Pasien")

st.write("Silakan masukkan biodata pasien dan informasi kesehatan yang diambil secara langsung pada tanggal periksa melalui form di bawah ini.")

# Create a form
with st.form("my_form"):
    # Add input fields in the form
    st.header("Informasi Umum Pasien")
    control_date = st.date_input("Tanggal Periksa")
    patient_id = st.text_input("Patient ID")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female"])

    st.header("Informasi Kesehatan Pasien")
    systolic_bp = st.number_input("Systolic Blood Pressure (mm Hg)", min_value = 90, max_value = 200)
    diastolic_bp = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value = 60, max_value = 130)
    total_cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value = 130, max_value = 320)
    hdl_cholesterol =  st.number_input("HDL Cholesterol (mg/dL)", min_value = 20, max_value = 100)
    input_by = st.selectbox("Input By", ["Nurse A", "Nurse B"])
    # input_by = st.text_input("Input By")  # Input by field
    submit_button = st.form_submit_button("Submit")

# Display the result after the form is submitted
if submit_button:
    # Get the current timestamp
    input_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a new data dictionary to append
    new_data = {
        "Control Date": [control_date],
        "Patient ID": [patient_id],
        "Age": [age],
        "Gender": [gender],
        "Systolic BP": [systolic_bp],
        "Diastolic BP": [diastolic_bp],
        "Total Cholesterol (mg/dL)": [total_cholesterol],
        "HDL Cholesterol (mg/dL)": [hdl_cholesterol],
        "Input By": [input_by],
        "Input Time": [input_time]
    }

    new_df  = pd.DataFrame(new_data)
    
    # Append the new data to the existing DataFrame
    df_existing = pd.concat([df_existing, new_df], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    df_existing.to_csv(csv_file, index=False)

    # Display the updated table
    st.write("Data Pasien:")
    st.dataframe(new_df)

    st.success("Data berhasil disimpan!")

 # Add the "Upload ECG and go to the next page" button
    if submit_button:
        st.page_link("pages/2_Scan_dan_Diagnosa_EKG.py", label="Unggah Hasil Scan EKG Pasien", icon = "⬆")
