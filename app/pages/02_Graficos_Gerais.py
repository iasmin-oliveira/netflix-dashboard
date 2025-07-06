import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gráficos Gerais", page_icon="📊")

st.title("📊 Gráficos Gerais")

@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    df['release_year'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
    df['duration_min'] = df['duration'].str.extract('(\d+)').astype(float)
    return df

df = load_data()

st.subheader("Top 10 Países com Mais Títulos")
paises = df['country'].dropna().str.split(', ').explode()
top_paises = paises.value_counts().nlargest(10).reset_index()
top_paises.columns = ['País', 'Quantidade']
fig1 = px.bar(top_paises, x='País', y='Quantidade', title='Top 10 Países com mais títulos')
st.plotly_chart(fig1)

st.subheader("Duração Média dos Filmes ao Longo dos Anos")
df_filmes = df[df['type'] == 'Movie']
media_duracao = df_filmes.groupby('release_year')['duration_min'].mean().dropna().reset_index()
intervalo = st.slider("Escolha o intervalo de anos", int(media_duracao['release_year'].min() or 2000), int(media_duracao['release_year'].max() or 2020), (2010, 2020))
media_filtrada = media_duracao[media_duracao['release_year'].between(*intervalo)]
fig2 = px.line(media_filtrada, x='release_year', y='duration_min', title='Duração média dos filmes por ano')
st.plotly_chart(fig2)
