import streamlit as st


st.title("Sidebar")
sb1=st.sidebar

with sb1:
  st.write("This is in the side bar")


text=st.text_input("Enter what you want to add to the sidebar")
but=st.button("Push to sidebar")

if but:
  sb1.write(text)
