import streamlit as st

# Configuração inicial
st.set_page_config(
    page_title="Não.",
    page_icon="😒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS padronizado com a página anterior
st.markdown("""
    <style>
    body {
        background-color: #E8F0F2; /* Fundo claro e uniforme */
    }
    h1, h2, h3, h4 {
        color: #5A7F6F; /* Verde suave e acinzentado */
        text-align: left; /* Centraliza os títulos */
        margin-bottom: 10px; /* Espaçamento menor abaixo do título */
    }
    .stButton>button {
        background-color: #5A7F6F; /* Cor do botão uniforme */
        color: white;
        border-radius: 5px;
        height: 50px;
        width: 150px;
        font-size: 16px;
        margin-top: 10px; /* Espaço superior no botão */
        position: absolute;
        bottom: -400px; /* Coloca o botão na parte inferior da página */
        left: 50%;
        transform: translateX(-50%);
    }
    [data-testid="collapsedControl"] {
        display: none; /* Esconde o menu lateral */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Você ***não*** é muito linda.")
st.write("Retire-se, por favor.")

# Botão na parte inferior
if st.button("Voltar"):
    st.switch_page("CuriousLittleGuy.py")
