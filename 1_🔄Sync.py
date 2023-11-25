import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="SyncStock",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="./icon.png"
)

pedidos = pd.read_csv("pedidos.csv")
#HEADER
with st.container():
    st.title("Pedidos - Martin Bower")

with st.container():
    update = st.button("Atualizar Pedidos🔄")
    if update:
        with st.spinner("Buscando pedidos..."):
            time.sleep(2)

        st.subheader("Número do Pedido:")
        st.info(pedidos["numero_pedido"].unique())

        st.subheader("Itens do Pedido")
        st.dataframe(
            pedidos[["produto", "quantidade", "fardo", "localizacao"]],
            column_config={
                "produto": "Produto",
                "quantidade": "Quantidade",
                "fardo": "Fardo",
                "localizacao": "Localização"
            },
            use_container_width=True,
            hide_index=True
        )