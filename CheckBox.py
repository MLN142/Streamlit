import streamlit as st

st.title("CHECKBOXES")

check=st.checkbox("Do you agree to terms and services")
if check:
  st.write("THANKS FOR AGREEING")

cols=st.columns(2)

with cols[0]:
  col1=st.checkbox("col1")

with cols[1]:
  col1=st.checkbox("col2")


cols2=st.columns(2)
with cols2[0]:
  col1=st.checkbox("col3")

with cols2[1]:
  col1=st.checkbox("col4")