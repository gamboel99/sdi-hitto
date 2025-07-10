import streamlit as st

def run():
    st.title("Ekstrakurikuler SDI Hitto")

    ekstra = st.selectbox("Pilih Ekstrakurikuler", [
        "Pramuka", "Tari", "Lalaran", "Rebana", "Drumband", "Komputer / IT", "Lainnya"
    ])

    if ekstra == "Pramuka":
        st.subheader("⛺ Pramuka")
        st.write("Melatih kedisiplinan, kepemimpinan, dan kerja sama dalam regu.")
    elif ekstra == "Tari":
        st.subheader("💃 Tari")
        st.write("Mengenalkan gerakan tradisional dan seni tari daerah.")
    elif ekstra == "Lalaran":
        st.subheader("📖 Lalaran")
        st.write("Melatih hafalan doa, hadits, dan ayat pendek.")
    elif ekstra == "Rebana":
        st.subheader("🥁 Rebana")
        st.write("Grup rebana mengiringi kegiatan islami dan lomba.")
    elif ekstra == "Drumband":
        st.subheader("🎷 Drumband")
        st.write("Pelatihan ritme dan marching band.")
    elif ekstra == "Komputer / IT":
        st.subheader("💻 Komputer / IT")
        st.write("Pengenalan komputer, mengetik, coding dasar.")
    else:
        st.subheader("✨ Lainnya")
        st.write("Ekstrakurikuler tambahan: menggambar, olahraga, literasi.")
