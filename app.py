import streamlit as st
import pandas as pd

df = pd.read_csv("data/nsi_population.csv")

st.title("🇧🇬 Demographic Decline Dashboard")

st.line_chart(df.set_index("Year")["Population"])

st.write("Data Overview")
st.dataframe(df)