import streamlit as st
import plotly.express as px

def pits_tab(laps):
    st.markdown("""
    Pit stop timing is critical in race strategy. This visualization maps out who pitted when, helping strategists analyze undercut or overcut attempts. Engineers assess execution accuracy, and drivers can evaluate how stop timing influenced their race. This high-level view supports post-race debriefs on pit timing effectiveness.
    """)
    st.subheader("Pit Stop Summary")
    st.markdown("This chart shows when drivers made their pit stops. The X-axis represents the lap, and each point represents a stop.")
    pit_laps = laps[laps['PitInTime'].notna()]
    fig = px.scatter(pit_laps, x='LapNumber', y='Driver', color='Compound', symbol='Compound', title='Pit Stops by Driver', labels={'LapNumber': 'Lap'})
    st.plotly_chart(fig, use_container_width=True)