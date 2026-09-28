import streamlit as st


st.title("SLIDER")
if "size" not in st.session_state:
  st.session_state.size=500





st.session_state.size=st.slider("CHOOSE SIZE OF THE IMAGE",100,1000,100)
st.image("media/basketball.jpg",width=st.session_state.size)