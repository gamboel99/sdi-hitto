import streamlit as st
import os

st.title("Perpustakaan Digital")
path = "uploads/perpustakaan"
if os.path.exists(path):
    files = os.listdir(path)
    for f in files:
        with open(f"{path}/{f}", "rb") as file:
            st.download_button(label=f"📄 {f}", data=file, file_name=f)
else:
    st.warning("Belum ada file perpustakaan.")