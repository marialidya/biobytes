import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_icon="🫀",
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.title("Dashboard")

patient_data = r'patient_data.csv'
ecg_data = r'ecg_data.csv'

try:
    df = pd.read_csv(patient_data)
    st.header("Daftar Pasien")
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")

try:
    df = pd.read_csv(ecg_data)
    st.header("Daftar Unggah EKG Pasien")
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")

class_counts = df["Predicted Class"].value_counts().reset_index()
class_counts.columns = ["Predicted Class", "Count"]
class_counts["Percentage"] = (class_counts["Count"] / class_counts["Count"].sum()) * 100

fig = px.pie(
    class_counts,
    values="Count",
    names="Predicted Class",
    title="Predicted Class Distribution",
    hole=0.4,
    labels={"Predicted Class": "Class"},
)

fig.update_traces(
    textinfo="percent+label",
    hoverinfo="label+percent+value",
    textposition="inside"
)

st.title("Pie Chart Klasifikasi EKG")
st.plotly_chart(fig)

st.header("Bar Chart Jadwal Kunjungan Pasien")
try:
    df = pd.read_csv(patient_data)
    df['Input Time'] = pd.to_datetime(df['Input Time'].astype('str'))
    df_grouped = df.groupby(df['Input Time'].dt.date).size().reset_index(name='Count')
    df_grouped.columns = ['Input Time', 'Patient Count']
    st.subheader("Jumlah Kunjungan Pasien Per Hari")
    st.dataframe(df_grouped)
    st.bar_chart(data=df_grouped.set_index('Input Time'))
    
except FileNotFoundError:
    st.error(f"File '{patient_data}' tidak ditemukan. Pastikan Anda telah memasukkan data pasien.")
