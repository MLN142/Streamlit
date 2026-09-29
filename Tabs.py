import streamlit as st

st.title("TABS")

tabs=st.tabs(["FIRST TAB","SECOND TAB"])

with tabs[0]:
  st.header("This is the first tab")