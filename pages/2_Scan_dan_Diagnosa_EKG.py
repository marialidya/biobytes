import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import pandas as pd
from datetime import datetime

import cv2
import tempfile

st.set_page_config(
    page_icon="🫀",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Pre-trained model
model = load_model(r"MobileNetV2.h5")

class_names = ['S', 'M', 'Q', 'N', 'P', 'V']

def predict(path_image, model):
    image = cv2.imread(path_image, cv2.IMREAD_UNCHANGED)

    if image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    image = cv2.resize(image, (128, 128))
    image_array = image / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])
    return class_names[predicted_class], confidence

csv_file = "ecg_data.csv"

try:
    df_existing = pd.read_csv(csv_file)
except FileNotFoundError:
    df_existing = pd.DataFrame(columns=["Patient ID", "Control Date",
                                        "Input Time", "Input By", "ECG Image", "Predicted Class", "Confidence"])
    df_existing.to_csv(csv_file, index=False)

if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None
    st.session_state.confidence = None
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'temp_path' not in st.session_state:
    st.session_state.temp_path = None
if 'control_date' not in st.session_state:  
    st.session_state.control_date = None
if 'patient_id' not in st.session_state:  
    st.session_state.patient_id = None
if 'input_time' not in st.session_state:  
    st.session_state.input_time = None
if 'input_by' not in st.session_state:  
    st.session_state.input_by = None

st.title("Image Classification with Transfer Learning")

st.markdown("Pada halaman ini, Anda dapat mengunggah hasil scan EKG pasien dan memberikan diagnosa.")

with st.form("my_form"):
    st.header("Informasi Umum Pasien")
    patient_id = st.text_input("ID Pasien")
    control_date = st.date_input("Tanggal Periksa")
    input_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    input_by = st.selectbox("Input By", ["Nurse A", "Nurse B"])

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    submit_button = st.form_submit_button("Submit")

if submit_button and uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    st.session_state.uploaded_image = uploaded_file
    st.session_state.temp_path = temp_path

if st.session_state.uploaded_image is not None:
    ecg_image = cv2.imread(st.session_state.temp_path, cv2.IMREAD_GRAYSCALE)
    st.image(ecg_image, caption="Uploaded ECG Image (Grayscale)", use_container_width=True)

if st.button("Predict"):
    with st.spinner("Classifying..."):
        if 'temp_path' in st.session_state:
            predicted_class, confidence = predict(st.session_state.temp_path, model)
            st.session_state.prediction_result = predicted_class
            st.session_state.confidence = confidence

            new_entry = {
                "Patient ID": st.session_state.patient_id,
                "Control Date": st.session_state.control_date,
                "Input Time": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Input By": st.session_state.input_by,
                "ECG Image": st.session_state.temp_path,
                "Predicted Class": st.session_state.prediction_result,
                "Confidence": st.session_state.confidence
            }

            new_df = pd.DataFrame([new_entry]) 
            df_existing = pd.concat([df_existing, new_df], ignore_index=True)

            df_existing.to_csv(csv_file, index=False)

            st.header(f"Hasil Diagnosa Pasien {patient_id}")
            
            st.success(f"Prediction: {predicted_class} with {confidence * 100:.2f}% confidence")

            if predicted_class == "N":
                # For "N" (Normal Beats)
                st.write(f"Klasifikasi diagnosa awal kondisi jantung pasien {patient_id} berdasarkan scan EKG yang diunggah adalah **Normal Beats (N)**.")
                st.subheader("Rekomendasi Tindakan")
                st.markdown("- **Tidak ada tindakan lebih lanjut** yang diperlukan jika pasien tidak memiliki gejala.")
                st.markdown("- Tetap **jadwalkan pemeriksaan ulang** setiap 6-12 bulan, sesuai dengan usia dan faktor risiko pasien.")
                st.markdown("- **Catatan Medis:** Pastikan untuk mencatat bahwa hasilnya normal dalam rekam medis pasien.")

                st.subheader("Pesan Darurat")
                st.markdown('<p style="color:green;"><strong>Hasil normal, tidak ada tindakan lebih lanjut diperlukan. Jadwalkan pemeriksaan rutin.</p>', unsafe_allow_html=True)

                if st.button("Jadwalkan Pemeriksaan Ulang"):
                    st.write("Pemeriksaan ulang berhasil dijadwalkan.")
                    
            elif predicted_class == "S":
                # For "S" (Supraventricular Tachycardia)
                st.write(f"Klasifikasi diagnosa awal kondisi jantung pasien {patient_id} berdasarkan scan EKG yang diunggah adalah **Supraventricular Tachycardia (S)**.")
                st.subheader("Rekomendasi Tindakan")
                st.markdown("- **Pemantauan lebih lanjut** jika pasien merasa gejala seperti jantung berdebar, pusing, atau sesak napas.")
                st.markdown("- Jika gejala sering muncul atau memburuk, **rujuk ke spesialis kardiologi** untuk penilaian lebih lanjut.")
                st.markdown("- **Observasi** secara berkala untuk memastikan tidak ada perubahan dalam irama yang lebih serius.")
                
                st.subheader("Pesan Darurat")
                st.markdown('<p style="color:yellow;"><strong>Gangguan irama ringan, tidak mengancam jiwa. Pantau gejala dan konsultasikan jika memburuk.</p>', unsafe_allow_html=True)

                if st.button("Rujuk ke Spesialis Kardiologi"):
                    st.write("Pasien berhasil dirujuk ke spesialis kardiologi.")

            elif predicted_class == "V":
                # For "V" (Ventricular Beats)
                st.write(f"Klasifikasi diagnosa awal kondisi jantung pasien {patient_id} berdasarkan scan EKG yang diunggah adalah **Ventricular Beats (V)**.")
                st.subheader("Rekomendasi Tindakan")
                st.markdown("- **Rujukan segera** ke unit gawat darurat terdekat untuk penilaian lebih lanjut dan pemantauan EKG kontinu.")
                st.markdown("- **Lakukan echocardiogram** untuk memeriksa struktur jantung jika ada riwayat penyakit jantung atau keluhan terkait.")
                st.markdown("- **Pemantauan intensif** di rumah sakit jika terjadi gejala seperti pingsan atau nyeri dada.")
                
                st.subheader("Pesan Darurat")
                st.markdown('<p style="color:red;"><strong>Kondisi kritis. Segera rujuk ke spesialis untuk pemeriksaan lebih lanjut!</p>', unsafe_allow_html=True)

                if st.button("Hubungi Ambulans"):
                    st.write("Berhasil menghubungi ambulans.")
            
            elif predicted_class == "M":
                # For "M" (Myocardial Infarction)
                st.write(f"Klasifikasi diagnosa awal kondisi jantung pasien {patient_id} berdasarkan scan EKG yang diunggah adalah **Myocardial Infarction (M)**.")
                st.subheader("Rekomendasi Tindakan")
                st.markdown("- **Segera rujuk** ke rumah sakit terdekat atau unit gawat darurat.")
                st.markdown("- Jika di lokasi awal, **berikan aspirin 300 mg** dan **nitrogliserin** (jika tidak ada kontraindikasi) sebelum pasien dibawa ke rumah sakit.")
                st.markdown("- **Lakukan terapi reperfusi** (PCI atau trombolisis) di rumah sakit untuk memperbaiki aliran darah ke jantung.")
                
                st.subheader("Pesan Darurat")
                st.markdown('<p style="color:red;"><strong>Serangan jantung terdeteksi! Segera bawa ke rumah sakit untuk penanganan darurat.</strong></p>', unsafe_allow_html=True)

                if st.button("Hubungi Ambulans"):
                    st.write("Berhasil menghubungi ambulans.")

            elif predicted_class == "Q":
                # For "Q" (Premature Ventricular Contractions - PVCs)
                st.write(f"Klasifikasi diagnosa awal kondisi jantung pasien {patient_id} berdasarkan scan EKG yang diunggah adalah **Premature Ventricular Contractions (PVCs)**.")
                st.subheader("Rekomendasi Tindakan")
                st.markdown("- **Observasi** jika pasien tidak menunjukkan gejala tambahan.")
                st.markdown("- Jika gejala berlanjut atau bertambah parah, lakukan **Holter monitoring** untuk melacak frekuensi PVC.")
                st.markdown("- **Evaluasi lebih lanjut** jika gejala berupa pusing atau nyeri dada terjadi, dan rujuk ke spesialis.")
                
                st.subheader("Pesan Darurat")
                st.markdown('<p style="color:yellow;"><strong>Gangguan irama ringan, tidak berbahaya. Pantau jika gejala berlanjut.</strong></p>', unsafe_allow_html=True)

                if st.button("Rujuk ke Spesialis Kardiologi"):
                    st.write("Berhasil menghubungi spesialis kardiologi.")

            elif predicted_class == "P":
                # For "P" (Idioventricular Rhythms)
                st.write(f"Klasifikasi diagnosa awal kondisi jantung pasien {patient_id} berdasarkan scan EKG yang diunggah adalah **Idioventricular Rhythms (P)**.")
                st.subheader("Rekomendasi Tindakan")
                st.markdown("- **Rujuk segera** ke spesialis kardiologi untuk evaluasi lebih lanjut, karena idioventricular rhythms dapat menandakan masalah jantung yang serius.")
                st.markdown("- **Pemantauan ketat** di rumah sakit atau fasilitas kesehatan dengan EKG kontinu jika pasien menunjukkan gejala serius (seperti pingsan).")
                st.markdown("- Lakukan **echocardiogram** dan tes lainnya untuk mengidentifikasi kemungkinan penyebab atau kondisi terkait.")
                
                st.subheader("Pesan Darurat")
                st.markdown('<p style="color:orange;"><strong>Gangguan irama ventrikel, perlu evaluasi segera.</strong></p>', unsafe_allow_html=True)

                if st.button("Rujuk ke Spesialis Kardiologi"):
                    st.write("Berhasil menghubungi spesialis kardiologi.")

        else:
            st.error("Image not found. Please upload an image before predicting.")
