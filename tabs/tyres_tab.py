import streamlit as st
import plotly.express as px

def tyres_tab(laps):
    st.markdown("""
    Tyre strategy visualization summarizes how often each compound was used and for how long. This gives insight into tyre preference and durability. Strategists assess which tyres performed best, while engineers evaluate wear patterns. It also helps compare strategy aggressiveness between teams. This cleaned-up format avoids clutter while maintaining value.
    """)
    st.subheader("Tyre Strategy")
    st.markdown("This tab previously focused on raw tyre compound degradation trends, but due to visual clutter and low interpretability, we present a cleaner analysis below.")
    tyre_stints = laps.groupby(['Driver', 'Compound'])['Stint'].nunique().reset_index()
    tyre_stints.columns = ['Driver', 'Compound', 'NumStints']
    fig = px.bar(tyre_stints, x='Driver', y='NumStints', color='Compound', title='Number of Tyre Stints by Compound per Driver')
    st.plotly_chart(fig, use_container_width=True)