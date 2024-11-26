from deepface import DeepFace
import tempfile
import cv2
import numpy as np
from DefinitiveVersion import img_verification
from Decoder import decode
import streamlit as st
import os
import requests
from PIL import Image
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(image_array, -1)  # -1 para carregar a imagem no formato original
    return img


st.set_page_config(
    page_title="Teste",
    page_icon="🤔",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS para ajustar a aparência
st.markdown("""
    <style>
    body { background-color: #E8F0F2; }
    h1 { color: #5A7F6F; text-align: center; margin-top: 20px; }
    .stButton>button { background-color: #5A7F6F; color: white; border-radius: 5px; height: 50px; width: 150px; font-size: 16px; }
    [data-testid="collapsedControl"] { display: none; }
    .stCamera { display: flex; justify-content: center; align-items: center; margin-top: 50px; }
    video { max-width: 100%; height: auto; }
    </style>
    """, unsafe_allow_html=True)

# Título no topo
st.title('Quem é você?')

# Câmera ou upload
img_file_buffer = st.camera_input("Cam1", label_visibility="hidden")
if img_file_buffer != None:
    bytes_photo = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_photo, np.uint8), cv2.IMREAD_COLOR)
    
    # Uso de diretório temporário
    with tempfile.TemporaryDirectory() as directory:
        img_name = f"{directory}/captured_image.jpg"
        cv2.imwrite(img_name, cv2_img)

        #Caminho relativo para o arquivo de referência
        reference_url = st.secrets["general"]["image_url"]
        reference_img = load_image_from_url(reference_url)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            temp_file_path = temp_file.name
            cv2.imwrite(temp_file_path, reference_img)
        
        # Verificação
        with st.spinner('Hmmmm'):
            result = img_verification(img_name, temp_file_path)

        if result:
            st.switch_page("pages/positiveresultpage.py")
        else:
            st.switch_page("pages/negativeresultpage.py")
