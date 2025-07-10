import streamlit as st
import pandas as pd
import base64
import requests

st.title("read CV from Github")

url = "https://raw.githubusercontent.com/amirfitri128/tobi_price/main/House_Price_Dataset.csv"

def load_data():
  return pd.read_csv(url)

try:
  df = load_data()
  st.success("Data loaded successfully!")
  st.dataframe(df)

except Exception as e:
  st.error("Failed to load data: {e}")
