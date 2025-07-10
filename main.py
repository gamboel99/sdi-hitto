
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SDI Hitto", layout="wide")

# ==== Custom CSS ====
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

tabs = st.tabs([
    "🏠 Beranda", "📘 Profil", "📖 Sejarah", "👥 Struktur Organisasi",
    "📚 Perpustakaan", "📝 Ujian Online", "🎓 Ekstrakurikuler", "📞 Hubungi Kami"
])

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

with tabs[1]:
    st.subheader("Profil Sekolah")
    st.write("SDI Hitto merupakan lembaga pendidikan dasar berbasis Islam yang berkomitmen mencetak generasi cerdas, berkarakter, dan islami.")

with tabs[2]:
    st.subheader("Sejarah Singkat")
    st.write("Didirikan tahun 2012 oleh Yayasan Hidayatuth Tholibin, SDI Hitto tumbuh sebagai sekolah yang mengintegrasikan pendidikan umum dan agama secara seimbang.")

with tabs[3]:
    st.subheader("Struktur Organisasi")
    st.markdown("""
    - **Kepala Sekolah**: Alfia Indra Oktafiani  
    - **Wakil Kepala Sekolah**: [diisi nanti]  
    - **Guru Kelas dan Ekstrakurikuler**: [diisi]  
    """)

with tabs[4]:
    st.subheader("Perpustakaan Digital")
    st.info("Fitur perpustakaan digital sedang dalam pengembangan. Akan berisi daftar buku dan materi bacaan yang dapat diakses siswa.")

with tabs[5]:
    st.subheader("Hasil Ujian Kelas 1")
    data_path = "data/hasil_ujian.csv"
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        st.dataframe(df)
        st.caption("Tabel di atas menampilkan nilai ujian siswa kelas 1.")
    else:
        st.warning("Data hasil ujian belum tersedia.")

with tabs[6]:
    st.subheader("Ekstrakurikuler SDI Hitto")

    ekstra = st.selectbox("Pilih Ekstrakurikuler", [
        "Pramuka", "Tari", "Lalaran", "Rebana", "Drumband", "Komputer / IT", "Lainnya"
    ])

    if ekstra == "Pramuka":
        st.subheader("⛺ Pramuka")
        st.write("Kegiatan Pramuka melatih kedisiplinan, kepemimpinan, dan kerja sama.")
    elif ekstra == "Tari":
        st.subheader("💃 Tari")
        st.write("Melatih kreativitas dan kepekaan seni lewat gerak tari daerah.")
    elif ekstra == "Lalaran":
        st.subheader("📖 Lalaran")
        st.write("Hafalan doa-doa pendek, ayat Al-Qur'an, dan hadits harian.")
    elif ekstra == "Rebana":
        st.subheader("🥁 Rebana")
        st.write("Grup rebana tampil di berbagai acara keagamaan sekolah.")
    elif ekstra == "Drumband":
        st.subheader("🎷 Drumband")
        st.write("Melatih kekompakan, ritme musik, dan performa dalam barisan.")
    elif ekstra == "Komputer / IT":
        st.subheader("💻 Komputer / IT")
        st.write("Pengenalan dasar komputer, aplikasi pendidikan, dan coding anak.")
    else:
        st.subheader("✨ Lainnya")
        st.write("Ekstrakurikuler lainnya sesuai minat siswa seperti menggambar, literasi, dll.")

with tabs[7]:
    st.subheader("Kontak Sekolah")
    st.write("📍 Alamat: Jl. Anggur no. 15 Ds. Tertek, RT/RW:1/6, Tertek, Pare")
    st.write("📧 Email: sdi.hitto@gmail.com")
    st.write("📞 Telepon: (0354) 123456")

st.markdown("""
<hr style='margin-top: 50px;'>
<center>
    <small>Developed by <strong>CV. Mitra Utama Consultindo (MUC)</strong></small>
</center>
""", unsafe_allow_html=True)
