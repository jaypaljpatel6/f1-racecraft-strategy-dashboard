import streamlit as st
import plotly.express as px

def lap_times_tab(laps, drivers, show_avg = False):
    st.markdown("""
    This tab provides an overview of lap-by-lap performance for selected drivers. Analysts and engineers can use this to study how pace evolves across the race, while strategists may detect performance drop-offs due to tyre degradation or track conditions. Consistent lap times indicate good tyre and energy management. Drivers benefit from reviewing their pace trends to spot inconsistencies. This visualization supports decision-making on stint lengths and optimal push windows.
    """)
    st.subheader("Lap Time Trends")
    st.markdown("Analyze lap-by-lap pace and consistency, with optional 3-lap rolling averages to smooth out noise.")
    selected = st.multiselect("Select Drivers", drivers, default=drivers[:3])
    for d in selected:
        l = laps.pick_driver(d).pick_quicklaps()
        fig = px.line(l, x='LapNumber', y='LapTimeSeconds', title=f'{d} Lap Times', labels={'LapNumber': 'Lap', 'LapTimeSeconds': 'Lap Time (s)'})
        if show_avg:
            l['Avg'] = l['LapTimeSeconds'].rolling(3).mean()
            fig.add_scatter(x=l['LapNumber'], y=l['Avg'], mode='lines', name=f'{d} Avg')
        st.plotly_chart(fig, use_container_width=True)