import streamlit as st

st.header("Say Hello")

if st.button("Say Hello"):
    st.write("HELLO THERE")
else:
    st.write("Goodbye instead")