import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="SyncStock",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="./icon.png"
)

#LEITURA DOS DADOS
pedidos = pd.read_csv("pedidos.csv")
products = pd.read_csv("products.csv")

#HEADER
with st.container():
    st.title("Baixar Pedidos - Martin Bower")

with st.container():
        st.subheader("Pedido Atual")
        st.info(pedidos["numero_pedido"].unique())

        st.subheader("Itens do Pedido")
        
        with st.container():
            item_pedido = st.selectbox(
                "Selecione o produto",
                (pedidos["produto"].unique())
            )

            validacao_avaria = pd.DataFrame(
                 {
                      "Tem avaria?": [True],
                      "Qual tipo de avaria?": [""],
                      "Quantidade de Produtos com Avaria:": [""]
                 }
            )

            send_info = st.data_editor(
                 validacao_avaria,
                 column_config={
                      "Tem avaria?": st.column_config.CheckboxColumn(
                           default=False
                      ),
                      "": None
                 }
            )

            enviar_info = st.button("Atualizar estoque")
            if enviar_info:
               with st.spinner("Enviando informações..."):
                    time.sleep(2)
                    st.success("Informações enviadas!")