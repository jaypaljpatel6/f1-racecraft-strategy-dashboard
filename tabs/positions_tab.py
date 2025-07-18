import streamlit as st
import plotly.express as px

def positions_tab(laps):
    st.markdown("""
    This tracker shows race position evolution lap-by-lap. Drivers can review their progress or loss over time. Strategists identify moments when track position changed significantly, which may correlate with pit stops, SC periods, or battles. It helps evaluate overall race execution and overtaking patterns.
    """)
    st.subheader("Position Tracker")
    st.markdown("Track position changes lap-by-lap for every driver in the field.")
    df_positions = laps[['Driver', 'LapNumber', 'Position']].dropna()
    fig = px.line(df_positions, x='LapNumber', y='Position', color='Driver', title="Driver Position Over Race", labels={'LapNumber': 'Lap', 'Position': 'Race Position'})
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)