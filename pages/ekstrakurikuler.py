
import streamlit as st

def run():
    st.title("Ekstrakurikuler SDI Hitto")

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
