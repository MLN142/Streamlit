import streamlit as st
import time

st.title("Empty Widget")

ph=st.empty()
ph.write("This is a text")

button1=st.button("Click here to generate another button")
if button1:
  button2=ph.button("Here is the second button")

