import streamlit as st

st.title("Select Box")
sb=st.selectbox("Choose your type",["Image","Video","Audio"],index=None)

if(sb=="Image"):
  st.image("media/basketball.jpg")
if(sb=="Video"):
  st.video("media/video.mp4")