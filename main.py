import streamlit as st

import os
from hashlib import blake2b
from tempfile import NamedTemporaryFile


from streamlit_pdf_viewer import pdf_viewer

# Remove default container padding/margins


st.session_state['doc_id'] = None
st.session_state['binary'] = None
st.session_state['uploaded'] = False

st.title('Text To Anki Tool')

def new_file():
    st.session_state['doc_id'] = None
    st.session_state['uploaded'] = True
    st.session_state['binary'] = None
    
uploaded_file = st.file_uploader("Upload PDF",
                                 type="pdf",
                                 on_change=new_file
                                 )

enable_text = st.toggle('Render text in PDF', value=False, disabled=False,
                            help="Enable the selection and copy-paste on the PDF")



col1, col2, col3 = st.columns([4,2,2], gap="small")




with col1:
    st.header("Text \n Input ", divider=True)
    with st.container(border=True):
        st.write("This is outside the container")
        if uploaded_file:
            if not st.session_state['binary']:
                response = None
                with (st.spinner('Reading file, calling Grobid...')):
                    binary = uploaded_file.getvalue()
                    tmp_file = NamedTemporaryFile()
                    tmp_file.write(bytearray(binary))
                    st.session_state['binary'] = binary
                
                pdf_viewer(
                        input=st.session_state['binary'],
                        render_text = enable_text
                    )


with col2:
    st.header("Text Input", divider=True)
    with st.container(border=True):
        st.write("This is inside the container")

with col3:
    st.header("Edit Anki Card", divider=True)
    with st.container(border=True):
        st.write("This is inside the container")

    
