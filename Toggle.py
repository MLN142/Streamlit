import streamlit as st

st.title("Toggle Video")


cols1=st.columns(2)
with cols1[0]:
  toggle1=st.toggle("Show Video")

with cols1[1]:
  toggle2=st.toggle("Show Image")



if toggle1:
  st.video("media/video.mp4")

if toggle2:
  st.image("media/basketball.jpg")

