import streamlit as st

st.title("Color Picker")

color=st.color_picker("pick a color")
st.write(f"the color you have selected is {color}")