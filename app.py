import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Dashboard")
st.write("Upload a CSV file to view the sales dashboard.")

# File uploader
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Data preview
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Key metrics
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", df["Sales"].sum())
    col2.metric("Average Sales", round(df["Sales"].mean(), 2))
    col3.metric("Max Sale", df["Sales"].max())

    # Sales over time chart
    st.subheader("Sales Over Time")
    fig, ax = plt.subplots(figsize=(4,3))
    df.groupby("Date")["Sales"].sum().plot(ax=ax, marker="o")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=False)

    # Sales by product chart
    st.subheader("Sales by Product")
    fig2, ax2 = plt.subplots(figsize=(4,3))
    df.groupby("Product")["Sales"].sum().plot(kind="bar", ax=ax2)
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=False)

else:
    st.info("Please upload a CSV file to see the dashboard.")
