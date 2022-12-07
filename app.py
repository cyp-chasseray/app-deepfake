import streamlit as st
import numpy as np
import requests
from PIL import Image
import io

'''
# DEEPFAKE HUNTER APPLICATION

'''

url = 'https://deepfakehuntercloud2-bnv74lx52q-nw.a.run.app/predict'

uploaded_files = st.file_uploader("Choose photos to upload", accept_multiple_files=False, type=['png', 'jpeg', 'jpg'])
if uploaded_files is not None:
    st.image(uploaded_files, channels="BGR")

if st.button('Prédire'):

    files={'image' : uploaded_files}

    response = requests.post(url, files=files)
    if response.status_code == 200:
        wb = response.json()
        if wb['result'] < 0.5:
            real = '<p style="font-family:sans-serif; color:Green; font-size: 20px;">Real</p>'
            st.markdown(real, unsafe_allow_html=True)
        else:
            fake = '<p style="font-family:sans-serif; color:Red; font-size: 20px;">Fake</p>'
            st.markdown(fake, unsafe_allow_html=True)
    else:
        st.write('Error ', str(response.status_code))
