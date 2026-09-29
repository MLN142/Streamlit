import streamlit as st


st.title("Time Input")

time=st.time_input("Choose Time")

st.write(f"Time chosen is {time}")