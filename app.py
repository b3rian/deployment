"""
# Budget Tracker App
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("💰 Personal Budget Tracker App")

# Initialize session state for transactions if not already done
if 'transactions' not in st.session_state:
    st.session_state['transactions'] = pd.DataFrame(columns=['Date', 'Type', 'Category', 
                                                              'Amount', 'Description'])
 
# User transactions data
st.subheader("➕ Add New Transaction")
with st.form("transaction_form"):
    date = st.date_input("Date")
    t_type = st.selectbox("Type", ["Income", "Expense"])
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0, step =0.01)
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        new_transaction = pd.DataFrame([[date, t_type, category, amount, description]],
                                columns=["Date", "Type", "Category", "Amount", "Description"])
        st.session_state['transactions'] = pd.concat([st.session_state['transactions'], new_transaction], ignore_index=True)
        st.success("Transaction added successfully!")

# Display transactions
st.subheader("📊 Transactions Overview")
st.dataframe(st.session_state['transactions'], use_container_width=True)
 

