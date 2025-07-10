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
headers = {"Authorization": f"token {st.secrets['github']['token']}"}

payload = {
  "message": "Add data.csv",
  "content": content,
  "branch": "main"

}

r = requests.put(url, headers=headers, json=payload)
if r.status_code in [200,201]:
  st.success("data Uploaded!")
else:
  st.error("failed to upload")
