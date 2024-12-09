import streamlit as st
import pandas as pd
import plotly.express as px

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

# Calculate counts and percentages
class_counts = df["Predicted Class"].value_counts().reset_index()
class_counts.columns = ["Predicted Class", "Count"]
class_counts["Percentage"] = (class_counts["Count"] / class_counts["Count"].sum()) * 100

# Create a pie chart using Plotly
fig = px.pie(
    class_counts,
    values="Count",
    names="Predicted Class",
    title="Predicted Class Distribution",
    hole=0.4,  # Adds a donut-style chart
    labels={"Predicted Class": "Class"},
)

# Add percentages to the hover tooltip
fig.update_traces(
    textinfo="percent+label",
    hoverinfo="label+percent+value",
    textposition="inside"
)

# Display in Streamlit
st.title("Pie Chart Klasifikasi EKG")
st.plotly_chart(fig)

st.header("Bar Chart Jadwal Kunjungan Pasien")
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
    st.subheader("Jumlah Kunjungan Pasien Per Hari")
    st.dataframe(df_grouped)

    # Create a bar chart
    st.bar_chart(data=df_grouped.set_index('Input Time'))
    
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")
