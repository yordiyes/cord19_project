import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('data/cleaned_metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Slider for year selection
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display sample of data
st.write(filtered_df.head())

# Plot publications over selected years
year_counts = filtered_df['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Dropdown for selecting journal
journal_options = df['journal'].dropna().unique()
selected_journal = st.selectbox("Select Journal", journal_options)
journal_df = df[df['journal'] == selected_journal]
st.write(f"Papers from {selected_journal}")
st.write(journal_df.head())
