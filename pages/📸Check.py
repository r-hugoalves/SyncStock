import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="SyncStock",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="./icon.png"
)

camera_on = st.toggle("Ativar câmera")

if camera_on:
    picture = st.camera_input("Take a picture")
    if picture:
        with st.spinner("Validando dados..."):
            time.sleep(3)
            st.success("Liberado!")
            st.image(picture)