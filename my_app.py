import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Personal Budget Tracker", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Add Transaction", "View Summary", "Upload/Download Data", "About"])

# Initialize session state
if 'transactions' not in st.session_state:
    st.session_state['transactions'] = pd.DataFrame(columns=["Date", "Type", "Category", "Amount", "Description"])

# Convert Date column for compatibility
if not st.session_state['transactions'].empty:
    st.session_state['transactions']['Date'] = pd.to_datetime(st.session_state['transactions']['Date'])

# Page: Add Transaction
if page == "Add Transaction":
    st.title("➕ Add New Transaction")
    with st.form("transaction_form"):
        date = st.date_input("Date")
        t_type = st.selectbox("Type", ["Income", "Expense"])
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        description = st.text_input("Description")
        submitted = st.form_submit_button("Add")
        if submitted:
            new_data = pd.DataFrame([[date, t_type, category, amount, description]],
                                    columns=["Date", "Type", "Category", "Amount", "Description"])
            st.session_state['transactions'] = pd.concat(
                [st.session_state['transactions'], new_data], ignore_index=True)
            st.success("Transaction added!")

# Page: View Summary
elif page == "View Summary":
    st.title("📊 Budget Summary")
    df = st.session_state['transactions']
    if df.empty:
        st.info("No transactions available.")
    else:
        total_income = df[df["Type"] == "Income"]["Amount"].sum()
        total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
        balance = total_income - total_expense

        col1, col2, col3 = st.columns(3)
        col1.metric("Income", f"KES {total_income:,.2f}")
        col2.metric("Expense", f"KES {total_expense:,.2f}")
        col3.metric("Balance", f"KES {balance:,.2f}")

        st.subheader("📋 Transactions")
        st.dataframe(df, use_container_width=True)

        st.subheader("📊 Expense Distribution")
        expense_df = df[df["Type"] == "Expense"]
        if not expense_df.empty:
            pie_data = expense_df.groupby("Category")["Amount"].sum()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

        st.subheader("📅 Spending Over Time")
        time_summary = df.groupby(['Date', 'Type'])["Amount"].sum().unstack(fill_value=0)
        st.line_chart(time_summary)

# Page: Upload/Download Data
elif page == "Upload/Download Data":
    st.title("📁 Data Management")

    st.subheader("⬇️ Download Transactions")
    csv = st.session_state['transactions'].to_csv(index=False)
    st.download_button("Download as CSV", csv, "transactions.csv", "text/csv")

    st.subheader("⬆️ Upload Transactions CSV")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        new_df = pd.read_csv(uploaded)
        new_df['Date'] = pd.to_datetime(new_df['Date'])
        st.session_state['transactions'] = pd.concat(
            [st.session_state['transactions'], new_df], ignore_index=True)
        st.success("Data uploaded successfully!")

# Page: About
elif page == "About":
    st.title("📘 About This App")
    st.markdown("""
        This Personal Budget Tracker helps you:
        - Add and categorize income & expenses
        - Visualize spending trends
        - Export and import your data easily

        Built with 💚 using [Streamlit](https://streamlit.io)
    """)
