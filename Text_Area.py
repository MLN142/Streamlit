import streamlit as st


st.title("ABOUT ME")

am=st.text_area("Tell me about yourself",placeholder="Write Here")

but1=st.button("Tell me")

if but1:
  st.write(am)
