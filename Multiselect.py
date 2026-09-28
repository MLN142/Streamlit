import streamlit as st

if "company" not in st.session_state:
  st.session_state.company=["","",""]

st.title("MULTISELECT")

companies=st.multiselect("Choose your favorate company",["AMAZON","APPLE","TCS"])
cols=st.columns(3)

def add_company(name):
  for i in range(3):
      if st.session_state.company[i]=="":
        st.session_state.company[i]=name
        break;

def remove_company(name):
  index=st.session_state.company.index(name)
  st.session_state.company[index]=""
  for i in range(index,2):
    temp=st.session_state.company[i]
    st.session_state.company[i]=st.session_state.company[i+1]
    st.session_state.company[i+1]=temp
   
if("AMAZON" in companies and "AMAZON" not in st.session_state.company ):
  add_company("AMAZON")

elif("AMAZON" not in companies and "AMAZON" in st.session_state.company):
  remove_company("AMAZON")


if("APPLE" in companies and "APPLE" not in st.session_state.company ):
   add_company("APPLE")

elif("APPLE" not in companies and "APPLE" in st.session_state.company):
  remove_company("APPLE")


if("TCS" in companies and "TCS" not in st.session_state.company ):
   add_company("TCS")

elif("TCS" not in companies and "TCS" in st.session_state.company):
  remove_company("TCS")



for i in range(3):
  if st.session_state.company[i]!="":
    with cols[i]:
      st.write("You have selected",st.session_state.company[i])

    

st.write(st.session_state.company)


   



  




