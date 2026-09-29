import streamlit as st

st.title("Form")

with st.form("My form"):
  name=st.text_input("Enter your name")
  age=st.slider("Pick your age",18,99)
  submitted=st.form_submit_button("Submit")

if submitted:
  st.write(f"Your name is {name} and age is {age}")
