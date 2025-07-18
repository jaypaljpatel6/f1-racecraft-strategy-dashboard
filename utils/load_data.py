# utils/load_data.py

import fastf1
import os
import streamlit as st

def load_session_data(year, gp, session_type):
    os.makedirs("./f1_cache", exist_ok=True)
    fastf1.Cache.enable_cache("./f1_cache")

    with st.spinner("Loading session data... this may take a few seconds..."):
        try:
            session = fastf1.get_session(year, gp, session_type)
            session.load()
            laps = session.laps.copy()
            laps["LapTimeSeconds"] = laps["LapTime"].dt.total_seconds()
            drivers = sorted(laps["Driver"].unique())
            return session, laps, drivers
        except Exception as e:
            st.error(f"Failed to load session data: {e}")
            st.stop()
