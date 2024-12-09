import streamlit as st

st.set_page_config(
    page_title="BioBytes",  # Sets the tab title
    page_icon="🫀",       # Sets the tab favicon (emoji or image URL)
    layout="wide",    # Can be "centered" or "wide"
    initial_sidebar_state="expanded"  # Can be "auto", "expanded", "collapsed"
)

st.image('https://em-content.zobj.net/source/apple/271/anatomical-heart_1fac0.png', width=150)
st.title("Portal Kesehatan BioBytes")

st.header("Menu Halaman")
st.page_link("Halaman_Utama.py", label="Halaman Utama", icon="🏠")
st.page_link("pages/1_Biodata_Pasien.py", label="Biodata Pasien", icon="🪪")
st.page_link("pages/2_Scan_dan_Diagnosa_EKG.py", label="Scan dan Diagnosa EKG", icon="🩺")
st.page_link("pages/3_Dashboard.py", label="Dashboard", icon="📊")

st.header("Tentang BioBytes")
st.write("Kami menyediakan sistem pendukung keputusan klinis berbasis web (CDSS) yang otomatis mengklasifikasikan data EKG, memberikan penilaian kondisi jantung secara cepat dan akurat. Dengan rekomendasi medis yang dapat langsung ditindaklanjuti, solusi kami membantu tenaga medis membuat keputusan tepat, bahkan di daerah dengan akses terbatas ke perawatan spesialis.")

st.header("Fitur Medis BioBytes")
st.markdown("- **Klasifikasi Detak Jantung ECG dengan CDSS:** Sistem berbasis AI yang mengklasifikasikan ECG untuk diagnosis aritmia secara cepat, akurat, dan memberikan rekomendasi tindakan medis yang tepat.")
st.markdown("- **Tele-ECG & Skrining Jantung Jarak Jauh:** Layanan skrining jantung jarak jauh melalui aplikasi berbasis web, memfasilitasi deteksi dini penyakit jantung, terutama di daerah dengan keterbatasan sumber daya medis.")
st.markdown("- **Rekomendasi Tindakan Medis Berbasis AI:** CDSS yang memberikan rekomendasi medis berdasarkan hasil klasifikasi ECG, mendukung pengambilan keputusan yang cepat dan tepat bagi tenaga medis.")
st.markdown("- **Peningkatan Akses Layanan Kesehatan:** Memberikan akses diagnosis jantung yang lebih baik bagi pasien di daerah terpencil, tanpa memerlukan spesialis kardiologi, dan mengurangi ketimpangan layanan kesehatan.")
st.markdown("- **Integrasi Data & Laporan Kesehatan:** Menyediakan laporan kesehatan yang mudah dipahami untuk pemantauan berkelanjutan, membantu pasien dan tenaga medis dalam pengelolaan penyakit jantung secara efisien.")
st.markdown("- **Memangkas Waktu & Meningkatkan Deteksi Dini:** Mempercepat diagnosis, terutama dalam situasi darurat, dan meningkatkan deteksi dini penyakit jantung, memastikan respons medis yang lebih cepat dan akurat.")


st.header("Statistik")
# Main title and subtitle
st.subheader("List Rumah Sakit yang telah bekerjasama")
st.markdown("""
Beberapa rumah sakit dan puskesmas telah ikut serta dalam layanan BioBytes 
dan sudah saling terkoneksi satu sama lain.
""")

# Layout with columns
col1, col2 = st.columns(2)

# First card
with col1:
    st.markdown("""
    <div style="text-align: center; padding: 20px; border: 2px solid #990c11; border-radius: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/3028/3028573.png" alt="Hospital Icon" style="width: 50px; margin-bottom: 10px;">
        <h3 style="margin: 0;">Rumah Sakit</h3>
        <p style="margin: 0; font-size: 18px; color: #333;">Status Pengampu</p>
        <h1 style="margin: 10px 0; color: #990c11;">60</h1>
    </div>
    """, unsafe_allow_html=True)

# Second card
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px; border: 2px solid #990c11; border-radius: 10px;">
        <img src="https://cdn-icons-png.freepik.com/256/6743/6743941.png" alt="RS/PKM Icon" style="width: 50px; margin-bottom: 10px;">
        <h3 style="margin: 0;">RS/PKM</h3>
        <p style="margin: 0; font-size: 18px; color: #333;">Status Diampu</p>
        <h1 style="margin: 10px 0; color: #990c11;">180</h1>
    </div>
    """, unsafe_allow_html=True)

# Add a background color if needed
st.markdown("""
<style>
    body {
        background-color: #F5F5F5;
    }
</style>
""", unsafe_allow_html=True)


# Create layout
col_left, col_right = st.columns([1, 2])

# Left column: Title and description
with col_left:
    st.subheader("List Dokter yang telah bekerjasama.")
    st.markdown("""
    Beberapa Dokter telah ikut serta dalam layanan telemedicine 
    dan sudah saling terkoneksi satu sama lain.
    """)

# Right column: Vertical cards
with col_right:
    for title, specialty, count, icon_url in [
        ("DR. SPESIALIS", "JANTUNG", 105, "https://cdn-icons-png.flaticon.com/512/6025/6025067.png"),
        ("DR. UMUM", "Dokter Umum", 350, "https://cdn-icons-png.flaticon.com/512/709/709043.png"),
    ]:
        st.markdown(f"""
        <div style="display: flex; align-items: center; padding: 15px; margin-bottom: 15px; border: 2px solid #990c11; border-radius: 10px;">
            <img src="{icon_url}" alt="Icon" style="width: 50px; margin-right: 20px;">
            <div style="flex-grow: 1;">
                <h3 style="margin: 0; font-size: 18px; color: #990c11;">{title}</h3>
                <p style="margin: 0; font-size: 14px; color: #555;">{specialty}</p>
            </div>
            <h1 style="margin: 0; color: #990c11;">{count}</h1>
        </div>
        """, unsafe_allow_html=True)

# Add a background color if needed
st.markdown("""
<style>
    body {
        background-color: #F5F5F5;
    }
</style>
""", unsafe_allow_html=True)
