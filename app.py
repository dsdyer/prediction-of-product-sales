import streamlit as st
import pandas as pd
df = pd.read_csv('data/sales_predictions_2023_preprocessed.csv')


# Title
st.title("Prediction of Product Sales")

# Markdown headers
st.header("Product Sales Data")

# Display the dataframe
st.dataframe(df)

if st.button("Descriptive Statistics"):
  descriptive_stats = df.describe()
  st.dataframe(descriptive_stats)

if st.button("Summary Information"):
  summary_info = df.info()
  st.write("Summary Information:")
  st.dataframe(summary_info)

if st.button("Null Values"):
  null_values = df.isnull().sum()
  st.write("Null Values:")
  st.write(null_values)


