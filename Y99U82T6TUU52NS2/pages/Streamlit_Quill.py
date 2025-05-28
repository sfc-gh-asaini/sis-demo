import streamlit as st

from streamlit_quill import st_quill

# Spawn a new Quill editor
content = st_quill()

# Display editor's content as you type
content