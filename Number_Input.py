import streamlit as st


st.title("SIMPLE CALCULATOR")

num1=st.number_input("Enter the first number")
num2=st.number_input("Enter the second number")

cols=st.columns(4)

with cols[0]:
  add=st.button("Addition (+)")

with cols[1]:
  sub=st.button("Subtraction (-)")

with cols[2]:
  div=st.button("Division (/)")

with cols[3]:
  mul=st.button("Multiplication (*)")

if add:
  st.success(num1+num2)

if sub:
  st.success(num1-num2)

if div:
  st.success(num1/num2)

if mul:
  st.success(num1*num2)

