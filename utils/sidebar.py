# utils/sidebar.py

import streamlit as st
import fastf1

def session_sidebar():
    st.sidebar.image("img/logo.jpeg", width=240)
    st.sidebar.header("Session Selection")

    year = st.sidebar.selectbox("Year", list(range(2024, 2017, -1)))

    with st.spinner("Loading races..."):
        try:
            all_races = fastf1.get_event_schedule(year).Location.tolist()
        except Exception:
            all_races = []

        if not all_races:
            st.error("No races found for the selected year.")
            st.stop()

    gp = st.sidebar.selectbox("Grand Prix", all_races)

    session_dict = {"Race": "R", "Qualifying": "Q", "Practice": "FP1"}
    session_label = st.sidebar.selectbox("Session Type", list(session_dict.keys()))
    session_type = session_dict[session_label]

    st.sidebar.markdown("---")

    return year, gp, session_type
