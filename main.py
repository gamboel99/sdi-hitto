import streamlit as st
import pandas as pd
import os
import pages.ekstrakurikuler as ekstra

st.set_page_config(page_title="SDI Hitto", layout="wide")

# ==== Custom CSS for Header and Background ====
st.markdown("""
<style>
    .main {
        background-color: #ccffcc;
    }
    .header {
        background-color: #006600;
        padding: 20px;
        display: flex;
        align-items: center;
        gap: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .header img {
        height: 70px;
    }
    .header-title {
        color: white;
        font-size: 28px;
        font-weight: bold;
    }
    .subheader {
        font-size: 16px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==== Logo Handling ====
logo = "https://raw.githubusercontent.com/gamboel99/sdi-hitto/main/uploads/logo.png"

st.markdown(f'''
<div class="header">
    <img src="{logo}">
    <div>
        <div class="header-title">SD ISLAM HIDAYATUTH THOLIBIN</div>
        <div class="subheader">Website Resmi SDI Hitto - Cerdas & Islami</div>
    </div>
</div>
''', unsafe_allow_html=True)

# ==== Tabs Menu ====
tabs = st.tabs([
    "🏠 Beranda", 
    "📘 Profil", 
    "📖 Sejarah", 
    "👥 Struktur Organisasi", 
    "📚 Perpustakaan", 
    "📝 Ujian Online", 
    "🎓 Ekstrakurikuler", 
    "📞 Hubungi Kami"
])

# ========== Tab: Beranda ==========
with tabs[0]:
    st.title("Selamat Datang di SDI Hitto")
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
    st.success("Website ini memuat informasi lengkap tentang SDI Hitto termasuk kegiatan siswa, hasil belajar, dan layanan digital.")

# ========== Tab: Profil ==========
with tabs[1]:
    st.subheader("Profil Sekolah")
    st.write("SDI Hitto merupakan lembaga pendidikan dasar berbasis Islam yang berkomitmen mencetak generasi cerdas, berkarakter, dan islami.")

# ========== Tab: Sejarah ==========
with tabs[2]:
    st.subheader("Sejarah Singkat")
    st.write("Didirikan tahun 2012 oleh Yayasan Hidayatuth Tholibin, SDI Hitto tumbuh sebagai sekolah yang mengintegrasikan pendidikan umum dan agama secara seimbang.")

# ========== Tab: Struktur Organisasi ==========
with tabs[3]:
    st.subheader("Struktur Organisasi")
    st.write("Berikut struktur kepemimpinan SDI Hitto:")
    st.markdown("""
    - **Kepala Sekolah**: Alfia Indra Oktafiani  
    - **Wakil Kepala Sekolah**: [diisi nanti]  
    - **Guru Kelas dan Ekstrakurikuler**: [diisi]  
    """)

# ========== Tab: Perpustakaan ==========
with tabs[4]:
    st.subheader("Perpustakaan Digital")
    st.info("Fitur perpustakaan digital sedang dalam pengembangan. Akan berisi daftar buku dan materi bacaan yang dapat diakses siswa.")

# ========== Tab: Ujian Online ==========
with tabs[5]:
    st.subheader("Hasil Ujian Kelas 1")
    data_path = "data/hasil_ujian.csv"
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        st.dataframe(df)
        st.caption("Tabel di atas menampilkan nilai ujian siswa kelas 1.")
    else:
        st.warning("Data hasil ujian belum tersedia.")

# ========== Tab: Ekstrakurikuler ==========
with tabs[6]:
    def run():
    st.title("Ekstrakurikuler SDI Hitto")

    ekstra = st.selectbox("Pilih Ekstrakurikuler", [
        "Pramuka", "Tari", "Lalaran", "Rebana", "Drumband", "Komputer / IT", "Lainnya"
    ])

    if ekstra == "Pramuka":
        st.subheader("⛺ Pramuka")
        st.write("Kegiatan Pramuka di SDI Hitto melatih kedisiplinan, kepemimpinan, dan kerja sama dalam regu.")
    elif ekstra == "Tari":
        st.subheader("💃 Tari")
        st.write("Ekstrakurikuler tari melestarikan seni budaya Nusantara melalui gerakan tradisional.")
    elif ekstra == "Lalaran":
        st.subheader("📖 Lalaran")
        st.write("Kegiatan melafalkan hafalan-hafalan bacaan doa, ayat pendek, dan hadits.")
    elif ekstra == "Rebana":
        st.subheader("🥁 Rebana")
        st.write("Grup rebana SDI Hitto mengiringi acara Islami seperti Maulid, PHBI, dan wisuda.")
    elif ekstra == "Drumband":
        st.subheader("🎷 Drumband")
        st.write("Latihan ritme dan kekompakan barisan serta musik marching band.")
    elif ekstra == "Komputer / IT":
        st.subheader("💻 Komputer / IT")
        st.write("Pengantar dunia digital: mengetik, coding dasar, dan pengenalan internet sehat.")
    else:
        st.subheader("✨ Lainnya")
        st.write("Ekstrakurikuler lain seperti olahraga, menggambar, atau literasi sesuai minat siswa.")
# ========== Tab: Hubungi Kami ==========
with tabs[7]:
    st.subheader("Kontak Sekolah")
    st.write("📍 Alamat: Jl. Anggur no. 15 Ds. Tertek, RT/RW:1/6, Tertek, Pare")
    st.write("📧 Email: sdi.hitto@gmail.com")
    st.write("📞 Telepon: (0354) 123456")
