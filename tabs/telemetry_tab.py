import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def telemetry_tab(laps, drivers):
    st.markdown("""
    This telemetry overlay compares the fastest laps between two drivers. It allows detailed examination of speed traces across the circuit. Race engineers use this to assess how aggressive or conservative a driver was. Strategists evaluate driver pace under peak performance. Drivers can visualize where their competitor braked earlier or accelerated harder.
    """)
    st.subheader("Telemetry Comparison")
    st.markdown("Overlay two drivers' fastest laps to analyze speed profiles across the lap distance.")
    d1, d2 = st.selectbox("Driver 1", drivers), st.selectbox("Driver 2", drivers, index=1)
    l1 = laps.pick_driver(d1).pick_fastest()
    l2 = laps.pick_driver(d2).pick_fastest()
    t1 = l1.get_car_data().add_distance()
    t2 = l2.get_car_data().add_distance()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t1['Distance'], y=t1['Speed'], mode='lines', name=d1))
    fig.add_trace(go.Scatter(x=t2['Distance'], y=t2['Speed'], mode='lines', name=d2))
    fig.update_layout(title='Fastest Lap Speed Comparison', xaxis_title='Distance (m)', yaxis_title='Speed (km/h)')
    st.plotly_chart(fig, use_container_width=True)