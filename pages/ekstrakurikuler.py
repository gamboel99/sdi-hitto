import streamlit as st

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
