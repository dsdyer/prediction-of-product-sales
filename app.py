import io
import streamlit as st
import pandas as pd
df = pd.read_csv('data/sales_predictions_2023_preprocessed.csv')


# Title
st.title("Prediction of Product Sales")

# Markdown headers
st.header("Product Sales Data")

# Display the dataframe
st.dataframe(df)


# Buttons
if st.button("Descriptive Statistics"):
  descriptive_stats = df.describe()
  st.dataframe(descriptive_stats)


if st.button("Summary Information"):
  buffer = io.StringIO()
  df.info(buf=buffer)
  summary_info = buffer.getvalue()
  st.text(summary_info)


if st.button("Null Values"):
  null_values = df.isnull().sum()
  st.write(null_values)


