import streamlit as st


st.title("Expander Widget")

st.image("media/basketball.jpg")

with st.expander("See Explanation"):
  st.write("This is the image of a person playing basketball")