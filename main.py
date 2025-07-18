# main.py
# Entry point for Streamlit app

import streamlit as st
from utils.load_data import load_session_data
from utils.sidebar import session_sidebar
from tabs.lap_times_tab import lap_times_tab
from tabs.sectors_tab import sectors_tab
from tabs.telemetry_tab import telemetry_tab
from tabs.tyres_tab import tyres_tab
from tabs.pits_tab import pits_tab
from tabs.positions_tab import positions_tab
from tabs.delta_tab import delta_tab
from tabs.head_to_head_tab import head_to_head_tab
from tabs.undercut_tab import undercut_tab
from tabs.tyre_life_tab import tyre_life_tab
from tabs.rating_tab import rating_tab
from tabs.summary_tab import summary_tab

st.set_page_config("F1 Strategy Dashboard", layout="wide")
st.title("RaceCraft IQ: Post-Race Strategy Intelligence")

# Sidebar
year, gp, session_type = session_sidebar()

# Load session
session, laps, drivers = load_session_data(year, gp, session_type)

# Tabs
tabs = st.tabs([
    "Lap Times", "Sectors", "Telemetry", "Tyres", "Pits", "Positions",
    "Delta to Leader", "Head-to-Head", "Undercut Analysis",
    "Tyre Life Model", "Driver Rating", "Summary & Export"
])

with tabs[0]: lap_times_tab(laps, drivers)
with tabs[1]: sectors_tab(laps, drivers)
with tabs[2]: telemetry_tab(laps, drivers)
with tabs[3]: tyres_tab(laps)
with tabs[4]: pits_tab(laps)
with tabs[5]: positions_tab(laps)
with tabs[6]: delta_tab(laps, drivers)
with tabs[7]: head_to_head_tab(laps, drivers)
with tabs[8]: undercut_tab(laps, drivers)
with tabs[9]: tyre_life_tab(laps)
with tabs[10]: rating_tab(laps)
with tabs[11]: summary_tab(laps)