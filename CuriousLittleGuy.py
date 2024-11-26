import tempfile
from PIL import Image
import numpy as np
from DefinitiveVersion import img_verification
import streamlit as st
import requests
import io

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    return img

st.set_page_config(
    page_title="...",
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
if img_file_buffer is not None:
    # Lendo a imagem com PIL
    img = Image.open(img_file_buffer)

    # Salvando a imagem no diretório temporário
    with tempfile.TemporaryDirectory() as directory:
        img_name = f"{directory}/captured_image.jpg"
        img.save(img_name)

        # Caminho relativo para o arquivo de referência
        reference_url = st.secrets["general"]["image_url"]
        reference_img = load_image_from_url(reference_url)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            temp_file_path = temp_file.name
            reference_img.save(temp_file_path)

        # Verificação
        with st.spinner('Hmmmm'):
            result = img_verification(img_name, temp_file_path)

        if result:
            st.switch_page("pages/positiveresultpage.py")
        else:
            st.switch_page("pages/negativeresultpage.py")
