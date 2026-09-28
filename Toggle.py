import streamlit as st

if "video" not in st.session_state:
  st.session_state.video=False

if "audio" not in st.session_state:
  st.session_state.audio=False




st.title("Toggle Video")


if st.session_state.video==True:
  st.video("media/video.mp4")

if st.session_state.audio==True:
  st.image("media/basketball.jpg")



cols1=st.columns(2)
with cols1[0]:
  toggle1=st.toggle("Show Video")
  if toggle1==True:
    st.session_state.video=True
  else:
    st.session_state.video=False


with cols1[1]:
  toggle2=st.toggle("Show Image")
  if toggle2:
    st.session_state.audio=True
  else:
    st.session_state.audio=False




