# Import python packages
import streamlit as st
import time
import pandas as pd
from snowflake.snowpark.context import get_active_session
import requests

# Write directly to the app
st.title(f"Streamlit 1.42 Demo Test :streamlit:")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)

# Get the current credentials
session = get_active_session()

#st.write(st.experimental_user)

st.subheader("New Components", divider=True)
'''**`st.pills`**'''
options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

'''**`st.segmented_control`**'''
options = ["North", "East", "South", "West"]
selection = st.segmented_control(
    "Directions", options, selection_mode="multi"
)
st.markdown(f"Your selected options: {selection}.")

'''**`st.audio_input`**'''
audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)


st.subheader("`st.metric` now supports borders", divider=True)
a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)


st.subheader("Updated Material Symbols", divider=True)
st.markdown("Calendar Month :material/calendar_month:")
st.markdown("Filter Alt :material/filter_alt:")
st.markdown("Settings Accessibility :material/settings_accessibility:")

st.subheader("Columns support borders", divider=True)
left, middle, right = st.columns(3, border=True)

left.markdown("Lorem ipsum " * 10)
middle.markdown("Lorem ipsum " * 5)
right.markdown("Lorem ipsum ")


st.subheader("`st.table` now support Markdown strings", divider=True)
df = pd.DataFrame(
    {
        "Command": ["**st.table**", "*st.dataframe*"],
        "Type": ["`static`", "`interactive`"],
        "Docs": [
            "[:rainbow[docs]](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)",
            "[:book:](https://docs.streamlit.io/develop/api-reference/data/st.table)",
        ],
    }
)
st.table(df)

st.subheader("`st.spinner` shows elapsed time", divider=True)
with st.spinner("Wait for it...", show_time=True):
    time.sleep(4)
st.success("Done!")
st.button("Rerun")