import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix Dashboard", page_icon="🎬")

st.title("🎬 Bem-vindo ao Netflix Dashboard")
st.markdown("""
Este painel interativo apresenta uma análise dos títulos disponíveis na Netflix com base em dados públicos.  
Utilize o menu lateral para navegar entre os gráficos e interagir com os dados.
""")
st.sidebar.success("Escolha uma página no menu ☝️")

@st.cache_data
def load_data():
    return pd.read_csv("data/netflix_titles.csv")

df = load_data()

st.subheader("Distribuição de Tipos de Conteúdo")
tipo_counts = df['type'].value_counts().reset_index()
tipo_counts.columns = ['Tipo', 'Quantidade']
fig = px.pie(tipo_counts, names='Tipo', values='Quantidade', title='Distribuição entre Filmes e Séries')
st.plotly_chart(fig)
