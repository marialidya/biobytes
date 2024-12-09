import streamlit as st
import pandas as pd

st.set_page_config(
    page_icon="🫀",
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.title("Dashboard")

# Path to your CSV file
patient_data = r'patient_data.csv'
ecg_data = r'ecg_data.csv'

# Read the CSV file into a Pandas DataFrame
try:
    df = pd.read_csv(patient_data)
    st.header("Daftar Pasien")
    st.dataframe(df)  # Display the DataFrame in Streamlit
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")

# Read the CSV file into a Pandas DataFrame
try:
    df = pd.read_csv(ecg_data)
    st.header("Daftar Unggah EKG Pasien")
    st.dataframe(df)  # Display the DataFrame in Streamlit
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")

st.header("Bar Chart")
# Read the CSV file
try:
    df = pd.read_csv(patient_data)

    # Ensure 'Input Time' is in datetime format
    df['Input Time'] = pd.to_datetime(df['Input Time'])

    # Group data by 'Input Time' and count occurrences
    df_grouped = df.groupby(df['Input Time'].dt.date).size().reset_index(name='Count')

    # Rename columns for clarity
    df_grouped.columns = ['Input Time', 'Patient Count']

    # Display grouped data
    st.write("### Patient Count by Input Date")
    st.dataframe(df_grouped)

    # Create a bar chart
    st.bar_chart(data=df_grouped.set_index('Input Time'))
    
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")
