import streamlit as st

st.set_page_config(page_title="SDI Hitto", layout="wide")

# ==== Custom CSS for Green Theme and Header ====
st.markdown("""
<style>
    body {
        background-color: #ccffcc;
    }
    .main > div {
        background-color: #ccffcc;
    }
    .header {
        background-color: #006600;
        padding: 20px;
        color: white;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
    }
    .subheader {
        text-align: center;
        font-size: 18px;
        color: white;
        margin-top: -10px;
    }
</style>
""", unsafe_allow_html=True)

# ==== Header Section ====
st.markdown('<div class="header">SDI HIDAYATUTH THOLIBIN</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Website Resmi SDI Hitto - Cerdas dan Islami</div>', unsafe_allow_html=True)
st.markdown("---")

# ==== Navigation Toolbar (simulated using tabs) ====
tabs = st.tabs(["Beranda", "Profil", "Sejarah", "Struktur Organisasi", "Perpustakaan", "Ujian Online", "Hubungi Kami"])

with tabs[0]:
    st.title("Beranda SDI Hitto")
    st.markdown("""
    **NPSN**: 69946459  
    **Status**: Swasta  
    **Bentuk Pendidikan**: SD  
    **Status Kepemilikan**: Yayasan  
    **SK Pendirian Sekolah**: Notaris No. 001  
    **Tanggal SK Pendirian**: 2012-01-05  
    **SK Izin Operasional**: 421/1653/418.47/2016  
    **Tanggal SK Izin Operasional**: 2016-05-10  
    **Kepala Sekolah**: Alfia Indra Oktafiani
    """)

    st.info("Selamat datang di Website SDI Hitto. Silakan pilih menu lain untuk melihat informasi lebih lanjut.")

with tabs[6]:
    st.subheader("Hubungi Kami")
    st.write("Alamat: Jl. Pendidikan No.1, Desa Keling, Kediri, Jawa Timur")
    st.write("Email: sdi.hitto@gmail.com")
    st.write("Telepon: (0354) 123456")