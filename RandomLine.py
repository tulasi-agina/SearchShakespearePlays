import random
import streamlit as st

st.write("Hello")

file = "Shakespeare_data.csv"
df = load_data()

st.write(df[4][2])
