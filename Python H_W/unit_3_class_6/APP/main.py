import streamlit as st

st.title("GAME HUB")
st.write("Here you will get all genuine links of crack games.")

name = st.text_input("Enter your name:")
st.write("Hello,", name)

num = st.number_input("Enter the number")


st.selectbox("Choose", ["BMW", "TOYOTA", "AMG"])


st.button("Touch me")

st.file_uploader("Upload file")
st.progress(100)