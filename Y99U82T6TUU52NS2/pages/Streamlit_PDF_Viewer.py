import os
from tempfile import NamedTemporaryFile
from streamlit_pdf_viewer import pdf_viewer
import streamlit as st


st.title("PDF Viewer")

st.header("Height and width")
resolution_boost = st.slider(label="Resolution boost", min_value=1, max_value=10, value=1)
width = st.slider(label="PDF width", min_value=100, max_value=1000, value=700)
height = st.slider(label="PDF height", min_value=-1, max_value=10000, value=-1)


uploaded_file = st.file_uploader("Upload an article",
                                 type=("pdf"),
                                 help="The full-text is extracted using Grobid. ")

if uploaded_file:
    response = None
    with (st.spinner('Reading file...')):
        binary = uploaded_file.getvalue()
        tmp_file = NamedTemporaryFile()
        tmp_file.write(bytearray(binary))
        st.session_state['binary'] = binary

if height > -1:
    pdf_viewer(
        input=st.session_state['binary'],
        width=width,
        height=height,
    )