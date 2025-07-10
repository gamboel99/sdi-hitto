import streamlit as st
import base64

st.set_page_config(page_title="SDI Hitto", layout="wide")

# ==== CSS Style ====
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
    .sidebar-content {
        background-color: #e6ffe6;
        padding: 20px;
        border-left: 2px solid #006600;
    }
</style>
""", unsafe_allow_html=True)

# ==== HEADER ====
st.markdown('<div class="header">SDI HIDAYATUTH THOLIBIN</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Website resmi SDI Hitto - Cerdas dan Islami</div>', unsafe_allow_html=True)
st.markdown("---")

# ==== KONTEN ====
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📰 Kegiatan Terkini")
    st.markdown("**Manasik Haji SDI Hitto Tahun 2025**")
    st.image("https://via.placeholder.com/800x400.png?text=Kegiatan+Manasik+Haji")
    st.write("""
    Manasik Haji adalah latihan pelaksanaan ibadah haji yang dilakukan oleh siswa SDI Hitto. 
    Kegiatan ini diikuti oleh seluruh siswa dari kelas 1 hingga kelas 6. 
    Tujuannya adalah memberikan pemahaman dan keterampilan kepada siswa tentang pelaksanaan rukun Islam ke-5.
    """)

with col2:
    st.markdown("### 📌 Recent Posts")
    st.markdown("""
    - Manasik Haji 2025
    - Kunjungan ke Kebun Binatang
    - Peringatan Maulid Nabi
    - Latihan Upacara
    """)

    st.markdown("### 💬 Recent Comments")
    st.markdown("""
    - *Ust. Ahmad* on Manasik Haji
    - *Bu Wali Kelas* on Kegiatan Literasi
    """)

st.markdown("---")
