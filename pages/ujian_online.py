import streamlit as st
import utils

st.title("Ujian / Ulangan Online")
user = st.text_input("Username")
if st.button("Login"):
    if utils.authenticate(user):
        st.success(f"{user} berhasil login!")
        st.write("Tampilkan soal & form jawab di sini…")
    else:
        st.error("Login gagal.")