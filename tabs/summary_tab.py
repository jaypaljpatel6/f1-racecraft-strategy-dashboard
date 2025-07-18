import streamlit as st
import plotly.express as px

def summary_tab(laps):
    st.markdown("""
    This tab summarizes key metrics for reporting and exporting. Analysts and media teams may download the data for further usage. It includes core statistics like average pace, compound usage, and stint lengths. This offers a race-level snapshot of driver performance for comparative review.
    """)
    st.subheader("Summary & Export")
    st.markdown("View summary metrics for each driver and download tables or charts for reporting.")
    summary = laps.groupby('Driver').agg({
        'LapTimeSeconds': ['mean', 'min', 'max'],
        'Stint': 'nunique',
        'Compound': 'nunique'
    })
    summary.columns = ['Avg Lap', 'Fastest Lap', 'Slowest Lap', 'Stints', 'Compounds Used']
    st.dataframe(summary.round(2))
    st.download_button("Download Summary as CSV", summary.to_csv().encode('utf-8'), file_name="f1_summary.csv")