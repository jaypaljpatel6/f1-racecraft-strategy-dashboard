import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def undercut_tab(laps, drivers):
    st.markdown("""
    Undercut analysis helps quantify the gain or loss from pitting earlier or later than a competitor. Strategists use this to refine future pit stop timings. It informs whether a driver benefited from clear air or suffered due to cold tyres. This visualization supports decision-making for pit window planning.
    """)
    st.subheader("Undercut Analysis")
    st.markdown("Evaluate the lap-time advantage gained or lost during pit stop undercut or overcut scenarios between any two drivers.")
    d1, d2 = st.selectbox("Undercut Driver A", drivers), st.selectbox("Undercut Driver B", drivers, index=1)
    l1 = laps[laps['Driver'] == d1]
    l2 = laps[laps['Driver'] == d2]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=l1['LapNumber'], y=l1['LapTimeSeconds'], mode='lines', name=d1))
    fig.add_trace(go.Scatter(x=l2['LapNumber'], y=l2['LapTimeSeconds'], mode='lines', name=d2))
    fig.update_layout(title='Undercut Comparison', xaxis_title='Lap', yaxis_title='Lap Time (s)')
    st.plotly_chart(fig, use_container_width=True)