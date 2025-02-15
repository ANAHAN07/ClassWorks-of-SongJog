import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("GO to", ["Home", "Projects", "Skills", "Contant"])

if page == "Home":
    st.title("Welcome to my Portfolio!")
    st.write("Hi, I am Ahnaf Mahmud Towseem Ahan")
    st.write("This is my portpholio")

elif page == "Projects":
    st.title("My Projects!")
    st.subheader("TASK MANAGER OS")
    st.write("This project is an OS to do your task perfectly")
    st.markdown("[Github Profile](https://github.com/ANAHAN07)")