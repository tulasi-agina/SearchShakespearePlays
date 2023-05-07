import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df
    
file = "Shakespeare_data.csv"
df = load_data()
create_data = {"Dataline": "number",
                "Play": "multiselect",
                "PlayerLinenumber": "number",
                "ActSceneLine": "text",
                "Player": "multiselect",
                "PlayerLine": "text"}

all_widgets = sp.create_widgets(df, create_data, ignore_columns=["Dataline"])
res = sp.filter_df(df, all_widgets)
st.title("Search Shakespeare")
st.header("Original DataFrame")
st.write(df)

st.header("Result DataFrame")
st.write(res)
