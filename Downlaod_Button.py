import streamlit as st

st.image("media/basketball.jpg",caption="basketball.jpg")
file_name=st.text_input("Enter File name to be downloaded")

if(file_name=="basketball.jpg"):
  st.image("media/basketball.jpg")
  st.write("Is this the image you want to download?")
  with open("media/basketball.jpg","rb") as file:
    st.download_button(
      label="Downlaod",
      data=file,
      file_name=file_name,
      mime="image/jpg"
    )
