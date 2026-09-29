import streamlit as st


st.title("File Uploader")

file=st.file_uploader("Uploaded an image")
but=st.button("Show image")

if but:

  st.write("Uploaded Image:")

  st.image(file)