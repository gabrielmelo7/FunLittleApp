import streamlit as st
st.set_page_config(
    page_title="Aeee",
    page_icon="😃",
    layout="centered",
    initial_sidebar_state="collapsed",
)

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
        margin-top: 10px; 
        position: absolute;
        bottom: -400px; 
        left: 50%;
        transform: translateX(-50%);
    }
    [data-testid="collapsedControl"] {
        display: none; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Você é ***muito*** linda!")
st.write("Feliz dia do bombom, feliz dois anos. Eu te amo muito, meu bem!!")
st.subheader("💚🍬")
st.balloons()

go_back = st.button("Voltar")
if go_back:
    st.switch_page("CuriousLittleGuy.py")

