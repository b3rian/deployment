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


   
     


 

