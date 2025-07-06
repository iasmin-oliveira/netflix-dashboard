import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Netflix Dashboard", page_icon="🎬")
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('data:image/png;base64,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',)
st.title("🎬 Bem-vindo ao Netflix Dashboard")
st.markdown("""
Este painel interativo apresenta uma análise dos títulos disponíveis na Netflix com base em dados públicos.  
""")

st.title("🎯 Objetivo do Dashboard")
st.markdown("""
O Netflix Dashboard tem como objetivo apresentar, de forma visual e interativa, uma análise exploratória do catálogo da Netflix, 
utilizando um conjunto de dados público disponível no Kaggle. Por meio de gráficos e filtros dinâmicos, é possível identificar padrões, 
tendências e características importantes sobre os títulos disponibilizados na plataforma, como tipo, país de origem, duração média, gênero e evolução ao longo dos anos.
""")

st.title("🧭 Como Navegar Entre as Seções")
st.markdown("""
O dashboard está dividido em múltiplas páginas, acessíveis pela barra lateral (sidebar):

🏠 Página Inicial: Introdução ao projeto e gráfico de distribuição entre filmes e séries.

📊 Gráficos Gerais: Apresenta o Top 10 países com mais títulos e a evolução da duração média dos filmes ao longo do tempo.

🔍 Análises Detalhadas: Permite explorar dados por gênero e por país, com filtros interativos para aprofundar a visualização dos lançamentos ao longo dos anos.

Basta clicar no nome da página no menu lateral para alternar entre as seções.
""")

st.title("🧩 Como os Filtros Influenciam os Dados")
st.markdown("""
O dashboard oferece filtros interativos que permitem modificar dinamicamente os dados exibidos nos gráficos, como:

Selectbox de gênero: Filtra os títulos por gênero (ex: Drama, Comédia, Documentário), permitindo visualizar sua evolução ao longo dos anos.

Selectbox de país: Exibe a distribuição dos lançamentos por ano para o país selecionado.

Slider de ano: Permite restringir a análise de duração média dos filmes a um intervalo de tempo específico.

Esses filtros possibilitam ao usuário explorar diferentes perspectivas dos dados, comparando países, gêneros, tipos e períodos de forma personalizada.
""")


st.sidebar.success("Escolha uma página no menu ☝️")

@st.cache_data
def load_data():
    return pd.read_csv("data/netflix_titles.csv")

df = load_data()

