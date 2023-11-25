import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="SyncStock",
    initial_sidebar_state="expanded",
    layout="wide",
    page_icon="./icon.png"
)

#HEADER
with st.container():
    st.title("Dashboard - Estoque Martin Bower")

#IMPORTAÇÃO DOS DADOS
products = pd.read_csv("products.csv")
avaria = 0
saida = 0

#DASHBOARD GERAL

with st.container():

    col_001, col_002 = st.columns(2)

    with col_001:
        st.metric(
            label="Estoque Atual",
            value=(products["quantidade_boa"].sum() - avaria - saida)
        )
    with col_002:
        st.metric(
            label="Avaria",
            value=(products["quantidade_ruim"].sum() + avaria)
        )
        
    fig_boa = px.pie(
            products,
            names="nome",
            values="quantidade_boa",
            title="Quantidade Boa por Produto",
            hole=.4
        )
    st.plotly_chart(fig_boa)
    fig_ruim = px.pie(
            products,
            names="nome",
            values="quantidade_ruim",
            title="Avaria por Produto",
            hole=.5
        )
    st.plotly_chart(fig_ruim)

#DASHBOARD POR PRODUTO
st.divider()
st.header("Estoque por Produto")

with st.container():
    filtro_produtos = st.selectbox(
        "Selecione o produto",
        (products["nome"].unique())
    )

nome_produto = products[products["nome"]==filtro_produtos]

st.divider()
with st.container():
    col01, col02, col03 = st.columns(3)

    with col01:
        st.metric(
            label="Estoque Atual",
            value=nome_produto["quantidade_boa"].sum()
        )
    with col02:
        st.metric(
            label="Avaria",
            value=nome_produto["quantidade_ruim"].sum()
        )
    with col03:
        st.metric(
            label="Última atualização",
            value="1"
        )
