import streamlit as st
import plotly.express as px
import pandas as pd

def head_to_head_tab(laps, drivers):
    st.markdown("""
    This head-to-head delta chart compares lap times between two drivers directly. Stakeholders can evaluate pace consistency and superiority over each lap. Race engineers might use this to benchmark drivers. The zero line indicates parity, with deviations favoring one driver or the other.
    """)
    st.subheader("Head-to-Head Delta")
    st.markdown("Compare two drivers' lap times directly and visualize who was faster per lap.")
    d1, d2 = st.selectbox("Driver A", drivers), st.selectbox("Driver B", drivers, index=1)
    l1 = laps[laps['Driver'] == d1].sort_values("LapNumber")
    l2 = laps[laps['Driver'] == d2].sort_values("LapNumber")
    merged = pd.merge(l1[['LapNumber', 'LapTimeSeconds']], l2[['LapNumber', 'LapTimeSeconds']], on='LapNumber', suffixes=(f'_{d1}', f'_{d2}'))
    merged['Delta'] = merged[f'LapTimeSeconds_{d1}'] - merged[f'LapTimeSeconds_{d2}']
    fig = px.line(merged, x='LapNumber', y='Delta', title=f"Lap Time Delta: {d1} vs {d2}", labels={'LapNumber': 'Lap', 'Delta': f'{d1} - {d2} Lap Time Delta (s)'})
    fig.add_hline(y=0, line_dash="dot", line_color="gray")
    st.plotly_chart(fig, use_container_width=True)