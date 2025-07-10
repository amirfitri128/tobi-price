import streamlit as st
import pandas as pd
import base64
import request

st.title("read CV from Github")

url = "https://raw.githubusercontent.com/limfw/temp/main/data.csv"

def load_data():
  return pd.read_csv(url)

try:
  df = load_data()
  st.success("Data loaded successfully!")
  st.dataframe(df)

except Exception as e:
  ste.error(f"Failed to load data: {e})
