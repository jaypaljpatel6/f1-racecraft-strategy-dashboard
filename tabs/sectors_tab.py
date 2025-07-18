import streamlit as st
import plotly.express as px
import pandas as pd

def sectors_tab(laps, drivers):
    st.markdown("""
    Sector times help identify where on the circuit a driver gains or loses time. Engineers can pinpoint technical limitations in specific track zones. Strategists may use this data to evaluate if a driver has potential to execute overtakes. For drivers, sector analysis reveals strengths and weaknesses in cornering or acceleration zones. It's a valuable diagnostic tool post-race.
    """)
    st.subheader("Sector Breakdown")
    st.markdown("Compare how a driver performs across different sectors over the race.")
    d = st.selectbox("Driver", drivers)
    l = laps.pick_driver(d)
    df = pd.DataFrame({
        'LapNumber': l['LapNumber'],
        'Sector 1': l['Sector1Time'].dt.total_seconds(),
        'Sector 2': l['Sector2Time'].dt.total_seconds(),
        'Sector 3': l['Sector3Time'].dt.total_seconds()
    })
    fig = px.line(df, x='LapNumber', y=['Sector 1', 'Sector 2', 'Sector 3'], title=f"{d} Sector Times", labels={'value': 'Sector Time (s)', 'LapNumber': 'Lap'})
    st.plotly_chart(fig, use_container_width=True)