import random
import streamlit as st
import pandas as pd

st.write("Hello")

file = "Shakespeare_data.csv"
df = pd.read_csv(file)

st.write(df.iat[4, 5])
