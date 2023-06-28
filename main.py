import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache
def load_data():
    # Load some data
    df = pd.read_csv('renewable_power_plants_CH.csv')
    return df

df = load_data()

# Add title and header
st.title("Clean Energy Sources in Switzerland")
st.markdown("## Data Exploration")

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.sidebar.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(df)

# Visualize the data
if st.sidebar.checkbox("Show Bar Plot"):
    with st.spinner('Generating Bar Plot...'):
        st.subheader("Bar Plot")
        fig = px.bar(df, x='energy_source_level_1', y='electrical_capacity', color='canton', title='Electrical Capacity by Energy Source and Canton')
        st.plotly_chart(fig)

if st.sidebar.checkbox("Show Pie Chart"):
    with st.spinner('Generating Pie Chart...'):
        st.subheader("Pie Chart")
        # Group less frequent categories into 'Other'
        value_counts = df['energy_source_level_2'].value_counts()
        to_remove = value_counts[value_counts <= 10].index
        df_copy = df.copy()
        df_copy['energy_source_level_2_grouped'] = df_copy['energy_source_level_2'].replace(to_remove, 'Other')
        fig = px.pie(df_copy, names='energy_source_level_2_grouped', title='Distribution of Energy Sources')
        st.plotly_chart(fig)


if st.sidebar.checkbox("Show Heatmap"):
    with st.spinner('Generating Heatmap...'):
        st.subheader("Heatmap")
        plt.figure(figsize=(10,8))
        # Select only numerical columns
        numerical_df = df.select_dtypes(include=['float64', 'int64'])
        sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
        st.pyplot()

if st.sidebar.checkbox("Show Scatter Plot"):
    with st.spinner('Generating Scatter Plot...'):
        st.subheader("Scatter Plot")
        fig = px.scatter(df, x='commissioning_date', y='electrical_capacity', color='energy_source_level_1', title='Electrical Capacity by Commissioning Date and Energy Source')
        st.plotly_chart(fig)
