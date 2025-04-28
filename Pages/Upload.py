import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from firebase_db import save_prediction

def show_upload(model):
    st.title("📤 Upload Transactions and Detect Fraud")

    uploaded_file = st.file_uploader("Upload your credit card transaction CSV file", type=["csv"], key="upload_csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Preview of Uploaded Data")
        st.dataframe(df.head())

        try:
            required_features = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8',
                                 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16',
                                 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24',
                                 'V25', 'V26', 'V27', 'V28', 'Amount']

            input_data = df[required_features]
            predictions = model.predict(input_data)

            df["Prediction"] = predictions
            df["Status"] = df["Prediction"].apply(lambda x: "✅ Legit" if x == 0 else "🚨 Fraud")

            st.subheader("🔍 Prediction Results")
            fraud_only = st.checkbox("🚨 Show Fraud Only", value=False)

            if fraud_only:
                fraud_df = df[df["Prediction"] == 1]
                st.dataframe(fraud_df[["Time", "Amount", "Status"]])
            else:
                st.dataframe(df[["Time", "Amount", "Status"]])

            # 🔽 Download Button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Full Prediction CSV", csv, "fraud_predictions.csv", "text/csv")

            # 📈 Graphs
            fraud_count = (df["Prediction"] == 1).sum()
            legit_count = (df["Prediction"] == 0).sum()
            total = len(df)

            st.subheader("📈 Fraud Report Summary")
            st.markdown(f"""
            - 🧾 Total Transactions: `{total}`
            - ✅ Legit Transactions: `{legit_count}`
            - 🚨 Fraud Transactions: `{fraud_count}`
            - 🔎 Fraud Rate: `{(fraud_count / total * 100):.2f}%`
            """)

            fig1, ax1 = plt.subplots()
            ax1.pie([legit_count, fraud_count], labels=["Legit", "Fraud"], autopct='%1.1f%%')
            st.pyplot(fig1)

            fig2, ax2 = plt.subplots()
            ax2.bar(["Legit", "Fraud"], [legit_count, fraud_count], color=['green', 'red'])
            ax2.set_ylabel("Number of Transactions")
            st.pyplot(fig2)

            # 🧠 Save predictions into Firestore
            for idx, row in df.iterrows():
                save_prediction(
                    username=st.session_state.user,
                    time=row["Time"],
                    amount=row["Amount"],
                    status=row["Status"]
                )

            st.success("✅ Predictions saved successfully!")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

    # Navigation
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()
