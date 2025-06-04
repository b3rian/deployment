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
st.session_state['transactions']['Date'] = pd.to_datetime(st.session_state['transactions']['Date'])
st.dataframe(st.session_state['transactions'], use_container_width=True)

# Summary
st.subheader("📈 Summary")

df = st.session_state['transactions']

if not df.empty:
    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = total_income - total_expense

    st.metric("Total Income", f"KES {total_income:,.2f}")
    st.metric("Total Expense", f"KES {total_expense:,.2f}")
    st.metric("Net Balance", f"KES {balance:,.2f}")

    # Visualization
    st.subheader("📊 Expense Distribution by Category")
    expense_df = df[df["Type"] == "Expense"]
    if not expense_df.empty:
        pie_data = expense_df.groupby("Category")["Amount"].sum()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

    st.subheader("📅 Spending Over Time")
    df['Date'] = pd.to_datetime(df['Date'])
    time_summary = df.groupby(['Date', 'Type'])["Amount"].sum().unstack(fill_value=0)
    st.line_chart(time_summary)
else:
    st.info("No transactions yet.")

st.subheader("📤 Export Data")
csv = df.to_csv(index=False)
st.download_button("Download as CSV", csv, file_name="budget_data.csv", mime="text/csv")

st.subheader("📥 Upload CSV")
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    df_upload = pd.read_csv(uploaded_file)
    st.session_state['transactions'] = pd.concat([st.session_state['transactions'], df_upload], ignore_index=True)
    st.success("Data uploaded successfully!")


 

