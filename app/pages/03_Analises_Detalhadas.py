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


st.subheader("Comparação de Lançamentos por País")
df['country'] = df['country'].fillna('')
paises_unicos = sorted(set([p for sublist in df['country'].str.split(', ') for p in sublist if p]))
paises_padrao = ["United States", "India"]
paises_padrao_validos = [p for p in paises_padrao if p in paises_unicos]
if len(paises_padrao_validos) < 2:
    paises_padrao_validos = paises_unicos[:2]
comparacao_paises_sel = st.multiselect(
    "Selecione dois países para comparar",
    options=paises_unicos,
    default=paises_padrao_validos
)
if len(comparacao_paises_sel) != 2:
    st.warning("Por favor, selecione exatamente dois países.")
else:
    regex = '|'.join(comparacao_paises_sel)
    df_pais_comparacao = df[df['country'].str.contains(regex, case=False, na=False)]
    df_exploded = df_pais_comparacao.assign(country=df_pais_comparacao['country'].str.split(', ')).explode('country')
    df_filtrado = df_exploded[df_exploded['country'].isin(comparacao_paises_sel)]
    df_ano_pais = (
        df_filtrado.groupby(['release_year', 'country'])
        .size()
        .reset_index(name='Lançamentos')
    )
    fig3 = px.line(
        df_ano_pais,
        x='release_year',
        y='Lançamentos',
        color='country',
        title="Lançamentos de títulos por país ao longo dos anos",
        labels={'release_year': 'Ano de Lançamento', 'country': 'País'}
    )
    fig3.update_layout(legend_title_text='País', xaxis=dict(dtick=1))
    st.plotly_chart(fig3)
