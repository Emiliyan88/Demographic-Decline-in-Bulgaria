import streamlit as st
import pandas as pd

df = pd.read_csv("data/1.1.1.1. Population by sex_trend.xlsx")

st.title("🇧🇬 Demographic Decline Dashboard")

st.line_chart(df.set_index("Year")["Population"])

st.write("Data Overview")
st.dataframe(df)