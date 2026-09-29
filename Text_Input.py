import streamlit as st

st.title("TEXT INPUT")

first=st.text_input("Enter your first name")
last=st.text_input("Enter your last name")

button=st.button("Show Name")

if button and not first and not last:
  st.write("Please enter your name.")

elif button and first and last:
  st.write(f"Hello {first} {last}")