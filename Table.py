import streamlit as st


st.title("Tables and Metrics")
st.metric("Wind Speed","100ms",-50)

table={"Column 1":[1,2,3,4,5],"Columns 2":[6,7,8,9,10]}
st.table(table)
st.dataframe(table)

