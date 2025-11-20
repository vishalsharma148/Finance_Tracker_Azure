import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from utils.azure_utils import analyze_sentiment, extract_keywords

st.set_page_config(page_title="Finance Tracker with Azure AI", layout="wide")

st.title("💰 Finance Tracker + Azure AI Insights")

# ------------------------------------------
# Upload Section
# ------------------------------------------
uploaded_file = st.file_uploader("Upload CSV with transactions", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📘 Raw Data")
    st.dataframe(df)

    # Ensure columns exist
    if "description" not in df.columns or "amount" not in df.columns:
        st.error("CSV must contain 'description' and 'amount' columns.")
    else:
        # ------------------------------------------
        # Apply Azure AI to each row
        # ------------------------------------------
        st.subheader("🧠 AI Sentiment & Keywords")

        df["sentiment"] = df["description"].apply(analyze_sentiment)
        df["keywords"] = df["description"].apply(extract_keywords)

        st.dataframe(df)

        # ------------------------------------------
        # Visualization
        # ------------------------------------------
        st.subheader("📊 Spending Overview")

        fig, ax = plt.subplots()
        ax.plot(df.index, df["amount"])
        ax.set_xlabel("Transaction")
        ax.set_ylabel("Amount")
        ax.set_title("Expense Trend")
        st.pyplot(fig)

        # ------------------------------------------
        # Monthly Report
        # ------------------------------------------
        st.subheader("📅 Monthly Summary")

        total_spent = df["amount"].sum()
        pos = sum(df["sentiment"] == "positive")
        neg = sum(df["sentiment"] == "negative")
        neu = sum(df["sentiment"] == "neutral")

        st.write(f"**Total Spent:** ₹{total_spent}")
        st.write(f"**Positive transactions:** {pos}")
        st.write(f"**Negative transactions:** {neg}")
        st.write(f"**Neutral transactions:** {neu}")

        st.success("AI-powered monthly summary generated.")
else:
    st.info("Upload a CSV to begin.")