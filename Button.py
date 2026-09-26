import streamlit as st

Available_cars=["Toyota","Mercedes","Fiat","Benz"]

x=st.text_input("Type a car")
y=st.button("Check availability")

if y:
  if x in Available_cars:
    st.write("Car is available")
  else:
    st.write("Car is unavailable")