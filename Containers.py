import streamlit as st


st.title("Containers")

with st.container(border=True):
  with st.expander("Expander 1"):
    st.write("This is in container 1")
  with st.expander("Expander 2"):
      st.write("This is also in container 1")
  