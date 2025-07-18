import streamlit as st
import plotly.express as px

def rating_tab(laps):
    st.markdown("""
    Driver ratings distill performance across pace, consistency, and tyre longevity. Teams can use this for internal evaluation. It supports driver coaching and benchmarking. The scoring model emphasizes low average lap times, low variance (consistency), and high tyre conservation. The table and bar chart provide a clear ranking for stakeholders.
    """)
    st.subheader("Driver Rating")
    st.markdown("Driver ratings are calculated using a combination of consistency, tyre management, and raw pace.")
    st.markdown("""
    **Methodology:**
    - Lower average lap times yield higher scores.
    - Standard deviation of lap times (consistency) penalizes erratic performance.
    - Longer average tyre life gives bonus points for conservation.

    **Formula:**
    ```
    Rating = 100 - 10*(AvgLapTime - MinAvg) - 2*StdDev
    ```
    """)
    rating_df = laps.groupby('Driver').agg({
        'LapTimeSeconds': ['mean', 'std'],
        'TyreLife': 'mean'
    })
    rating_df.columns = ['Avg Lap Time', 'Consistency (StdDev)', 'Avg Tyre Life']
    rating_df['Rating'] = 100 - (rating_df['Avg Lap Time'] - rating_df['Avg Lap Time'].min()) * 10 - rating_df['Consistency (StdDev)'] * 2
    st.dataframe(rating_df.sort_values("Rating", ascending=False).round(2))
    fig = px.bar(rating_df.reset_index().sort_values("Rating", ascending=False), x='Driver', y='Rating', title='Overall Driver Rating')
    st.plotly_chart(fig, use_container_width=True)