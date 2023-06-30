import streamlit as st

st.title("Tweet Application")

st.subheader("🚀 Generate tweets on any topic")

st.text_input("Topic")
st.text_input("Number of tweets")

st.button("Generate")