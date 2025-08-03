import streamlit as st
import pandas as pd
import numpy as np


st.title('Text To Anki Tool')



col1, col2 = st.columns(2, gap="small")

with col1:
    st.header("Text \n Input ", divider=True)
    with st.container(border=True):
        st.write("This is outside the container")


with col2:
    st.header("Anki Flashcard Template", divider=True)
    with st.container(border=True):
        st.write("This is inside the container")
    

    
