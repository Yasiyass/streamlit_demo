import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import seaborn as sns

# Load some data
df = pd.read_csv('renewable_power_plants_CH.csv')

# Add title and header
st.title("Clean Energy Sources in Switzerland")
st.header("Data Exploration")

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.header("This is my dataset:")
    st.dataframe(df)
    # st.table(data=iris)
    # st.write(data=iris)

# Visualize the data
if st.checkbox("Show Bar Plot"):
    st.header("Bar Plot")
    fig = px.bar(df, x='energy_source_level_1', y='electrical_capacity', color='canton', title='Electrical Capacity by Energy Source and Canton')
    st.plotly_chart(fig)

if st.checkbox("Show Pie Chart"):
    st.header("Pie Chart")
    # Group less frequent categories into 'Other'
    value_counts = df['energy_source_level_2'].value_counts()
    to_remove = value_counts[value_counts <= 10].index
    df['energy_source_level_2_grouped'] = df['energy_source_level_2'].replace(to_remove, 'Other')
    fig = px.pie(df, names='energy_source_level_2_grouped', title='Distribution of Energy Sources')
    st.plotly_chart(fig)


if st.checkbox("Show Heatmap"):
    st.header("Heatmap")
    plt.figure(figsize=(10,8))
    # Select only numerical columns
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
    st.pyplot()


if st.checkbox("Show Scatter Plot"):
    st.header("Scatter Plot")
    fig = px.scatter(df, x='commissioning_date', y='electrical_capacity', color='energy_source_level_1', title='Electrical Capacity by Commissioning Date and Energy Source')
    st.plotly_chart(fig)
