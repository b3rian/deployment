import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📊 Interactive Data Explorer")

uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✅ Data loaded successfully!")
    st.write(df.head())
else:
    st.warning("Please upload a file to get started.")

if uploaded_file:
    st.subheader("🔍 Dataset Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Shape of dataset**")
        st.write(df.shape)

        st.write("**Column types**")
        st.write(df.dtypes)

    with col2:
        st.write("**Missing values**")
        st.write(df.isnull().sum())

        st.write("**Summary statistics**")
        st.write(df.describe())

st.subheader("🧹 Filter the Dataset")

filter_columns = st.multiselect("Select columns to filter by:", df.columns)

for col in filter_columns:
    if df[col].dtype == 'object':
        options = df[col].unique()
        selected = st.multiselect(f"Values for {col}:", options, default=list(options))
        df = df[df[col].isin(selected)]
    else:
        min_val, max_val = float(df[col].min()), float(df[col].max())
        selected = st.slider(f"Range for {col}:", min_val, max_val, (min_val, max_val))
        df = df[(df[col] >= selected[0]) & (df[col] <= selected[1])]

st.write("### Filtered Data")
st.dataframe(df)

st.subheader("📈 Data Visualization")

chart_type = st.selectbox("Choose chart type", ["Scatter Plot", "Histogram", "Box Plot", "Line Chart"])

if chart_type:
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    if chart_type == "Scatter Plot":
        x_axis = st.selectbox("X-axis", numeric_cols)
        y_axis = st.selectbox("Y-axis", numeric_cols)
        color = st.selectbox("Color by (optional)", [None] + list(categorical_cols))
        fig = px.scatter(df, x=x_axis, y=y_axis, color=color)
        st.plotly_chart(fig)

    elif chart_type == "Histogram":
        col = st.selectbox("Column", numeric_cols)
        bins = st.slider("Number of bins", 5, 100, 30)
        fig = px.histogram(df, x=col, nbins=bins)
        st.plotly_chart(fig)

    elif chart_type == "Box Plot":
        y_axis = st.selectbox("Y-axis", numeric_cols)
        x_axis = st.selectbox("X-axis (categorical)", categorical_cols)
        fig = px.box(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)

    elif chart_type == "Line Chart":
        x_axis = st.selectbox("X-axis", numeric_cols)
        y_axis = st.selectbox("Y-axis", numeric_cols)
        fig = px.line(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)
 
st.subheader("⬇️ Download Filtered Data")

@st.cache_data
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode("utf-8")

csv_data = convert_df_to_csv(df)
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="filtered_data.csv",
    mime="text/csv",
)
  


 

