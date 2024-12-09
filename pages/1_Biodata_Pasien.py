import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Biodata Pasien",
    page_icon="🫀",
    layout="wide", 
    initial_sidebar_state="expanded"
)

csv_file = "patient_data.csv"

try:
    df_existing = pd.read_csv(csv_file)
except FileNotFoundError:
    df_existing = pd.DataFrame(columns=["Patient ID", "Age", "Gender", "Systolic BP",
    "Diastolic BP", "Total Cholesterol (mg/dL)", "HDL Cholesterol (mg/dL)", "Input Time", "Input By"])
    df_existing.to_csv(csv_file, index=False)
    
st.title("Biodata Pasien")

st.write("Silakan masukkan biodata pasien dan informasi kesehatan yang diambil secara langsung pada tanggal periksa melalui form di bawah ini.")

with st.form("my_form"):
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
    submit_button = st.form_submit_button("Submit")

if submit_button:
    input_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
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
    df_existing = pd.concat([df_existing, new_df], ignore_index=True)
    df_existing.to_csv(csv_file, index=False)

    st.write("Data Pasien:")
    st.dataframe(new_df)

    st.success("Data berhasil disimpan!")

    if submit_button:
        st.page_link("pages/2_Scan_dan_Diagnosa_EKG.py", label="Unggah Hasil Scan EKG Pasien", icon = "⬆")
