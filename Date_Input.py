import streamlit as st


st.title("Date Input")

date=st.date_input("Choose date")

st.write(f"Date chosen is {date}")