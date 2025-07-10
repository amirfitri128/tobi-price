import streamlit as st
import pandas as pd
import base64
import requests

st.title("read CV from Github")

url = "https://raw.githubusercontent.com/amirfitri128/tobi-price/main/House_Price_Dataset.csv"

def load_data():
  return pd.read_csv(url)

try:
  df = load_data()
  st.success("Data loaded successfully!")
  st.dataframe(df)

except Exception as e:
  st.error("Failed to load data: {e}")

">>https://github.com/settings/personal-access-tokens "
a = st.text_input("Enter a")
b = st.text_input("Enter b")
c = st.text_input("Enter c")

if st.button("Uploadnto Github"):
  df = pd.DataFrame([{"a": a, "b": b, "c": c}])
  csv = df.to_csv(index=False)
  content = base64.b64encode(csv.encode()).decode()

url = "https://api.github.com/repos/amirfitri128/tobi-price/data2.csv"
