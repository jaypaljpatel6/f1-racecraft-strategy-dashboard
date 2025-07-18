import streamlit as st
import plotly.express as px

def tyre_life_tab(laps):
    st.markdown("""
    Tyre life modeling estimates how long each compound lasted for each driver. Engineers use it to evaluate tyre performance limits. Strategists can cross-check this with race plans. It informs on which compound held up well across different driving styles and conditions. This helps tailor compound selection for future races.
    """)
    st.subheader("Tyre Life Model")
    st.markdown("This model aggregates stint durations across compounds to visualize tyre longevity and race strategy.")
    tyre_life = laps.groupby(['Driver', 'Compound', 'Stint'])['LapNumber'].count().reset_index()
    tyre_life.columns = ['Driver', 'Compound', 'Stint', 'LapsInStint']
    fig = px.box(tyre_life, x='Compound', y='LapsInStint', color='Compound', points='all', title='Stint Lengths per Compound')
    st.plotly_chart(fig, use_container_width=True)