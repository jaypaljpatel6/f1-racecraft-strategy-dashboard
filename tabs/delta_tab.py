import streamlit as st
import plotly.express as px

def delta_tab(laps, drivers):
    st.markdown("""
    This analysis tracks a selected driver's time gap to the race leader. Strategists and drivers can see when they gained or lost time relative to P1. It helps identify strategic or pace-based differences and can highlight the impact of pit stops or traffic. The gap trend tells a story of overall competitiveness.
    """)
    st.subheader("Delta to Leader")
    st.markdown("Select a driver to see their gap to the race leader across each lap.")
    driver_selected = st.selectbox("Driver for Delta", drivers)
    laps['DeltaToLeader'] = laps['Time'].dt.total_seconds() - laps.groupby('LapNumber')['Time'].transform('min').dt.total_seconds()
    df_delta = laps[laps['Driver'] == driver_selected][['LapNumber', 'DeltaToLeader']]
    fig = px.line(df_delta, x='LapNumber', y='DeltaToLeader', title=f"{driver_selected} - Delta to Leader by Lap", labels={'LapNumber': 'Lap', 'DeltaToLeader': 'Gap (s)'})
    st.plotly_chart(fig, use_container_width=True)