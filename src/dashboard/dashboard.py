import streamlit as st
import pandas as pd
import json
import os

from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title("Real-Time AI Fraud Detection Dashboard")

# Auto refresh every 2 seconds
st_autorefresh(interval=2000, key="refresh")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = os.path.join(
    BASE_DIR,
    "../streaming/predictions.json"
)

ALERT_FILE = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "../streaming/alerts.json"
    )
)

# =========================
# LOAD PREDICTIONS
# =========================

if os.path.exists(LOG_FILE):

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)

    except:
        data = []

else:
    data = []

# =========================
# MAIN DASHBOARD
# =========================

if len(data) > 0:

    df = pd.DataFrame(data)

    total_transactions = len(df)

    fraud_count = len(
        df[df["prediction"] == "FRAUD"]
    )

    normal_count = len(
        df[df["prediction"] == "NORMAL"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Transactions",
        total_transactions
    )

    col2.metric(
        "Fraud Transactions",
        fraud_count
    )

    col3.metric(
        "Normal Transactions",
        normal_count
    )

    # =========================
    # ALERT SECTION
    # =========================

    st.subheader("Fraud Alerts")

    if os.path.exists(ALERT_FILE):

        try:
            with open(ALERT_FILE, "r") as f:
                alerts = json.load(f)

        except:
            alerts = []

    else:
        alerts = []

    if len(alerts) > 0:

        for alert in reversed(alerts):

            st.error(
                f"""
FRAUD DETECTED

Amount: ${alert['amount']}

Probability: {alert['probability']:.4f}
                """
            )

    else:
        st.success("No active fraud alerts")

    # =========================
    # LIVE PREDICTIONS
    # =========================

    st.subheader("Live Predictions")

    st.dataframe(
        df.sort_index(ascending=False),
        use_container_width=True
    )

    # =========================
    # PROBABILITY GRAPH
    # =========================

    st.subheader("Fraud Probability Distribution")

    st.line_chart(df["probability"])

else:

    st.warning("No predictions available yet")