import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análises Detalhadas", page_icon="🔍")

st.title("🔍 Análises Detalhadas")

@st.cache_data
def load_data():
    df = pd.read_csv("data/netflix_titles.csv")
    df['release_year'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
    return df

df = load_data()

st.subheader("Distribuição por Gênero ao Longo dos Anos")
df['listed_in'] = df['listed_in'].str.split(', ')
df_genero = df.explode('listed_in')
genero_escolhido = st.selectbox("Selecione um gênero", sorted(df_genero['listed_in'].dropna().unique()))
df_genero_filtrado = df_genero[df_genero['listed_in'] == genero_escolhido]
genero_ano = df_genero_filtrado.groupby('release_year').size().reset_index(name='Quantidade')
fig1 = px.bar(genero_ano, x='release_year', y='Quantidade', title=f"Evolução do gênero '{genero_escolhido}' por ano")
st.plotly_chart(fig1)

st.subheader("Lançamentos por País ao Longo dos Anos")
df['country'] = df['country'].fillna('')
paises_unicos = sorted(set([p for sublist in df['country'].str.split(', ') for p in sublist if p]))
pais_sel = st.selectbox("Selecione um país", paises_unicos)
df_pais = df[df['country'].str.contains(pais_sel)]
df_pais_ano = df_pais.groupby('release_year').size().reset_index(name='Lançamentos')
fig2 = px.area(df_pais_ano, x='release_year', y='Lançamentos', title=f"Lançamentos de títulos do país '{pais_sel}' ao longo dos anos")
st.plotly_chart(fig2)
