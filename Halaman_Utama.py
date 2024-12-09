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
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

st.header("Layanan Medis")
st.write("Layanan Prediksi dan Diagnosa EKG adalah lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

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
        <img src="https://cdn-icons-png.flaticon.com/512/2936/2936924.png" alt="Hospital Icon" style="width: 50px; margin-bottom: 10px;">
        <h3 style="margin: 0;">Rumah Sakit</h3>
        <p style="margin: 0; font-size: 18px; color: #333;">Status Pengampu</p>
        <h1 style="margin: 10px 0; color: #990c11;">xxx</h1>
    </div>
    """, unsafe_allow_html=True)

# Second card
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px; border: 2px solid #990c11; border-radius: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/3050/3050517.png" alt="RS/PKM Icon" style="width: 50px; margin-bottom: 10px;">
        <h3 style="margin: 0;">RS/PKM</h3>
        <p style="margin: 0; font-size: 18px; color: #333;">Status Diampu</p>
        <h1 style="margin: 10px 0; color: #990c11;">xxx</h1>
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
        ("DR. SPESIALIS", "JANTUNG", 360, "https://cdn-icons-png.flaticon.com/512/2917/2917995.png"),
        ("DR. UMUM", "Dokter Umum", 999, "https://cdn-icons-png.flaticon.com/512/2392/2392364.png"),
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